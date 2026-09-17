# day18_application.py

import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from util.print_util import pp, up

'''
alcohol         알코올 함량
malic_acid      말산
total_phenols   총 페놀
color_intensity 색상 강도
hue             색조
target          와인 품종
'''

# wine 데이터
wine = load_wine(as_frame=True)

# Feature 리스트
features = ['alcohol','malic_acid','total_phenols','color_intensity','hue']
pp(features)

# X / y
X = wine.frame[features]
y = wine.target

# 클래스별 데이터 수
pp(y.value_counts().sort_index())

# train / test
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# K값을 여러개 적용해서 정확도 변화 비교
rows = []
for k in [1, 3, 5, 7, 9, 11]:
    model = KNeighborsClassifier(n_neighbors=k) # KNN
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    rows.append({
        'K': k,
        '정확도': accuracy_score(y_test, pred)
    })

result_df = pd.DataFrame(rows)
result_df['정확도'] = result_df['정확도'].round(4)
pp(result_df)

# 가장 높은 정확도의 K값의 인덱스
best_index = result_df['정확도'].idxmax()

# 가장 높은 정확도의 K값
best_k = int(result_df.loc[best_index, 'K'])
pp(best_k)

# 가장 높은 정확도
best_acc = float(result_df.loc[best_index, '정확도'])
pp(best_acc)

# 선택한 K값으로 최종 모델을 다시 학습시켜서 실제값과 예측값을 비교
best_model = KNeighborsClassifier(n_neighbors=best_k)

best_model.fit(X_train, y_train)

best_pred = best_model.predict(X_test)

compare =pd.DataFrame({
    '실제값': y_test.iloc[:10].to_numpy(),
    '예측값': best_pred[:10]
}, index=y_test.index[:10])

compare['일치여부'] = compare['실제값'] == compare['예측값']
pp(compare)

up(5)































