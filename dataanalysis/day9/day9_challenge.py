# day9_challenge.py

import numpy as np

# 4개 생산라인 (행), 6시간 불량 개수 (열)
defects = np.array([
    [3, 5, 4, 6, 2, 4],
    [6, 7, 5, 8, 6, 7],
    [2, 3, 1, 4, 3, 2],
    [4, 5, 6, 5, 7, 4]
])

# 각 라인의 평균 불량 개수
print('라인별 평균: ', np.round(defects.mean(axis=1), 2))

# 시간대별 전체 불량 개수
print('시간대별 합계: ', defects.sum(axis=0))

# 각 라인별 시간당 목표 불량 개수
target = np.array([4, 5, 3, 4]) # 1행 4열

# 목표 불량 개수를 4행 1열로 변경
target_column = target[:, np.newaxis]
print('목표 shape: ', target_column.shape)

# 실제 불량 개수에서 각 라인의 목표값을 뺌
difference = defects - target_column
print('목표 대비 차이: \n', difference)

# 실제 불량 개수가 라인별 목표값보다 큰 위치 Boolean 배열
over_target = defects > target_column
print('목표 초과 여부: \n', over_target)

# 각 행의 True 개수를 더해서 라인별 목표 초과 회수 계산
over_count = over_target.sum(axis=1)
print('라인별 목표 초과 회수: ', over_count)

# 목표 초과 회수가 가장 많은 라인의 인덱스
worst_line_index = np.argmax(over_count)
print('최다 초과 라인 인덱스: ', worst_line_index)

# 각 라인의 최소값을 구하고 4행 1열 형태로
line_min = defects.min(axis=1)[:, np.newaxis]
print(line_min)
print('라인별 최소값 shape: ', line_min.shape)

# 각 라인의 최대값을 구하고 4행 1열 형태로
line_max = defects.max(axis=1)[:, np.newaxis]
print(line_max)
print('라인별 최대값 shape: ', line_max.shape)

# 정규화 (Normalization)
# : 어떤 범위의 값들을 지정한 다른 범위의 값들로 치환하는 과정

# Min-Max 정규화
# 원래값에서 최소값을 뺀 값을 최대값에서 최소값 뺀 값으로 나눠서
# 모든 값을 0~1 범위 안에 있도록 값을 재구성

# Min-Max 정규화 공식의 분모 구하기
range_value = line_max - line_min # 최대값 - 최소값

# 브로드캐스팅으로 각 라인 내부의 값을 0~1 범위로 정규화
normalized = (defects - line_min) / range_value

# 결과 출력
print('라인별 Min-Max 정규화: \n', np.round(normalized, 2))

































