# day22_basic.py

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from util.print_util import pp, up

df = pd.DataFrame({
    "주간도서관방문": [6, 7, 5, 1, 2, 1, 4, 5, 4, 2, 3, 2],
    "일평균열람시간": [220, 245, 210, 45, 60, 50, 150, 170, 140, 80, 95, 75],
    "온라인강의시간": [3, 2, 4, 10, 9, 11, 6, 5, 7, 8, 7, 9]
})

features = ['주간도서관방문', '일평균열람시간', '온라인강의시간']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[features])

model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# 스케일링 데이터로 학습 후 군집 예측
df['군집'] = model.fit_predict(X_scaled)

pp('군집별 데이터 수')
pp(df['군집'].value_counts().sort_index())
pp('군집별 평균 이용 특성')
pp(df.groupby('군집')[features].mean().round(2))

# 표준화된 군집 중심을 원래 단위로 복원
centers = scaler.inverse_transform(model.cluster_centers_)

center_df = pd.DataFrame(centers, columns=features).round(2)
center_df.index.name = '군집'

pp('원래 단위의 군집 중심점')
pp(center_df)
pp('전체 군집 결과')
pp(df)

up(5)









































