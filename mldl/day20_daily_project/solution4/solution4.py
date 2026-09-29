# solution4.py
# 20일차 머신러닝 미니프로젝트 강사용 풀이
# 주제: 자전거 대여량 예측

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

# 전처리와 모델을 연결하기 위해 make_pipeline을 가져옵니다.
from sklearn.pipeline import make_pipeline

# 회귀 모델들을 가져옵니다.
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# 회귀 모델을 평가하기 위한 지표를 가져옵니다.
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Windows에서는 맑은 고딕을 사용해 그래프의 한글이 깨지지 않게 합니다.
if platform.system() == "Windows":
    plt.rcParams["font.family"] = "Malgun Gothic"

# 그래프에서 마이너스 기호가 깨지지 않게 설정합니다.
plt.rcParams["axes.unicode_minus"] = False

# 현재 파이썬 파일이 있는 폴더를 기준 폴더로 지정합니다.
BASE_DIR = Path(__file__).resolve().parent

# 분석할 CSV 파일의 경로를 지정합니다.
DATA_FILE = BASE_DIR / "team4_data.csv"

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
X = df.drop(columns=["대여량"])

# 예측해야 할 정답 컬럼을 y로 사용합니다.
y = df["대여량"]

# 학습 데이터와 테스트 데이터를 75:25 비율로 분리합니다.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
)

# 비교할 세 개의 회귀 모델을 딕셔너리로 준비합니다.
models = {
    # 선형회귀는 결측치를 중앙값으로 채운 뒤 학습합니다.
    "LinearRegression": make_pipeline(
        SimpleImputer(strategy="median"),
        LinearRegression(),
    ),
    # 의사결정트리 회귀 모델을 준비합니다.
    "DecisionTree": make_pipeline(
        SimpleImputer(strategy="median"),
        DecisionTreeRegressor(
            max_depth=7,
            random_state=42,
        ),
    ),
    # 랜덤포레스트 회귀 모델을 준비합니다.
    "RandomForest": make_pipeline(
        SimpleImputer(strategy="median"),
        RandomForestRegressor(
            n_estimators=200,
            max_depth=10,
            random_state=42,
            n_jobs=-1,
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

    # 나중에 그래프를 그릴 수 있도록 예측값을 저장합니다.
    predictions[name] = pred

    # 평균 절대 오차 MAE를 계산합니다.
    mae = mean_absolute_error(y_test, pred)

    # 평균 제곱근 오차 RMSE를 계산합니다.
    rmse = mean_squared_error(y_test, pred) ** 0.5

    # 결정계수 R²를 계산합니다.
    r2 = r2_score(y_test, pred)

    # 한 모델의 평가 결과를 리스트에 추가합니다.
    results.append([name, mae, rmse, r2])

# 평가 결과를 DataFrame으로 변환합니다.
result_df = pd.DataFrame(
    results,
    columns=["모델", "MAE", "RMSE", "R2"],
)

# R²가 높은 순서로 정렬합니다.
result_df = result_df.sort_values("R2", ascending=False).reset_index(drop=True)

# 모델 비교 결과를 출력합니다.
print("\n[모델 성능 비교]")
print(result_df.round(4))

# 모델 비교표를 CSV 파일로 저장합니다.
result_df.to_csv(
    RESULT_DIR / "model_results.csv",
    index=False,
    encoding="utf-8-sig",
)

# R²가 가장 높은 모델 이름을 최종 모델 이름으로 선택합니다.
best_name = result_df.loc[0, "모델"]

# 최종 모델의 예측값을 가져옵니다.
best_pred = predictions[best_name]

# 타깃 값의 분포를 히스토그램으로 그립니다.
plt.figure(figsize=(7, 4))
plt.hist(y, bins=25, edgecolor="black")
plt.title("자전거 대여량 예측 - Target 분포")
plt.xlabel("대여량")
plt.ylabel("빈도")
plt.tight_layout()
plt.savefig(RESULT_DIR / "01_target_distribution.png", dpi=150)
plt.show()

# 모델별 MAE를 막대그래프로 그립니다.
plt.figure(figsize=(8, 4))
plt.bar(result_df["모델"], result_df["MAE"])
plt.title("모델별 MAE 비교")
plt.xlabel("모델")
plt.ylabel("MAE")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig(RESULT_DIR / "02_model_mae.png", dpi=150)
plt.show()

# 실제값과 최종 모델의 예측값을 산점도로 그립니다.
plt.figure(figsize=(6, 6))
plt.scatter(y_test, best_pred, alpha=0.65)

# 실제값과 예측값이 완전히 같은 위치를 나타내는 기준선을 그립니다.
min_value = min(y_test.min(), best_pred.min())
max_value = max(y_test.max(), best_pred.max())
plt.plot(
    [min_value, max_value],
    [min_value, max_value],
    linestyle="--",
)

# 실제값과 예측값 그래프의 제목과 축 이름을 지정합니다.
plt.title(f"실제값 vs 예측값 - {best_name}")
plt.xlabel("실제값")
plt.ylabel("예측값")
plt.tight_layout()
plt.savefig(RESULT_DIR / "03_actual_vs_prediction.png", dpi=150)
plt.show()

# 랜덤포레스트 파이프라인에서 실제 RandomForestRegressor 모델을 꺼냅니다.
rf_model = models["RandomForest"].named_steps["randomforestregressor"]

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

# 최종 모델과 주요 평가 결과를 출력합니다.
print("\n[최종 모델]")
print(best_name)

# 최종 모델의 R²를 출력합니다.
print("최종 모델 R²:", round(result_df.loc[0, "R2"], 4))

# 랜덤포레스트 기준 중요도가 높은 특성 3개를 출력합니다.
print("\n[RandomForest 중요 특성 TOP 3]")
print(importance.sort_values(ascending=False).head(3))

# 결과 파일이 저장된 위치를 출력합니다.
print("\n결과 저장 폴더:", RESULT_DIR)
