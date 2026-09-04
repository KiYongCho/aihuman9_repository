# day9_basic.py

import numpy as np

# 1차원 리스트 > 1차원 배열
wait_times = np.array([12, 8, 15, 6, 20, 9, 11, 7])

print('shape: ', wait_times.shape) # (8,)
print('ndim: ', wait_times.ndim) # 1
print('size: ', wait_times.size) # 8
print('dtype: ', wait_times.dtype) # int64

total_wait = wait_times.sum() # 합계, 메소드 방식
# total_wait = np.sum(wait_times) # 합계, 함수 방식
avg_wait = wait_times.mean() # 평균
min_wait = wait_times.min() # 최소값
max_wait = wait_times.max() # 최대값

print('합계:', total_wait)
print('평균:', avg_wait)
print('최소값:', min_wait)
print('최대값:', max_wait)

# 평균보다 긴 대기시간, 조건 인덱싱
long_waits = wait_times[wait_times > avg_wait]
print(long_waits)

# 모든 대기시간을 2분 줄임, 벡터 연산
improved_wait_times = wait_times - 2
print(improved_wait_times)

# 개선 후 평균 대기시간
improved_avg = improved_wait_times.mean()
print(improved_avg)






































