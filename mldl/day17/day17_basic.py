# day17_basic.py

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from include.graph_config import set_graph
from util.print_util import pp, pt, up

set_graph(10, 8, 13)

df = pd.DataFrame({
    "공부시간": [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5],
    "평가점수": [48, 52, 55, 60, 63, 68, 72, 75, 80, 83, 87, 91]
})

X = df[["공부시간"]]
y = df["평가점수"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

# 선형회귀 모델 객체를 생성
model = LinearRegression()

# 학습 데이터를 사용해 선형회귀 모델의 계수와 절편을 학습
model.fit(X_train, y_train)

# 학습된 모델로 입력 데이터의 목표값을 예측
pred = model.predict(X_test)

# 실제값과 예측값을 비교하기 위한 결과 DataFrame
result = pd.DataFrame({
    "공부시간": X_test["공부시간"],
    "실제점수": y_test,
    "예측점수": pred
}).sort_values("공부시간")
pp(result.round(2))

# 학습에 사용한 컬럼명과 동일하게 구성
new_data = pd.DataFrame({"공부시간": [7.0]})

# 새로운 입력값을 예측하고 첫 번째 예측값을 하나의 값으로 추출
pred_score = model.predict(new_data)[0]

# 결정계수 R² 값을 출력해 모델의 설명력을 확인
pp(f"7시간 공부 시 예상 평가점수: {pred_score:.1f}점")

# 회귀선을 그리기 위한 x축 입력값을 DataFrame 형태로 생성
line_x = pd.DataFrame({"공부시간": sorted(df["공부시간"].tolist())})

# 학습된 모델로 입력 데이터의 목표값을 예측
line_y = model.predict(line_x)

plt.scatter(df["공부시간"], df["평가점수"], label="실제 데이터")
plt.plot(line_x["공부시간"], line_y, label="회귀선")
plt.title("공부시간에 따른 평가점수 예측")
plt.xlabel("공부시간")
plt.ylabel("평가점수")
plt.legend()
plt.tight_layout()
plt.show()

up(5)
