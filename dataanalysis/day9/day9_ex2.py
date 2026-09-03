# day9_ex2.py
# NumPy 정렬, 결합, 중복 제거 함수

import numpy as np

# 1. np.sort() - 배열의 값을 오름차순으로 정렬한 새로운 배열을 반환
arr = np.array([50, 20, 40, 10, 30])
sorted_arr = np.sort(arr)
print("원본:", arr)
print("오름차순 정렬:", sorted_arr)
sorted_desc = np.sort(arr)[::-1] # 내림차순 정렬은 오름차순 결과를 역순으로 슬라이싱
print("내림차순 정렬:", sorted_desc)

# 2. np.argsort() - 값을 정렬했을 때의 인덱스 순서를 반환
arr = np.array([50, 20, 40, 10, 30])
index = np.argsort(arr)
print("원본:", arr)
print("정렬 인덱스:", index)
# argsort()가 반환한 인덱스를 배열에 적용하면 실제로 정렬된 값을 얻을 수 있음
print("정렬된 값:", arr[index])

# 이름과 점수를 함께 정렬하는 예제
names = np.array(["민준", "서연", "지훈", "하은"])
scores = np.array([85, 95, 75, 90])
index = np.argsort(scores) # 점수를 기준으로 정렬할 인덱스를 구함
# 같은 인덱스를 이름과 점수 배열에 적용하면
# 두 배열의 대응 관계를 유지하면서 정렬할 수 있음
print("점수 기준 이름 정렬:", names[index])
print("점수 오름차순:", scores[index])

# 3. np.concatenate() - 기존 axis를 기준으로 연결

# 1차원 배열 연결
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = np.concatenate((a, b))
print(result)

# 2차원 배열 연결
a = np.array([ [1, 2], [3, 4] ])
b = np.array([ [5, 6], [7, 8] ])
result_axis0 = np.concatenate((a, b), axis=0) # 행 방향 연결
print(result_axis0)
result_axis1 = np.concatenate((a, b), axis=1) # 열 방향 연결
print(result_axis1)

# 4. np.vstack() - Vertical Stack, 세로 방향 결합, 여러 배열을 위아래 방향으로 쌓음
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = np.vstack((a, b))
print(result)
print(result.shape) # 1차원 배열 두개를 쌓으면 2차원 배열

# 5. np.hstack() - Horizontal Stack, 가로 방향 결합, 여러 배열을 좌우 방향으로 연결
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = np.hstack((a, b))
print(result)
# 2차원 배열의 hstack
a = np.array([ [1, 2], [3, 4] ])
b = np.array([ [5], [6] ])
result = np.hstack((a, b))
print(result)

# 6. np.unique() - 배열에서 중복된 값을 제거하고 고유값만 반환

arr = np.array([10, 20, 10, 30, 20, 40, 10])
result = np.unique(arr)
print("원본:", arr)
print("고유값:", result)

# return_counts=True를 사용하면
# 각 고유값이 몇 번 등장했는지도 함께 확인 가능
values, counts = np.unique(arr, return_counts=True)
print("고유값:", values)
print("개수:", counts)


# 문자열 범주형 데이터의 빈도 확인
grades = np.array(["A", "B", "A", "C", "B", "A"])
values, counts = np.unique(grades, return_counts=True)
print("등급:", values)
print("등급별 개수:", counts)