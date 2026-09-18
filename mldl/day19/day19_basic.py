# day19_basic.py

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from util.print_util import pp, pt, up
from include.graph_config import set_graph

set_graph(10, 8, 13)

# 임의 데이터 생성
rng = np.random.default_rng(42) # 난수 생성기
size = 300 # 난수 개수
df = pd.DataFrame({
    "temperature": rng.uniform(60, 100, size), # 60~100 사이 값을 균등하게 300개 생성
    "pressure": rng.uniform(80, 140, size),
    "speed": rng.uniform(20, 80, size),
    "moisture": rng.uniform(2, 12, size)
})

# 세 품질 조건을 모두 만족하면 합격 1, 아니면 불합격 0으로 생성
quality_condition = (
    (df['temperature'].between(70, 90))
    & (df['pressure'].between(95, 125))
    & (df['moisture'] < 9)
)

df['quality'] = quality_condition.astype(int) # 정수로 변환

X = df.drop(columns='quality') # Feature
y = df['quality'] # Target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# 결정트리 모델 생성
model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)

# 학습
model.fit(X_train, y_train)

train_acc = model.score(X_train, y_train) # train 정확도
test_acc = model.score(X_test, y_test) # test 정확도

importance_df = pd.DataFrame({
    "feature": X.columns,
    "importance": model.feature_importances_,
}).sort_values(by='importance', ascending=False).reset_index(drop=True)

pp('[데이터 일부]')
pp(df.head())

pp(f'학습 정확도: {train_acc:.4f}')
pp(f'테스트 정확도: {test_acc:.4f}')

pp('[특성 중요도]')
pp(importance_df)

pp(f'가장 중요한 특성: {importance_df.loc[0, "feature"]}')

up(5)























