# solution4.py
# 센서 이상 징후 판별 - SimpleRNN vs LSTM 강사용 풀이

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay
from tensorflow import keras

# 재현 가능한 결과를 위해 난수 시드를 고정합니다.
keras.utils.set_random_seed(42)

# 파일과 결과 폴더 경로를 지정합니다.
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "team4_data.npz"
RESULT_DIR = BASE_DIR / "result"
RESULT_DIR.mkdir(exist_ok=True)

# NPZ 데이터를 읽습니다.
data = np.load(DATA_FILE)

# 시퀀스 입력을 가져옵니다.
X = data["X"]

# 정답 라벨을 가져옵니다.
y = data["y"]

# shape를 출력합니다.
print("[X shape]", X.shape)
print("[y shape]", y.shape)

# 입력 shape에서 timesteps와 features를 구합니다.
timesteps = X.shape[1]
features = X.shape[2]

# Train/Test를 75:25로 분리합니다.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y,
)

# SimpleRNN 모델 생성 함수를 정의합니다.
def build_rnn():
    # Sequential 모델을 생성합니다.
    model = keras.Sequential([
        # 한 샘플이 timesteps x features 형태임을 지정합니다.
        keras.layers.Input(shape=(timesteps, features)),

        # 24차원 hidden state를 사용하는 SimpleRNN을 추가합니다.
        keras.layers.SimpleRNN(24),

        # 이진 분류 출력층을 추가합니다.
        keras.layers.Dense(1, activation="sigmoid"),
    ])

    # 학습 방법을 설정합니다.
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=0.001),
        loss="binary_crossentropy",
        metrics=["accuracy"],
    )

    # 모델을 반환합니다.
    return model

# LSTM 모델 생성 함수를 정의합니다.
def build_lstm():
    # Sequential 모델을 생성합니다.
    model = keras.Sequential([
        # 입력 shape를 지정합니다.
        keras.layers.Input(shape=(timesteps, features)),

        # 24개의 LSTM unit을 사용합니다.
        keras.layers.LSTM(24),

        # 이진 분류 출력층을 추가합니다.
        keras.layers.Dense(1, activation="sigmoid"),
    ])

    # 학습 방법을 설정합니다.
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=0.001),
        loss="binary_crossentropy",
        metrics=["accuracy"],
    )

    # 모델을 반환합니다.
    return model

# 모델을 딕셔너리로 준비합니다.
models = {
    "SimpleRNN": build_rnn(),
    "LSTM": build_lstm(),
}

# 모델별 결과를 저장합니다.
results = []

# History를 저장합니다.
histories = {}

# 예측값을 저장합니다.
predictions = {}

# 각 모델을 순서대로 학습합니다.
for name, model in models.items():
    # 모델의 구조를 확인합니다.
    print(f"\n[{name} summary]")
    model.summary()

    # 같은 조건의 EarlyStopping을 만듭니다.
    early_stopping = keras.callbacks.EarlyStopping(
        monitor="val_loss",
        patience=8,
        restore_best_weights=True,
    )

    # 모델을 학습합니다.
    history = model.fit(
        X_train,
        y_train,
        epochs=120,
        batch_size=32,
        validation_split=0.2,
        callbacks=[early_stopping],
        verbose=0,
    )

    # 테스트 확률을 예측합니다.
    prob = model.predict(X_test, verbose=0).ravel()

    # 0.5 기준으로 클래스를 만듭니다.
    pred = (prob >= 0.5).astype(int)

    # 테스트 정확도를 계산합니다.
    acc = accuracy_score(y_test, pred)

    # 결과를 저장합니다.
    results.append({
        "모델": name,
        "파라미터수": model.count_params(),
        "Epoch수": len(history.history["loss"]),
        "최저_val_loss": min(history.history["val_loss"]),
        "최종_val_accuracy": history.history["val_accuracy"][-1],
        "테스트정확도": acc,
    })

    # 그래프를 위해 History를 저장합니다.
    histories[name] = history

    # 혼동행렬을 위해 예측값을 저장합니다.
    predictions[name] = pred

# 결과를 DataFrame으로 변환합니다.
result_df = pd.DataFrame(results)

# 결과를 출력합니다.
print("\n[모델 비교]")
print(result_df.round(4))

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

# 테스트 정확도가 가장 높은 모델을 선택합니다.
best_name = result_df.sort_values(
    "테스트정확도",
    ascending=False,
).iloc[0]["모델"]

# 선택한 모델의 예측값을 가져옵니다.
best_pred = predictions[best_name]

# 혼동행렬을 그립니다.
ConfusionMatrixDisplay.from_predictions(y_test, best_pred)
plt.title(f"Confusion Matrix - {best_name}")
plt.tight_layout()
plt.savefig(RESULT_DIR / "02_confusion_matrix.png", dpi=150)
plt.show()

# 최종 모델 이름을 출력합니다.
print("\n[최종 선택]")
print(best_name)
