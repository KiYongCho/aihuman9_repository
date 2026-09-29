# solution2.py
# 배송 소요시간 예측 - Dense 회귀 강사용 풀이

from pathlib import Path
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
from tensorflow import keras

# 재현 가능한 결과를 위해 난수 시드를 고정합니다.
keras.utils.set_random_seed(42)

# 파일과 결과 폴더 경로를 지정합니다.
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "team2_data.csv"
RESULT_DIR = BASE_DIR / "result"
RESULT_DIR.mkdir(exist_ok=True)

# 데이터를 읽습니다.
df = pd.read_csv(DATA_FILE, encoding="utf-8-sig")

# 데이터 크기와 결측치를 확인합니다.
print("[데이터 shape]")
print(df.shape)

print("\n[결측치]")
print(df.isna().sum())

# Target을 제외한 컬럼의 결측치를 중앙값으로 처리합니다.
for col in df.columns:
    if col != "배송소요시간_분":
        df[col] = df[col].fillna(df[col].median())

# 입력과 정답을 분리합니다.
X = df.drop(columns=["배송소요시간_분"])
y = df["배송소요시간_분"]

# Train/Test를 나눕니다.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
)

# 입력 특성을 표준화합니다.
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 입력 특성 수를 저장합니다.
input_dim = X_train_scaled.shape[1]

# 동일 구조의 모델을 반복 생성하기 위해 함수를 정의합니다.
def build_model():
    # Dense 회귀 모델을 만듭니다.
    model = keras.Sequential([
        # 입력 특성 수를 지정합니다.
        keras.layers.Input(shape=(input_dim,)),

        # 첫 번째 은닉층입니다.
        keras.layers.Dense(32, activation="relu"),

        # 두 번째 은닉층입니다.
        keras.layers.Dense(16, activation="relu"),

        # 회귀 문제이므로 출력 뉴런은 1개이며 Linear 동작을 사용합니다.
        keras.layers.Dense(1),
    ])

    # Adam과 MSE를 사용합니다.
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=0.001),
        loss="mse",
        metrics=["mae"],
    )

    # 모델을 반환합니다.
    return model

# 실험 결과를 저장할 리스트를 만듭니다.
experiments = []

# History 객체를 저장할 딕셔너리를 만듭니다.
histories = {}

# 예측값을 저장할 딕셔너리를 만듭니다.
predictions = {}

# 비교할 Batch Size를 순회합니다.
for batch_size in [16, 64]:
    # 매 실험마다 새로운 모델을 만듭니다.
    model = build_model()

    # EarlyStopping을 새로 만듭니다.
    early_stopping = keras.callbacks.EarlyStopping(
        monitor="val_loss",
        patience=10,
        restore_best_weights=True,
    )

    # 학습 시작 시간을 기록합니다.
    start_time = time.perf_counter()

    # 모델을 학습합니다.
    history = model.fit(
        X_train_scaled,
        y_train,
        epochs=250,
        batch_size=batch_size,
        validation_split=0.2,
        callbacks=[early_stopping],
        verbose=0,
    )

    # 학습 종료 시간을 이용해 소요 시간을 계산합니다.
    elapsed = time.perf_counter() - start_time

    # 테스트 데이터의 배송 시간을 예측합니다.
    pred = model.predict(X_test_scaled, verbose=0).ravel()

    # MAE를 계산합니다.
    mae = mean_absolute_error(y_test, pred)

    # RMSE를 계산합니다.
    rmse = mean_squared_error(y_test, pred) ** 0.5

    # 실제 수행 Epoch 수를 계산합니다.
    epochs_run = len(history.history["loss"])

    # 결과를 리스트에 추가합니다.
    experiments.append({
        "batch_size": batch_size,
        "MAE": mae,
        "RMSE": rmse,
        "epochs": epochs_run,
        "seconds": elapsed,
    })

    # 그래프 작성을 위해 History를 저장합니다.
    histories[batch_size] = history

    # 실제값/예측값 비교를 위해 예측값도 저장합니다.
    predictions[batch_size] = pred

# 결과를 DataFrame으로 변환합니다.
result_df = pd.DataFrame(experiments)

# 결과를 출력합니다.
print("\n[Batch Size 비교]")
print(result_df.round(3))

# validation loss를 비교합니다.
plt.figure(figsize=(9, 5))
for batch_size, history in histories.items():
    plt.plot(
        history.history["val_loss"],
        label=f"batch={batch_size}",
    )
plt.xlabel("Epoch")
plt.ylabel("Validation Loss")
plt.title("Batch Size별 Validation Loss")
plt.legend()
plt.tight_layout()
plt.savefig(RESULT_DIR / "01_batch_val_loss.png", dpi=150)
plt.show()

# MAE가 가장 작은 실험을 선택합니다.
best_row = result_df.loc[result_df["MAE"].idxmin()]

# 최적 Batch Size를 가져옵니다.
best_batch = int(best_row["batch_size"])

# 선택된 예측값을 가져옵니다.
best_pred = predictions[best_batch]

# 실제값과 예측값을 산점도로 비교합니다.
plt.figure(figsize=(6, 6))
plt.scatter(y_test, best_pred, alpha=0.6)

# 실제값=예측값인 기준선을 그립니다.
min_v = min(y_test.min(), best_pred.min())
max_v = max(y_test.max(), best_pred.max())
plt.plot([min_v, max_v], [min_v, max_v], linestyle="--")

# 그래프 정보를 설정합니다.
plt.xlabel("실제 배송시간(분)")
plt.ylabel("예측 배송시간(분)")
plt.title(f"실제값 vs 예측값 - batch={best_batch}")
plt.tight_layout()
plt.savefig(RESULT_DIR / "02_actual_vs_prediction.png", dpi=150)
plt.show()

# 최종 선택 결과를 출력합니다.
print("\n[최종 선택 Batch Size]")
print(best_batch)
