# day16_basic.py

import pandas as pd
from sklearn.utils.multiclass import type_of_target
from util.print_util import pp, up

FEATURES = ['distance_km', 'package_count', 'traffic_index', 'rain_mm']
TARGET = 'delivery_minutes'

df = pd.DataFrame({
    "distance_km": [2.5, 4.1, 6.8, 3.2, 10.5, 8.7, 5.4, 12.1],
    "package_count": [1, 3, 2, 1, 5, 4, 2, 6],
    "traffic_index": [3, 6, 8, 4, 9, 7, 5, 10],
    "rain_mm": [0, 0, 4, 12, 0, 7, 1, 15],
    "delivery_minutes": [18.5, 29.2, 46.8, 35.1, 61.4, 58.7, 34.6, 79.3]
})

X = df[FEATURES]
y = df[TARGET]

pp('X shape: ', X.shape)
pp('y shape: ', y.shape)
pp('Feature columns: ', X.columns.tolist())
pp('Label name: ', y.name)
pp('Target type: ', type_of_target(y))
pp('문제 유형 : 회귀')
pp('delivery_minutes는 연속적인 수치 값을 예측하는 정답이므로')

up(5)






























