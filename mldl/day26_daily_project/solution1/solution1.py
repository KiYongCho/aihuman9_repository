# solution1.py
# 회원 재방문 예측 - Dense 이진 분류 강사용 풀이

# 안전한 파일 경로 처리를 위해 Path를 가져옵니다.
from pathlib import Path

# 데이터 처리를 위해 pandas를 가져옵니다.
import pandas as pd

# 수치 계산을 위해 NumPy를 가져옵니다.
import numpy as np

# 그래프 출력을 위해 matplotlib을 가져옵니다.
import matplotlib.pyplot as plt

# 학습/테스트 데이터 분리를 위해 train_test_split을 가져옵니다.
from sklearn.model_selection import train_test_split

# 입력값의 단위를 맞추기 위해 StandardScaler를 가져옵니다.
from sklearn.preprocessing import StandardScaler

# 테스트 성능과 혼동행렬을 확인하기 위해 평가 도구를 가져옵니다.
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay

# TensorFlow Keras를 가져옵니다.
from tensorflow import keras

# 재현 가능한 결과를 위해 난수 시드를 고정합니다.
keras.utils.set_random_seed(42)

# 현재 파이썬 파일이 있는 폴더를 기준 폴더로 사용합니다.
BASE_DIR = Path(__file__).resolve().parent

# CSV 파일의 경로를 지정합니다.
DATA_FILE = BASE_DIR / "team1_data.csv"

# 결과 그래프를 저장할 폴더를 지정합니다.
RESULT_DIR = BASE_DIR / "result"

# 결과 폴더가 없으면 생성합니다.
RESULT_DIR.mkdir(exist_ok=True)

# CSV 파일을 DataFrame으로 읽습니다.
df = pd.read_csv(DATA_FILE, encoding="utf-8-sig")

# 데이터 크기를 출력합니다.
print("[데이터 shape]")
print(df.shape)

# 컬럼별 결측치 개수를 출력합니다.
print("\n[결측치]")
print(df.isna().sum())

# 숫자형 컬럼을 순회합니다.
for col in df.columns:
    # Target 컬럼은 결측치 처리 대상에서 제외합니다.
    if col == "재방문여부":
        continue

    # 각 숫자형 컬럼의 중앙값으로 결측치를 채웁니다.
    df[col] = df[col].fillna(df[col].median())

# Target을 제외한 컬럼을 입력 X로 지정합니다.
X = df.drop(columns=["재방문여부"])

# 재방문 여부를 정답 y로 지정합니다.
y = df["재방문여부"]

# 데이터를 학습용 75%, 테스트용 25%로 나눕니다.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y,
)

# StandardScaler 객체를 생성합니다.
scaler = StandardScaler()

# Training Set을 기준으로 평균과 표준편차를 학습하고 변환합니다.
X_train_scaled = scaler.fit_transform(X_train)

# Test Set에는 Training Set에서 학습한 기준만 적용합니다.
X_test_scaled = scaler.transform(X_test)

# 입력 특성 수를 구합니다.
input_dim = X_train_scaled.shape[1]

# 기본 Dense 모델을 만드는 함수를 정의합니다.
def build_basic_model():
    # 층을 순서대로 연결하는 Sequential 모델을 생성합니다.
    model = keras.Sequential([
        # 한 건의 입력이 input_dim개의 특성을 가진다고 지정합니다.
        keras.layers.Input(shape=(input_dim,)),

        # 첫 번째 은닉층에서 32개 뉴런과 ReLU를 사용합니다.
        keras.layers.Dense(32, activation="relu"),

        # 두 번째 은닉층에서 16개 뉴런과 ReLU를 사용합니다.
        keras.layers.Dense(16, activation="relu"),

        # 이진 분류이므로 출력층은 1개 뉴런과 Sigmoid를 사용합니다.
        keras.layers.Dense(1, activation="sigmoid"),
    ])

    # Adam과 Binary Crossentropy를 사용해 학습 규칙을 설정합니다.
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=0.001),
        loss="binary_crossentropy",
        metrics=["accuracy"],
    )

    # 완성된 모델을 반환합니다.
    return model

