# day18_basic.py

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from util.print_util import pp, up

'''
sepal length (cm)    꽃받침 길이
sepal width (cm)     꽃받침 너비
petal length (cm)    꽃잎 길이
petal width (cm)     꽃잎 너비
target               품종
'''

# iris 데이터셋
iris = load_iris(as_frame=True) # as_frame=True : Feature와 Target 데이터프레임으로
df = iris.frame # 데이터프레임
pp(df.head())

# Feature / Target
X = iris.data
y = iris.target

# 학습 / 테스트 분리
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y # 세 품종의 비율을 유지하면서 데이터를 분리
)

# 분류모델
model = LogisticRegression(max_iter=1000) # 최대 최적화 반복회수 1000

# 학습
model.fit(X_train, y_train)

# 예측
pred = model.predict(X_test)

# 정확도
acc = accuracy_score(y_test, pred)
pp('정확도: ', round(acc, 4))

# 실제값 / 예측값 비교 출력
result = pd.DataFrame({
    '실제값': y_test.iloc[:5].to_numpy(),
    '예측값': pred[:5]
}, index=y_test.index[:5])
result['실제품종'] = result['실제값'].map(dict(enumerate(iris.target_names)))
result['예측품종'] = result['예측값'].map(dict(enumerate(iris.target_names)))
pp(result)

# 테스트 데이터 앞 3건의 클래스별 예측 확률
proba = model.predict_proba(X_test.iloc[:3])
proba_df = pd.DataFrame(
    proba,
    columns= iris.target_names,
    index=X_test.index[:3]
).round(4)
pp(proba_df)

up(5)















































