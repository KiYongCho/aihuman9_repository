# team2_starter.py
# 배송 소요시간 예측 - Dense 회귀 미니프로젝트

# 파일 경로를 처리하기 위해 Path를 가져옵니다.
from pathlib import Path

# 데이터 처리를 위해 pandas를 가져옵니다.
import pandas as pd

# 수치 계산을 위해 NumPy를 가져옵니다.
import numpy as np

# 그래프 출력을 위해 matplotlib을 가져옵니다.
import matplotlib.pyplot as plt

# 데이터 분리를 위해 함수를 가져옵니다.
from sklearn.model_selection import train_test_split

# 특성 스케일링을 위해 StandardScaler를 가져옵니다.
from sklearn.preprocessing import StandardScaler

# 회귀 평가를 위해 MAE를 가져옵니다.
from sklearn.metrics import mean_absolute_error, mean_squared_error

# TensorFlow Keras를 가져옵니다.
from tensorflow import keras

# 난수 시드를 고정합니다.
keras.utils.set_random_seed(42)

# CSV 파일 경로를 지정합니다.
DATA_FILE = Path(__file__).resolve().parent / "team2_data.csv"

# CSV 데이터를 읽습니다.
df = pd.read_csv(DATA_FILE, encoding="utf-8-sig")

# TODO 1. 데이터 shape, 자료형, 결측치를 확인하세요.

# TODO 2. 숫자형 결측치를 중앙값으로 처리하세요.

# TODO 3. X와 y를 분리하세요.
# Target: 배송소요시간_분

# TODO 4. Train/Test를 75:25로 나누세요.

# TODO 5. StandardScaler를 Training Set 기준으로 적용하세요.

# TODO 6. Dense 회귀 모델을 생성하는 함수를 작성하세요.
# 예: Input → Dense(32, relu) → Dense(16, relu) → Dense(1)

# TODO 7. optimizer="adam", loss="mse"로 compile하세요.

# TODO 8. batch_size=16 실험을 수행하세요.

# TODO 9. 동일 구조를 다시 만들고 batch_size=64 실험을 수행하세요.

# TODO 10. 두 실험에 같은 EarlyStopping 조건을 사용하세요.

# TODO 11. History의 validation loss를 비교하세요.

# TODO 12. MAE와 RMSE를 계산하세요.

# TODO 13. 실제값과 예측값 산점도를 그리세요.
