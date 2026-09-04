# day9_application.py

import numpy as np

# 4개 매장 (행), 5일 매출 (열), 2차원 배열
sales = np.array([
    [120, 135, 128, 142, 150],
    [98, 105, 110, 115, 120],
    [160, 155, 172, 168, 180],
    [130, 125, 140, 138, 145]
])

print('shape: ', sales.shape) # (4, 5)
print('size: ', sales.size) # 20

# 매장별 평균, 소수 두째자리에서 반올림
store_avg = sales.mean(axis=1)
print('매장별 평균: ', np.round(store_avg, 2))

# 요일별 합계
print('요일별 합계: ', sales.sum(axis=0))

# 평균 매출이 가장 높은 매장의 인덱스
print('평균 매출이 가장 높은 매장의 인덱스: ', np.argmax(store_avg))

# 전체 매출 평균, 소수 두째자리에서 반올림
print('전체 매출 평균: ', round(float(sales.mean()), 2))

# 110% 기준값
high_threshold = sales.mean() * 1.10 # 전체 평균의 1.1배
print('110% 기준값: ', round(float(high_threshold), 2))

# 기준값 이상인 매출, 조건 인덱싱
high_sales = sales[sales >= high_threshold]
print('기준값 이상인 매출: ', high_sales)

# 기준값 이상인 매출의 행/열 위치, 행인덱스들, 열인덱스들
row_indices, col_indices = np.where(sales >= high_threshold)
print('행인덱스들: ', row_indices, '열인덱스들: ', col_indices)







































