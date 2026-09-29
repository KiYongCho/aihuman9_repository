# team3_starter.py
# 제품 표면 패턴 판별 - CNN 이진 분류 미니프로젝트

# 파일 경로 처리를 위해 Path를 가져옵니다.
from pathlib import Path

# 수치 배열 처리를 위해 NumPy를 가져옵니다.
import numpy as np

# 그래프 출력을 위해 matplotlib을 가져옵니다.
import matplotlib.pyplot as plt

# 데이터 분리를 위해 함수를 가져옵니다.
from sklearn.model_selection import train_test_split

# 혼동행렬 출력을 위해 도구를 가져옵니다.
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay

# TensorFlow Keras를 가져옵니다.
from tensorflow import keras

# 난수 시드를 고정합니다.
keras.utils.set_random_seed(42)

# NPZ 데이터 파일 경로를 지정합니다.
DATA_FILE = Path(__file__).resolve().parent / "team3_data.npz"

# NPZ 파일을 읽습니다.
data = np.load(DATA_FILE)

# 입력 이미지 배열을 가져옵니다.
X = data["X"]

# 정답 배열을 가져옵니다.
y = data["y"]

# TODO 1. X.shape와 y.shape를 출력하고 각 축의 의미를 적으세요.

# TODO 2. 샘플 이미지 8장을 시각화하세요.

# TODO 3. Train/Test 데이터를 75:25로 분리하세요.
# stratify=y, random_state=42를 사용하세요.

# TODO 4. CNN 모델을 구성하세요.
# Input(16,16,1)
# Conv2D(16, 3, padding="same", relu)
# MaxPooling2D(2)
# Conv2D(32, 3, padding="same", relu)
# MaxPooling2D(2)
# Flatten
# Dense(32, relu)
# Dropout(0.3)
# Dense(1, sigmoid)

# TODO 5. model.summary()로 shape 흐름을 확인하세요.

# TODO 6. Adam + binary_crossentropy + accuracy로 compile하세요.

# TODO 7. EarlyStopping을 적용하여 학습하세요.

# TODO 8. train/validation loss와 accuracy를 시각화하세요.

# TODO 9. 테스트 정확도를 계산하세요.

# TODO 10. 혼동행렬을 출력하세요.
