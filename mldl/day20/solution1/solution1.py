# solution1.py
# 20일차 머신러닝 미니프로젝트 강사용 풀이
# 주제: 고객 이탈 예측

# 파일 경로를 안전하게 처리하기 위해 Path를 가져옵니다.
from pathlib import Path

# 운영체제에 따라 한글 폰트를 설정하기 위해 platform을 가져옵니다.
import platform

# 표 형태의 데이터를 처리하기 위해 pandas를 가져옵니다.
import pandas as pd

# 그래프를 그리기 위해 matplotlib을 가져옵니다.
import matplotlib.pyplot as plt

# 학습용/테스트용 데이터를 나누기 위해 train_test_split을 가져옵니다.
from sklearn.model_selection import train_test_split

# 결측치를 중앙값으로 채우기 위해 SimpleImputer를 가져옵니다.
from sklearn.impute import SimpleImputer

# 서로 단위가 다른 특성을 표준화하기 위해 StandardScaler를 가져옵니다.
from sklearn.preprocessing import StandardScaler

# 전처리와 모델을 하나의 흐름으로 연결하기 위해 make_pipeline을 가져옵니다.
from sklearn.pipeline import make_pipeline

# 분류 모델들을 가져옵니다.
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# 분류 모델을 평가하기 위한 지표와 혼동행렬 도구를 가져옵니다.
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    ConfusionMatrixDisplay,
)

# Windows에서는 맑은 고딕을 사용해 그래프의 한글이 깨지지 않게 합니다.
if platform.system() == "Windows":
    plt.rcParams["font.family"] = "Malgun Gothic"

# 그래프에서 마이너스 기호가 깨지지 않게 설정합니다.
plt.rcParams["axes.unicode_minus"] = False

# 현재 파이썬 파일이 있는 폴더를 기준 폴더로 지정합니다.
BASE_DIR = Path(__file__).resolve().parent

# 분석할 CSV 파일의 경로를 지정합니다.
DATA_FILE = BASE_DIR / "team1_data.csv"

# 그래프와 결과 파일을 저장할 폴더를 지정합니다.
RESULT_DIR = BASE_DIR / "result"

# result 폴더가 없으면 새로 만듭니다.
RESULT_DIR.mkdir(exist_ok=True)

# CSV 파일을 DataFrame으로 읽습니다.
df = pd.read_csv(DATA_FILE, encoding="utf-8-sig")

# 데이터 앞부분을 출력합니다.
print("\n[데이터 미리보기]")
print(df.head())

# 데이터의 행과 열 개수를 출력합니다.
print("\n[데이터 크기]")
print(df.shape)

# 각 컬럼의 자료형을 출력합니다.
print("\n[자료형]")
print(df.dtypes)

# 각 컬럼의 결측치 개수를 출력합니다.
print("\n[결측치 개수]")
print(df.isna().sum())

# 숫자형 데이터의 기초 통계량을 출력합니다.
print("\n[기초 통계량]")
print(df.describe())

# 정답 컬럼을 제외한 나머지 컬럼을 입력 특성 X로 사용합니다.
X = df.drop(columns=["이탈여부"])

# 예측해야 할 정답 컬럼을 y로 사용합니다.
y = df["이탈여부"]

# 학습 데이터와 테스트 데이터를 75:25 비율로 분리합니다.
# stratify=y를 사용하면 0과 1의 비율을 학습/테스트 데이터에 비슷하게 유지할 수 있습니다.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y,
)

# 비교할 네 개의 분류 모델을 딕셔너리로 준비합니다.
models = {
    # 로지스틱 회귀는 결측치 처리 후 표준화를 적용합니다.
    "LogisticRegression": make_pipeline(
        SimpleImputer(strategy="median"),
        StandardScaler(),
        LogisticRegression(max_iter=2000),
    ),
    # KNN은 거리 기반 알고리즘이므로 표준화의 영향을 많이 받습니다.
    "KNN": make_pipeline(
        SimpleImputer(strategy="median"),
        StandardScaler(),
        KNeighborsClassifier(n_neighbors=7),
    ),
    # 의사결정트리는 스케일링이 필수는 아니므로 결측치만 먼저 처리합니다.
    "DecisionTree": make_pipeline(
        SimpleImputer(strategy="median"),
        DecisionTreeClassifier(max_depth=5, random_state=42),
    ),
    # 랜덤포레스트도 결측치 처리 후 학습합니다.
    "RandomForest": make_pipeline(
        SimpleImputer(strategy="median"),
        RandomForestClassifier(
            n_estimators=200,
            max_depth=7,
            random_state=42,
        ),
    ),
}

