# team1_starter.py
# 회원 재방문 예측 - Dense 이진 분류 미니프로젝트

# 파일 경로를 처리하기 위해 Path를 가져옵니다.
from pathlib import Path

# 데이터 처리를 위해 pandas를 가져옵니다.
import pandas as pd

# 수치 계산을 위해 NumPy를 가져옵니다.
import numpy as np

# 그래프 출력을 위해 matplotlib을 가져옵니다.
import matplotlib.pyplot as plt

# 학습/테스트 데이터 분리를 위해 함수를 가져옵니다.
from sklearn.model_selection import train_test_split

# 입력값의 크기를 맞추기 위해 StandardScaler를 가져옵니다.
from sklearn.preprocessing import StandardScaler

# 최종 분류 성능을 확인하기 위해 평가 함수를 가져옵니다.
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay

# TensorFlow Keras를 가져옵니다.
from tensorflow import keras

# 재현 가능한 결과를 위해 난수 시드를 고정합니다.
keras.utils.set_random_seed(42)

# 현재 파일과 같은 폴더의 CSV 파일 경로를 지정합니다.
DATA_FILE = Path(__file__).resolve().parent / "team1_data.csv"

# CSV 파일을 읽습니다.
df = pd.read_csv(DATA_FILE, encoding="utf-8-sig")

# TODO 1. 데이터의 shape, 자료형, 결측치 개수를 확인하세요.

# TODO 2. 숫자형 컬럼의 결측치를 중앙값으로 처리하세요.

# TODO 3. X와 y를 분리하세요.
# Target: 재방문여부

# TODO 4. train_test_split()으로 75:25로 분리하세요.
# random_state=42, stratify=y를 사용하세요.

# TODO 5. StandardScaler를 Training Set에 fit한 뒤 Train/Test를 변환하세요.

# TODO 6. Dropout이 없는 기본 Dense 모델을 구성하세요.
# 예: Input → Dense(32, relu) → Dense(16, relu) → Dense(1, sigmoid)

# TODO 7. Dropout(0.3)이 포함된 두 번째 Dense 모델을 구성하세요.

# TODO 8. 두 모델을 Adam + binary_crossentropy + accuracy로 compile하세요.

# TODO 9. EarlyStopping을 생성하세요.
# monitor="val_loss", patience=10, restore_best_weights=True

# TODO 10. 두 모델을 학습하고 History를 저장하세요.

# TODO 11. 두 모델의 validation loss를 한 그래프에 비교하세요.

# TODO 12. 테스트 정확도를 비교하세요.

# TODO 13. 최종 모델의 혼동행렬을 출력하세요.
