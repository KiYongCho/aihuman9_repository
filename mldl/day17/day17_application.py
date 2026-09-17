# day17_application.py

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from include.graph_config import set_graph
from util.print_util import pp, pt, up

set_graph(10, 8, 13)

df = pd.DataFrame({
    "광고비": [80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380],
    "매출": [1050, 1120, 1220, 1280, 1380, 1490, 1580, 1660, 1770, 1850, 1960, 2070, 2160, 2260, 2370, 2460]
})

X = df[["광고비"]]
y = df["매출"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

# 선형회귀 모델 객체를 생성합니다
model = LinearRegression()

# 학습 데이터를 사용해 선형회귀 모델의 계수와 절편을 학습
model.fit(X_train, y_train)

# 학습된 모델로 입력 데이터의 목표값을 예측
pred = model.predict(X_test)

# 실제값과 예측값을 비교하기 위한 결과 DataFrame을 생성
result = pd.DataFrame({
    "광고비": X_test["광고비"],
    "실제매출": y_test,
    "예측매출": pred
}).sort_values("광고비")

# 실제값과 예측값의 차이를 이용해 오차 컬럼을 추가
result["절대오차"] = (result["실제매출"] - result["예측매출"]).abs()
pp(result.round(2))

# 평균적으로 매출 예측이 실제값에서 얼마나 벗어나는지 만원 단위로 표현
mae = mean_absolute_error(y_test, pred)
pp(f"MAE: {mae:.2f}만원")

# 실제값 변동을 모델이 얼마나 설명하는지 결정계수 R²를 계산
r2 = r2_score(y_test, pred)
pp(f"R2: {r2:.3f}")

# 새로운 광고비 입력값을 DataFrame 형태로 생성
new_ad = pd.DataFrame({"광고비": [400]})

# 새로운 입력값을 예측하고 첫 번째 예측값을 하나의 값으로 추출
new_sales = model.predict(new_ad)[0]

# 새로운 입력값에 대한 예측 결과를 출력
pp(f"광고비 400만원일 때 예상 매출: {new_sales:.0f}만원")

# 회귀선을 그리기 위한 x축 입력값을 DataFrame 형태로 생성
line_x = pd.DataFrame({"광고비": sorted(df["광고비"].tolist())})

# 학습된 모델로 입력 데이터의 목표값을 예측
line_y = model.predict(line_x)

plt.scatter(df["광고비"], df["매출"], label="실제 데이터")
plt.plot(line_x["광고비"], line_y, label="회귀선")
plt.title("광고비에 따른 매출 예측")
plt.xlabel("광고비(만원)")
plt.ylabel("매출(만원)")
plt.legend()
plt.tight_layout()
plt.show()

up(5)