# 각 모델의 평가 결과를 저장할 리스트를 만듭니다.
results = []

# 각 모델의 예측값을 저장할 딕셔너리를 만듭니다.
predictions = {}

# 준비한 모델을 하나씩 반복합니다.
for name, model in models.items():
    # 학습 데이터로 모델을 학습합니다.
    model.fit(X_train, y_train)

    # 테스트 데이터의 정답을 예측합니다.
    pred = model.predict(X_test)

    # 나중에 혼동행렬을 그릴 수 있도록 예측값을 저장합니다.
    predictions[name] = pred

    # 정확도를 계산합니다.
    accuracy = accuracy_score(y_test, pred)

    # 정밀도를 계산합니다.
    precision = precision_score(y_test, pred, zero_division=0)

    # 재현율을 계산합니다.
    recall = recall_score(y_test, pred, zero_division=0)

    # F1-score를 계산합니다.
    f1 = f1_score(y_test, pred, zero_division=0)

    # 한 모델의 평가 결과를 리스트에 추가합니다.
    results.append([name, accuracy, precision, recall, f1])

# 평가 결과를 DataFrame으로 변환합니다.
result_df = pd.DataFrame(
    results,
    columns=["모델", "Accuracy", "Precision", "Recall", "F1"],
)

# F1-score가 높은 순서로 정렬합니다.
result_df = result_df.sort_values("F1", ascending=False).reset_index(drop=True)

# 모델 비교 결과를 출력합니다.
print("\n[모델 성능 비교]")
print(result_df.round(4))

# 모델 비교표를 CSV 파일로 저장합니다.
result_df.to_csv(
    RESULT_DIR / "model_results.csv",
    index=False,
    encoding="utf-8-sig",
)

# F1-score가 가장 높은 모델 이름을 최종 모델 이름으로 선택합니다.
best_name = result_df.loc[0, "모델"]

# 최종 모델 객체를 가져옵니다.
best_model = models[best_name]

# 최종 모델의 예측값을 가져옵니다.
best_pred = predictions[best_name]

# 타깃 클래스의 개수를 계산합니다.
target_counts = y.value_counts().sort_index()

# 타깃 클래스 분포를 막대그래프로 그립니다.
plt.figure(figsize=(6, 4))
plt.bar(target_counts.index.astype(str), target_counts.values)
plt.title("고객 이탈 예측 - Target 분포")
plt.xlabel("이탈여부")
plt.ylabel("건수")
plt.tight_layout()
plt.savefig(RESULT_DIR / "01_target_distribution.png", dpi=150)
plt.show()

# 모델별 F1-score를 막대그래프로 그립니다.
plt.figure(figsize=(8, 4))
plt.bar(result_df["모델"], result_df["F1"])
plt.ylim(0, 1)
plt.title("모델별 F1-score 비교")
plt.xlabel("모델")
plt.ylabel("F1-score")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig(RESULT_DIR / "02_model_f1.png", dpi=150)
plt.show()

# 최종 모델의 혼동행렬을 그립니다.
ConfusionMatrixDisplay.from_predictions(
    y_test,
    best_pred,
    cmap="Blues",
)
plt.title(f"혼동행렬 - {best_name}")
plt.tight_layout()
plt.savefig(RESULT_DIR / "03_confusion_matrix.png", dpi=150)
plt.show()

# 랜덤포레스트 파이프라인에서 실제 RandomForest 모델을 꺼냅니다.
rf_model = models["RandomForest"].named_steps["randomforestclassifier"]

# 랜덤포레스트의 특성 중요도를 Series로 만듭니다.
importance = pd.Series(
    rf_model.feature_importances_,
    index=X.columns,
).sort_values(ascending=True)

# 특성 중요도를 가로 막대그래프로 그립니다.
plt.figure(figsize=(8, 5))
plt.barh(importance.index, importance.values)
plt.title("RandomForest 특성 중요도")
plt.xlabel("중요도")
plt.tight_layout()
plt.savefig(RESULT_DIR / "04_feature_importance.png", dpi=150)
plt.show()

# 최종 모델과 결과를 요약해서 출력합니다.
print("\n[최종 모델]")
print(best_name)

# 최종 모델의 F1-score를 출력합니다.
print("최종 모델 F1-score:", round(result_df.loc[0, "F1"], 4))

# 랜덤포레스트 기준 중요도가 높은 특성 3개를 출력합니다.
print("\n[RandomForest 중요 특성 TOP 3]")
print(importance.sort_values(ascending=False).head(3))

# 결과 파일이 저장된 위치를 출력합니다.
print("\n결과 저장 폴더:", RESULT_DIR)