# Dropout이 포함된 모델을 만드는 함수를 정의합니다.
def build_dropout_model():
    # Sequential 모델을 생성합니다.
    model = keras.Sequential([
        # 입력 shape를 지정합니다.
        keras.layers.Input(shape=(input_dim,)),

        # 첫 번째 은닉층을 구성합니다.
        keras.layers.Dense(32, activation="relu"),

        # 학습 중 약 30%의 출력을 임시로 0으로 만듭니다.
        keras.layers.Dropout(0.3),

        # 두 번째 은닉층을 구성합니다.
        keras.layers.Dense(16, activation="relu"),

        # 이진 분류 출력층을 구성합니다.
        keras.layers.Dense(1, activation="sigmoid"),
    ])

    # 학습 방법을 설정합니다.
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=0.001),
        loss="binary_crossentropy",
        metrics=["accuracy"],
    )

    # 완성된 모델을 반환합니다.
    return model

# 두 개의 모델을 생성합니다.
basic_model = build_basic_model()
dropout_model = build_dropout_model()

# 두 모델의 구조를 출력합니다.
print("\n[기본 모델]")
basic_model.summary()

print("\n[Dropout 모델]")
dropout_model.summary()

# 검증 손실이 10 Epoch 동안 좋아지지 않으면 학습을 중단하도록 설정합니다.
early_stopping1 = keras.callbacks.EarlyStopping(
    monitor="val_loss",
    patience=10,
    restore_best_weights=True,
)

# 기본 모델을 학습합니다.
history_basic = basic_model.fit(
    X_train_scaled,
    y_train,
    epochs=200,
    batch_size=32,
    validation_split=0.2,
    callbacks=[early_stopping1],
    verbose=0,
)

# 두 번째 모델은 별도의 Callback 객체를 사용합니다.
early_stopping2 = keras.callbacks.EarlyStopping(
    monitor="val_loss",
    patience=10,
    restore_best_weights=True,
)

# Dropout 모델을 학습합니다.
history_dropout = dropout_model.fit(
    X_train_scaled,
    y_train,
    epochs=200,
    batch_size=32,
    validation_split=0.2,
    callbacks=[early_stopping2],
    verbose=0,
)

# 각 모델이 실제로 수행한 Epoch 수를 출력합니다.
print("\n[실제 수행 Epoch]")
print("기본 모델:", len(history_basic.history["loss"]))
print("Dropout 모델:", len(history_dropout.history["loss"]))

# 기본 모델의 테스트 확률을 예측합니다.
basic_prob = basic_model.predict(X_test_scaled, verbose=0).ravel()

# 확률이 0.5 이상이면 1로 분류합니다.
basic_pred = (basic_prob >= 0.5).astype(int)

# Dropout 모델의 테스트 확률을 예측합니다.
dropout_prob = dropout_model.predict(X_test_scaled, verbose=0).ravel()

# 확률을 0/1 클래스로 변환합니다.
dropout_pred = (dropout_prob >= 0.5).astype(int)

# 두 모델의 테스트 정확도를 계산합니다.
basic_acc = accuracy_score(y_test, basic_pred)
dropout_acc = accuracy_score(y_test, dropout_pred)

# 정확도를 출력합니다.
print("\n[테스트 정확도]")
print("기본 모델:", round(basic_acc, 4))
print("Dropout 모델:", round(dropout_acc, 4))

# 두 모델의 validation loss를 비교합니다.
plt.figure(figsize=(9, 5))
plt.plot(history_basic.history["val_loss"], label="Basic val_loss")
plt.plot(history_dropout.history["val_loss"], label="Dropout val_loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Validation Loss 비교")
plt.legend()
plt.tight_layout()
plt.savefig(RESULT_DIR / "01_val_loss_compare.png", dpi=150)
plt.show()

# 정확도가 높은 모델을 최종 모델로 선택합니다.
if dropout_acc >= basic_acc:
    best_model = dropout_model
    best_pred = dropout_pred
    best_name = "Dropout Dense"
else:
    best_model = basic_model
    best_pred = basic_pred
    best_name = "Basic Dense"

# 최종 모델의 혼동행렬을 그립니다.
ConfusionMatrixDisplay.from_predictions(y_test, best_pred)
plt.title(f"Confusion Matrix - {best_name}")
plt.tight_layout()
plt.savefig(RESULT_DIR / "02_confusion_matrix.png", dpi=150)
plt.show()

# 최종 선택 결과를 출력합니다.
print("\n[최종 선택]")
print(best_name)
