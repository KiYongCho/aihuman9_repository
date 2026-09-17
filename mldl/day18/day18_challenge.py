# day18_challenge.py

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from include.graph_config import set_graph
from util.print_util import pp, pt, up

set_graph(10, 8, 13)

# 각 입력 데이터는 8x8 손글씨 이미지를 펼친 64개 픽셀 특성으로 구성
'''
data.data        8×8 이미지의 64개 픽셀 밝기값
data.target      손글씨 숫자(0~9)
'''

# 데이터 로드
digits = load_digits(as_frame=True)

# X, y
X = digits.data
y = digits.target
pp(X.shape)
pp(y.shape)

# 클래스별 데이터 개수
pp(y.value_counts().sort_index())

# train / test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# LogisticRegression 모델 생성
logistic = LogisticRegression(
    max_iter=3000
)

# 학습
logistic.fit(X_train, y_train)

# 예측
logistic_pred = logistic.predict(X_test)

# 정확도
logistic_acc = accuracy_score(y_test, logistic_pred)

# KNN 모델 생성
knn = KNeighborsClassifier(
    n_neighbors=3
)

# 학습
knn.fit(X_train, y_train)

# 예측
knn_pred = knn.predict(X_test)

# 정확도
knn_acc = accuracy_score(y_test, knn_pred)

# 정확도뿐 아니라 맞힌 개수와 틀린 개수도 비교
comparison = pd.DataFrame({
    '모델': ['LogisticRegression', 'KNN'],
    '정확도': [logistic_acc, knn_acc],
    '정답수': [
        (logistic_pred == y_test.to_numpy()).sum(),
        (knn_pred == y_test.to_numpy()).sum()
    ],
    '오답수': [
        (logistic_pred != y_test.to_numpy()).sum(),
        (knn_pred != y_test.to_numpy()).sum()
    ]
})
comparison['정확도'] = comparison['정확도'].round(4)
pp(comparison)

# 정확도가 높은 모델의 이름과 예측 결과를 선택
if logistic_acc > knn_acc:
    best_name = 'LogisticRegression'
    best_pred = logistic_pred
elif logistic_acc < knn_acc:
    best_name = 'KNN'
    best_pred = knn_pred
else:
    best_name = '두 모델의 정확도가 같음'
    best_pred = logistic_pred
pp('정확도가 높은 모델 : ', best_name)
pp('모델의 정확도 : ', best_pred)

# 실제값과 예측값이 다른 행만 필터링해 오분류 사례를 확인
error_df = pd.DataFrame({
    '실제값': y_test.to_numpy(),
    '예측값': best_pred
}, index=y_test.index)

error_df = error_df[error_df['실제값'] != error_df['예측값']]
pp(error_df.head(10))

# 어떤 실제 숫자에서 오분류가 많이 발생했는지 빈도를 집계
error_count = error_df['실제값'].value_counts().sort_index()
pp(error_count)

# 두 모델의 정확도를 막대그래프로 비교
plt.bar(comparison['모델'], comparison['정확도'])
plt.ylim(0, 1) # y축 값 제한
plt.ylabel('정확도')
plt.title('손글씨 숫자 분류 모델 정확도 비교')
for i, value in enumerate(comparison['정확도']):
    # 그래프에 텍스트 출력, ha:horizontal alignment(수평정렬)
    plt.text(i, value + 0.01, f'{value:.4f}', ha='center')
plt.tight_layout()
plt.show()

up(5)






















