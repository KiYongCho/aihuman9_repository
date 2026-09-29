# solution3.py
# 제품 표면 패턴 판별 - CNN 강사용 풀이

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay
from tensorflow import keras

# 난수 시드를 고정합니다.
keras.utils.set_random_seed(42)

# 파일과 결과 폴더 경로를 지정합니다.
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "team3_data.npz"
RESULT_DIR = BASE_DIR / "result"
RESULT_DIR.mkdir(exist_ok=True)

# NPZ 데이터를 읽습니다.
data = np.load(DATA_FILE)

# 이미지 입력 배열을 가져옵니다.
X = data["X"]

# 정답 클래스를 가져옵니다.
y = data["y"]

# 입력과 정답 shape를 확인합니다.
print("[X shape]", X.shape)
print("[y shape]", y.shape)

# 8개의 샘플 이미지를 확인합니다.
plt.figure(figsize=(10, 4))
for i in range(8):
    # 2행 4열 중 i번째 위치를 선택합니다.
    plt.subplot(2, 4, i + 1)

    # 흑백 이미지를 표시합니다.
    plt.imshow(X[i, :, :, 0], cmap="gray", vmin=0, vmax=1)

    # 클래스 이름을 제목으로 표시합니다.
    label_name = "가로" if y[i] == 0 else "세로"
    plt.title(label_name)

    # 축은 이미지 확인에 필요 없으므로 숨깁니다.
    plt.axis("off")

plt.tight_layout()
plt.savefig(RESULT_DIR / "01_samples.png", dpi=150)
plt.show()

# Train/Test 데이터를 75:25로 나눕니다.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y,
)

# CNN 모델을 순서대로 구성합니다.
model = keras.Sequential([
    # 16x16 흑백 이미지 한 장의 shape를 지정합니다.
    keras.layers.Input(shape=(16, 16, 1)),

    # 16개의 3x3 필터로 지역 특징을 추출합니다.
    keras.layers.Conv2D(
        16,
        kernel_size=3,
        padding="same",
        activation="relu",
    ),

    # 높이와 너비를 절반 정도로 줄입니다.
    keras.layers.MaxPooling2D(pool_size=2),

    # 더 많은 32개 필터로 복합 특징을 추출합니다.
    keras.layers.Conv2D(
        32,
        kernel_size=3,
        padding="same",
        activation="relu",
    ),

    # 다시 공간 크기를 줄입니다.
    keras.layers.MaxPooling2D(pool_size=2),

    # 다차원 Feature Map을 1차원 벡터로 펼칩니다.
    keras.layers.Flatten(),

    # 분류를 위한 Dense 은닉층을 추가합니다.
    keras.layers.Dense(32, activation="relu"),

    # 과적합 완화를 위해 Dropout을 적용합니다.
    keras.layers.Dropout(0.3),

    # 이진 분류 출력층을 구성합니다.
    keras.layers.Dense(1, activation="sigmoid"),
])

# 층별 출력 shape와 파라미터 수를 확인합니다.
model.summary()

# 학습 방법을 설정합니다.
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.001),
    loss="binary_crossentropy",
    metrics=["accuracy"],
)

# 검증 손실이 개선되지 않으면 학습을 조기에 종료합니다.
early_stopping = keras.callbacks.EarlyStopping(
    monitor="val_loss",
    patience=8,
    restore_best_weights=True,
)

# 모델을 학습합니다.
history = model.fit(
    X_train,
    y_train,
    epochs=100,
    batch_size=32,
    validation_split=0.2,
    callbacks=[early_stopping],
    verbose=0,
)

# 실제 수행 Epoch 수를 출력합니다.
print("\n[실제 수행 Epoch]")
print(len(history.history["loss"]))

# 테스트 데이터의 클래스 확률을 예측합니다.
prob = model.predict(X_test, verbose=0).ravel()

# 0.5를 기준으로 0 또는 1로 분류합니다.
pred = (prob >= 0.5).astype(int)

# 테스트 정확도를 계산합니다.
acc = accuracy_score(y_test, pred)

# 정확도를 출력합니다.
print("\n[테스트 정확도]")
print(round(acc, 4))

# 학습/검증 Loss를 시각화합니다.
plt.figure(figsize=(8, 4))
plt.plot(history.history["loss"], label="train loss")
plt.plot(history.history["val_loss"], label="validation loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("CNN 학습곡선 - Loss")
plt.legend()
plt.tight_layout()
plt.savefig(RESULT_DIR / "02_loss_curve.png", dpi=150)
plt.show()

# 학습/검증 Accuracy를 시각화합니다.
plt.figure(figsize=(8, 4))
plt.plot(history.history["accuracy"], label="train accuracy")
plt.plot(history.history["val_accuracy"], label="validation accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.title("CNN 학습곡선 - Accuracy")
plt.legend()
plt.tight_layout()
plt.savefig(RESULT_DIR / "03_accuracy_curve.png", dpi=150)
plt.show()

# 혼동행렬을 출력합니다.
ConfusionMatrixDisplay.from_predictions(y_test, pred)
plt.title("CNN Confusion Matrix")
plt.tight_layout()
plt.savefig(RESULT_DIR / "04_confusion_matrix.png", dpi=150)
plt.show()
