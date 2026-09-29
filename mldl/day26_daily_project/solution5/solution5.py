# solution5.py
# 다음 시점 전력수요 예측 - SimpleRNN vs LSTM 회귀 강사용 풀이

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
from tensorflow import keras

# 재현 가능한 결과를 위해 난수 시드를 고정합니다.
keras.utils.set_random_seed(42)

# 파일과 결과 폴더 경로를 지정합니다.
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "team5_data.npz"
RESULT_DIR = BASE_DIR / "result"
RESULT_DIR.mkdir(exist_ok=True)

# NPZ 데이터를 읽습니다.
data = np.load(DATA_FILE)

# 입력 시퀀스를 가져옵니다.
X = data["X"]

# 다음 시점 전력수요를 정답으로 가져옵니다.
y = data["y"]

# shape를 확인합니다.
print("[X shape]", X.shape)
print("[y shape]", y.shape)

# 전체 샘플의 80% 위치를 계산합니다.
split_idx = int(len(X) * 0.8)

# 시간 순서를 유지하여 앞쪽을 Training Set으로 사용합니다.
X_train = X[:split_idx]
y_train = y[:split_idx]

# 뒤쪽을 Test Set으로 사용합니다.
X_test = X[split_idx:]
y_test = y[split_idx:]

# 시점당 특성 수를 구합니다.
feature_count = X.shape[2]

# StandardScaler를 만듭니다.
x_scaler = StandardScaler()

# 3차원 Training Set을 2차원으로 펼쳐 scaler를 학습합니다.
X_train_2d = X_train.reshape(-1, feature_count)

# Training Set의 평균과 표준편차를 학습합니다.
x_scaler.fit(X_train_2d)

# Training Set을 같은 shape로 다시 변환합니다.
X_train_scaled = x_scaler.transform(
    X_train.reshape(-1, feature_count)
).reshape(X_train.shape)

# Test Set에는 Training Set 기준을 적용합니다.
X_test_scaled = x_scaler.transform(
    X_test.reshape(-1, feature_count)
).reshape(X_test.shape)

# y도 학습 안정성을 위해 표준화합니다.
y_scaler = StandardScaler()

# y Training Set을 2차원으로 바꾸어 scaler를 학습합니다.
y_train_scaled = y_scaler.fit_transform(
    y_train.reshape(-1, 1)
).ravel()

# 모델 생성에 사용할 timesteps와 features를 구합니다.
timesteps = X.shape[1]
features = X.shape[2]

# SimpleRNN 회귀 모델 생성 함수를 정의합니다.
def build_rnn():
    # Sequential 모델을 생성합니다.
    model = keras.Sequential([
        # 입력 shape를 지정합니다.
        keras.layers.Input(shape=(timesteps, features)),

        # 32개 hidden unit을 가진 SimpleRNN을 사용합니다.
        keras.layers.SimpleRNN(32),

        # 회귀이므로 Dense(1) Linear 출력층을 사용합니다.
        keras.layers.Dense(1),
    ])

    # Adam과 MSE를 사용합니다.
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=0.001),
        loss="mse",
    )

    # 모델을 반환합니다.
    return model

# LSTM 회귀 모델 생성 함수를 정의합니다.
def build_lstm():
    # Sequential 모델을 생성합니다.
    model = keras.Sequential([
        # 입력 shape를 지정합니다.
        keras.layers.Input(shape=(timesteps, features)),

        # 32개 LSTM unit을 사용합니다.
        keras.layers.LSTM(32),

        # 회귀 출력층을 추가합니다.
        keras.layers.Dense(1),
    ])

    # Adam과 MSE를 사용합니다.
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=0.001),
        loss="mse",
    )

    # 모델을 반환합니다.
    return model

# 비교할 두 모델을 준비합니다.
models = {
    "SimpleRNN": build_rnn(),
    "LSTM": build_lstm(),
}

# 모델별 결과를 저장할 리스트를 만듭니다.
results = []

# History를 저장합니다.
histories = {}

# 실제 단위의 예측값을 저장합니다.
predictions = {}

# 모델을 하나씩 반복합니다.
for name, model in models.items():
    # EarlyStopping을 생성합니다.
    early_stopping = keras.callbacks.EarlyStopping(
        monitor="val_loss",
        patience=8,
        restore_best_weights=True,
    )

    # 모델을 학습합니다.
    history = model.fit(
        X_train_scaled,
        y_train_scaled,
        epochs=120,
        batch_size=32,
        validation_split=0.2,
        callbacks=[early_stopping],
        verbose=0,
    )

    # 표준화된 예측값을 구합니다.
    pred_scaled = model.predict(
        X_test_scaled,
        verbose=0,
    ).ravel()

    # 예측값을 원래 전력수요 단위로 되돌립니다.
    pred = y_scaler.inverse_transform(
        pred_scaled.reshape(-1, 1)
    ).ravel()

    # MAE를 계산합니다.
    mae = mean_absolute_error(y_test, pred)

    # RMSE를 계산합니다.
    rmse = mean_squared_error(y_test, pred) ** 0.5

    # 결과를 저장합니다.
    results.append({
        "모델": name,
        "파라미터수": model.count_params(),
        "Epoch수": len(history.history["loss"]),
        "MAE": mae,
        "RMSE": rmse,
    })

    # 그래프 작성을 위해 History를 저장합니다.
    histories[name] = history

    # 예측값도 저장합니다.
    predictions[name] = pred

# 결과를 DataFrame으로 변환합니다.
result_df = pd.DataFrame(results)

# 결과를 출력합니다.
print("\n[모델 비교]")
print(result_df.round(3))

# 두 모델의 validation loss를 비교합니다.
plt.figure(figsize=(9, 5))
for name, history in histories.items():
    plt.plot(
        history.history["val_loss"],
        label=f"{name} val_loss",
    )
plt.xlabel("Epoch")
plt.ylabel("Validation Loss")
plt.title("SimpleRNN vs LSTM - Validation Loss")
plt.legend()
plt.tight_layout()
plt.savefig(RESULT_DIR / "01_val_loss_compare.png", dpi=150)
plt.show()

# RMSE가 가장 낮은 모델을 선택합니다.
best_name = result_df.sort_values(
    "RMSE",
    ascending=True,
).iloc[0]["모델"]

# 선택 모델의 예측값을 가져옵니다.
best_pred = predictions[best_name]

# 전체 테스트 구간 중 앞 180개 정도를 선그래프로 비교합니다.
show_n = min(180, len(y_test))

# 그래프 크기를 지정합니다.
plt.figure(figsize=(12, 5))

# 실제값을 선그래프로 그립니다.
plt.plot(
    np.arange(show_n),
    y_test[:show_n],
    label="Actual",
)

# 예측값을 선그래프로 그립니다.
plt.plot(
    np.arange(show_n),
    best_pred[:show_n],
    label=f"Predicted - {best_name}",
)

# 그래프 정보를 설정합니다.
plt.xlabel("Test Timestep")
plt.ylabel("Power Demand")
plt.title("실제 전력수요 vs 예측 전력수요")
plt.legend()
plt.tight_layout()
plt.savefig(RESULT_DIR / "02_actual_vs_prediction.png", dpi=150)
plt.show()

# 최종 선택 모델을 출력합니다.
print("\n[최종 선택]")
print(best_name)
