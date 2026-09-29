# day22_application.py

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from util.print_util import pp, up
from include.graph_config import set_graph

set_graph(10, 8, 13)

df = pd.DataFrame({
    "전력사용량": [82, 88, 79, 85, 91, 86, 42, 38, 45, 41, 39, 44, 65, 69, 63, 71, 67, 66],
    "평균온도": [74, 77, 72, 75, 79, 76, 48, 45, 51, 47, 46, 50, 61, 64, 59, 66, 63, 62],
    "진동수준": [6.8, 7.2, 6.5, 7.0, 7.6, 7.1, 2.1, 1.8, 2.4, 2.0, 1.9, 2.3, 4.2, 4.6, 4.0, 4.9, 4.5, 4.3],
    "일가동시간": [20, 21, 19, 22, 21, 20, 8, 7, 9, 8, 7, 9, 14, 15, 13, 16, 15, 14]
})

features = ["전력사용량", "평균온도", "진동수준", "일가동시간"]

scaler = StandardScaler()  # 서로 다른 단위의 설비 특성을 같은 거리 기준으로 맞춤
X_scaled = scaler.fit_transform(df[features])

rows = []
for k in range(2, 6): # K : 2~5
    model = KMeans(
        n_clusters=k,
        n_init=10,
        random_state=42,
    )
    labels = model.fit_predict(X_scaled)
    score = silhouette_score(
        X_scaled, # 표준화된 설비 특성
        labels # 현재 K에서 생성된 군집 번호
    )
    # 군집 수, inertia, silhouette score
    rows.append([k, model.inertia_, score])

evaluation_df = pd.DataFrame(rows, columns=["K", "Inertia", "Silhouette"])
evaluation_df['Inertia'] = evaluation_df['Inertia'].round(3)
evaluation_df['Silhouette'] = evaluation_df['Silhouette'].round(4)
pp('K별 평가 결과')
pp(evaluation_df)

# Silhouette 값이 가장 큰 인덱스에 해당하는 K
best_k = int(evaluation_df.loc[evaluation_df['Silhouette'].idxmax(), 'K'])
pp('Silhouetee 기준 선택 K:', best_k)

final_model = KMeans(
    n_clusters=best_k,
    n_init=10,
    random_state=42
)

df['군집'] = final_model.fit_predict(X_scaled)

pp('군집별 설비 수')
pp(df['군집'].value_counts().sort_index())
pp('군집별 평균 운전 특성')
pp(df.groupby('군집')[features].mean().round(2))
pp('설비별 군집 결과')
pp(df)

# K, Inertia 라인그래프
# plt.plot(evaluation_df['K'], evaluation_df['Inertia'], marker='o')
# plt.xlabel('군집 수 K')
# plt.ylabel('Inertia')
# plt.title('설비 운전 데이터 Elbow Method')
# plt.xticks(evaluation_df['K'])
# plt.grid(alpha=0.3)
# plt.tight_layout()
# plt.show()

# K, Silhouette Score 라인그래프
plt.plot(evaluation_df['K'], evaluation_df['Silhouette'], marker='o')
plt.xlabel('군집 수 K')
plt.ylabel('Silhouette Score')
plt.title('설비 운전 데이터 K별 Silhouette Score')
plt.xticks(evaluation_df['K'])
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# Silouette Score가 높아도 운영상 필요한 그룹 수와 각 군집의 해석 가능성이
# 낮을 수 있음
# 그러므로 통계 지표와 실제 활용 목적을 함께 검토해야 함

up(5)










