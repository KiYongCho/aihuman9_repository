# day17_challenge.py

# day17_challenge.py

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from include.graph_config import set_graph
from util.print_util import pp, pt, up

set_graph(10, 8, 13)

df = pd.DataFrame({
    "면적": [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140],
    "역거리": [18, 15, 14, 16, 12, 13, 10, 11, 9, 8, 10, 7, 6, 8, 5, 6, 4, 5, 3, 4],
    "준공연수": [24, 20, 18, 22, 15, 17, 14, 12, 13, 10, 11, 9, 8, 10, 7, 6, 5, 7, 4, 3],
    "가격": [33300, 37000, 41200, 40300, 46650, 46950, 52100, 53100, 56450, 60000, 59650, 64550, 66800, 68200, 71250, 73900, 76450, 78250, 81300, 83550]
})

y = df["가격"]

# 단순회귀에 사용할 독립변수
X_simple = df[["면적"]]

Xs_train, Xs_test, ys_train, ys_test = train_test_split(
    X_simple,
    y,
    test_size=0.25,
    random_state=42
)

# 선형회귀 모델 객체를 생성
simple_model = LinearRegression()

# 학습 데이터를 사용해 선형회귀 모델의 계수와 절편을 학습
simple_model.fit(Xs_train, ys_train)

# 학습된 모델로 입력 데이터의 목표값을 예측
simple_pred = simple_model.predict(Xs_test)

# 실제값과 예측값의 평균절대오차 MAE를 계산
simple_mae = mean_absolute_error(ys_test, simple_pred)

# 실제값 변동을 모델이 얼마나 설명하는지 결정계수 R²를 계산
simple_r2 = r2_score(ys_test, simple_pred)

# 다중회귀에 사용할 특성 컬럼 목록
features = ["면적", "역거리", "준공연수"]

# 여러 특성을 포함한 다중회귀용 독립변수 데이터
X_multi = df[features]

Xm_train, Xm_test, ym_train, ym_test = train_test_split(
    X_multi,
    y,
    test_size=0.25,
    random_state=42
)

# 선형회귀 모델 객체를 생성
multi_model = LinearRegression()

# 학습 데이터를 사용해 선형회귀 모델의 계수와 절편을 학습
multi_model.fit(Xm_train, ym_train)

# 학습된 모델로 입력 데이터의 목표값을 예측
multi_pred = multi_model.predict(Xm_test)

# 실제값과 예측값의 평균절대오차 MAE를 계산
multi_mae = mean_absolute_error(ym_test, multi_pred)

# 실제값 변동을 모델이 얼마나 설명하는지 결정계수 R²를 계산
multi_r2 = r2_score(ym_test, multi_pred)

comparison = pd.DataFrame({
    "모델": ["면적 단순회귀", "3특성 다중회귀"],
    "MAE": [simple_mae, multi_mae],
    "R2": [simple_r2, multi_r2]
})
pp("[모델 성능 비교]")
pp(comparison.round(3))

# 특성별 회귀계수를 확인하기 위한 DataFrame을 생성
coef_df = pd.DataFrame({
    "특성": features,
    "회귀계수": multi_model.coef_
})

# 특성마다 측정 단위와 값의 범위가 다르므로 회귀계수 절댓값만으로 중요도를 직접 비교하면 안됨

pp("[다중회귀 회귀계수]")
pp(coef_df.round(2))

new_house = pd.DataFrame({
    "면적": [100],
    "역거리": [5],
    "준공연수": [6]
})

# 새로운 입력값을 예측하고 첫 번째 예측값을 하나의 값으로 추출
new_price = multi_model.predict(new_house)[0]

# 새로운 입력값에 대한 예측 결과를 출력
pp(f"조건에 맞는 주택의 예상 가격: {new_price:.0f}만원")

# 회귀선을 그리기 위한 x축 입력값을 DataFrame 형태로 생성
line_x = pd.DataFrame({"면적": sorted(df["면적"].tolist())})

# 학습된 모델로 입력 데이터의 목표값을 예측
line_y = simple_model.predict(line_x)

plt.scatter(df["면적"], df["가격"], label="실제 데이터")
plt.plot(line_x["면적"], line_y, label="단순회귀선")
plt.title("주택 면적과 가격의 단순 선형회귀")
plt.xlabel("면적(㎡)")
plt.ylabel("가격(만원)")
plt.legend()
plt.tight_layout()
plt.show()

# 두 모델의 MAE와 R²를 함께 비교해 더 적절한 모델인지 판단
if multi_mae < simple_mae and multi_r2 > simple_r2:
    pp("테스트 데이터 기준으로 다중회귀가 MAE는 더 낮고 R2는 더 높아 더 적절합니다.")
elif simple_mae < multi_mae and simple_r2 > multi_r2: # 반대 조건에서 단순회귀 모델이 더 적절한지 확인
    pp("테스트 데이터 기준으로 단순회귀가 MAE는 더 낮고 R2는 더 높아 더 적절합니다.")
else: # 두 평가 지표가 같은 방향으로 결론나지 않는 경우
    pp("MAE와 R2가 서로 다른 방향을 보이므로 한 지표만으로 모델을 선택하지 말고 추가 검증이 필요합니다.")

up(5)

