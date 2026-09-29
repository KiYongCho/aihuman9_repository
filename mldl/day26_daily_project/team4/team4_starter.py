# team4_starter.py
# 센서 이상 징후 판별 - SimpleRNN vs LSTM 미니프로젝트

# 파일 경로를 처리하기 위해 Path를 가져옵니다.
from pathlib import Path

# 배열 처리를 위해 NumPy를 가져옵니다.
import numpy as np

# 그래프를 그리기 위해 matplotlib을 가져옵니다.
import matplotlib.pyplot as plt

# 데이터 분리를 위해 함수를 가져옵니다.
from sklearn.model_selection import train_test_split

# 분류 평가를 위해 함수를 가져옵니다.
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay

# TensorFlow Keras를 가져옵니다.
from tensorflow import keras

# 난수 시드를 고정합니다.
keras.utils.set_random_seed(42)

# NPZ 파일 경로를 지정합니다.
DATA_FILE = Path(__file__).resolve().parent / "team4_data.npz"

# 데이터를 읽습니다.
data = np.load(DATA_FILE)

# 입력 시퀀스를 가져옵니다.
X = data["X"]

# 정답을 가져옵니다.
y = data["y"]

# TODO 1. X.shape와 y.shape를 출력하세요.

# TODO 2. samples, timesteps, features의 의미를 설명하세요.

# TODO 3. Train/Test를 75:25로 분리하세요.
# stratify=y를 사용하세요.

# TODO 4. SimpleRNN(24) 기반 모델을 만드세요.

# TODO 5. LSTM(24) 기반 모델을 만드세요.

# TODO 6. 두 모델 모두 Dense(1, sigmoid)를 출력층으로 사용하세요.

# TODO 7. 두 모델을 같은 Adam, binary_crossentropy, accuracy 조건으로 compile하세요.

# TODO 8. 같은 EarlyStopping 설정으로 학습하세요.

# TODO 9. 두 모델의 count_params(), 실제 Epoch 수, val_loss, val_accuracy를 비교하세요.

# TODO 10. 최종 모델의 혼동행렬을 출력하세요.
