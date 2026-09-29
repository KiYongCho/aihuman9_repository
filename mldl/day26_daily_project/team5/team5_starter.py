# team5_starter.py
# 다음 시점 전력수요 예측 - SimpleRNN vs LSTM 회귀 미니프로젝트

# 파일 경로를 처리하기 위해 Path를 가져옵니다.
from pathlib import Path

# 배열 처리를 위해 NumPy를 가져옵니다.
import numpy as np

# 그래프를 그리기 위해 matplotlib을 가져옵니다.
import matplotlib.pyplot as plt

# 특성 스케일링을 위해 StandardScaler를 가져옵니다.
from sklearn.preprocessing import StandardScaler

# 회귀 평가 지표를 가져옵니다.
from sklearn.metrics import mean_absolute_error, mean_squared_error

# TensorFlow Keras를 가져옵니다.
from tensorflow import keras

# 난수 시드를 고정합니다.
keras.utils.set_random_seed(42)

# NPZ 데이터 경로를 지정합니다.
DATA_FILE = Path(__file__).resolve().parent / "team5_data.npz"

# 데이터를 읽습니다.
data = np.load(DATA_FILE)

# 입력 시퀀스를 가져옵니다.
X = data["X"]

# 다음 시점의 전력수요 정답을 가져옵니다.
y = data["y"]

# TODO 1. X.shape와 y.shape를 출력하세요.

# TODO 2. X의 (24, 2)가 의미하는 내용을 설명하세요.

# TODO 3. 시간 순서를 유지하여 앞 80%를 학습, 뒤 20%를 테스트로 나누세요.

# TODO 4. Training Set을 기준으로 특성 스케일을 조정하세요.

# TODO 5. SimpleRNN(32) 회귀 모델을 만드세요.

# TODO 6. LSTM(32) 회귀 모델을 만드세요.

# TODO 7. 두 모델 모두 Dense(1), Adam, mse를 사용하세요.

# TODO 8. 동일한 EarlyStopping 설정으로 두 모델을 학습하세요.

# TODO 9. MAE, RMSE, 실제 Epoch 수를 비교하세요.

# TODO 10. 테스트 구간의 실제값과 예측값을 선그래프로 표시하세요.
