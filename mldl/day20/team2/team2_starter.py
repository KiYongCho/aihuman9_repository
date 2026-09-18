# team2_starter.py
# 20일차 머신러닝 미니프로젝트 - 제조설비 고장 예측
# 아래 TODO 부분을 팀원과 함께 완성하세요.

from pathlib import Path
import platform

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import ConfusionMatrixDisplay

# Windows에서 matplotlib 그래프의 한글을 표시합니다.
if platform.system() == "Windows":
    plt.rcParams["font.family"] = "Malgun Gothic"

# 마이너스 기호가 깨지는 현상을 방지합니다.
plt.rcParams["axes.unicode_minus"] = False

# 현재 파이썬 파일과 같은 폴더에 있는 CSV 파일 경로를 만듭니다.
DATA_FILE = Path(__file__).resolve().parent / "team2_data.csv"

# CSV 데이터를 DataFrame으로 읽습니다.
df = pd.read_csv(DATA_FILE, encoding="utf-8-sig")

# 데이터 일부를 확인합니다.
print(df.head())

# TODO 1. 데이터의 행/열 개수, 컬럼명, 자료형을 확인합니다.

# TODO 2. 각 컬럼의 결측치 개수를 확인합니다.

# TODO 3. 결측치를 처리합니다.
# 힌트: 숫자형 컬럼은 중앙값(median)을 사용해도 좋습니다.

# TODO 4. 입력 데이터 X와 정답 y를 정의합니다.
# Target 컬럼: 고장여부

# TODO 5. 학습/테스트 데이터를 분리합니다.
# 힌트: test_size=0.25, random_state=42, stratify=y

# TODO 6. 최소 3개 이상의 분류 모델을 생성합니다.
# 예: LogisticRegression, KNN, DecisionTreeClassifier, RandomForestClassifier

# TODO 7. 각 모델을 학습하고 예측값을 만듭니다.

# TODO 8. Accuracy, Precision, Recall, F1-score를 계산하여 비교합니다.

# TODO 9. 최종 모델의 혼동행렬을 시각화합니다.

# TODO 10. RandomForest를 사용했다면 feature_importances_를 시각화합니다.

# TODO 11. 모델별 성능을 표 형태의 DataFrame으로 정리합니다.

# TODO 12. 모델 성능 비교 그래프를 작성합니다.

# TODO 13. 최종 모델과 선택 이유를 5줄 이상으로 정리합니다.
