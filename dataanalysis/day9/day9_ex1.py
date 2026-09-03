# day9_ex1.py
# 주제: NumPy 배열, 수치 연산

import numpy as np

# 1. python 리스트와 numpy 배열

# 파이썬 리스트 연산
python_scores = [70, 85, 90, 95]
python_result = [] # 결과 저장 리스트
for score in python_scores:
    python_result.append(score + 5)
print('python 리스트 계산: ', python_result)

# numpy 배열 벡터 연산
numpy_scores = np.array([70, 85, 90, 95]) # ndarray 생성
print('numpy 벡터 연산: ', numpy_scores + 5)
print('배열 객체 타입: ', type(numpy_scores)) # <class 'numpy.ndarray'>

# 2. 여러 방식으로 배열 생성

# 1차원 배열 생성
arr1 = np.array([10, 20, 30, 40, 50])
print(arr1)

# 0부터 10미만까지 2씩 증가하는 배열 생성
arr2 = np.arange(0, 10, 2)
print(arr2)

# 0부터 1까지를 5개의 동일한 간격으로 분할한 배열 생성
arr3 = np.linspace(0, 1, 5)
print(arr3)

# 2행 3열을 모두 0.으로 채운 배열 생성
zeros = np.zeros((2, 3))
print(zeros)

# 2행 3열을 모두 1로 채운 배열 생성
ones = np.ones((2, 3))
print(ones)

# 2행 3열을 모두 지정한 수로 채운 배열 생성
full = np.full((2, 3), 7)
print(full)

# 3. shape, ndim, size, dtype 확인
students_scores = np.array([
    [80, 90, 85],
    [70, 75, 95]
])
print('shape: ', students_scores.shape) # (2, 3), 모양
print('ndim: ', students_scores.ndim) # 2, 차원 수
print('size: ', students_scores.size) # 6, 전체 요소 수
print('dtype: ', students_scores.dtype) # int64, 요소 데이터타입

# 4. dtype 지정, 자료형 변환
flast_scores = np.array([70, 85, 90], dtype=np.float64)
print(flast_scores) # [70. 85. 90.]
print(flast_scores.dtype) # float64

int_scores = flast_scores.astype(np.int32) # 4바이트 정수로 변환
print(int_scores) # [70 85 90]
print(int_scores.dtype) # int32

# 5. numpy 주요 상수
print('np.pi: ', np.pi)
print('np.e: ', np.e)
print('np.inf: ', np.inf)
print('np.nan: ', np.nan)

# nan 비교는 np.isnan() 함수 사용
print(np.nan == np.nan) # False
print(np.isnan(np.nan)) # True

# 6. 1차원 배열 인덱싱과 슬라이싱
values = np.array([10, 20, 30, 40, 50, 60])
print('첫번째 요소: ', values[0]) # 10
print('마지막 요소: ', values[-1]) # 60
print('values[1:4]: ', values[1:4]) # [20 30 40]
print('values[:3]: ', values[:3]) # [10 20 30]
print('values[::2]: ', values[::2]) # [10 30 50]

# 7. 2차원 배열 인덱싱과 슬라이싱
matrix = np.array([
    [11, 12, 13, 14],
    [21, 22, 23, 24],
    [31, 32, 33, 34]
])
print('matrix[1, 2]: ', matrix[1, 2]) # 23, 2행 3열
print('두번째 행: ', matrix[1]) # [21 22 23 24]
print('세번째 열: ', matrix[:, 2]) # [13 23 33]
print('matrix[0:2, 1:3]: ', matrix[0:2, 1:3]) # [[12 13] [22 23]]

# 8. 조건 인덱싱
exam_scores = np.array([55, 70, 82, 91, 68, 88, 76, 95])
condition = exam_scores >= 80 # 80이상인지 비교한 불리언 배열 생성
print(condition) # [False False  True  True False  True False  True]
print('80 이상: ', exam_scores[condition]) # [82 91 88 95]
# 70이상 90미만 조건 인덱싱
mid_scores = exam_scores[(exam_scores >= 70) & (exam_scores < 90)]
print(mid_scores) # [70 82 88 76]
# 90 이상인 요소의 인덱스
high_indices = np.where(exam_scores >= 90)[0]
print(high_indices) # [3 7]

# 9. 벡터 연산 (Vectorized Operation)
base = np.array([10, 20, 30, 40])
print('+5: ', base + 5) # [15 25 35 45]
print('-3: ', base - 3) # [ 7 17 27 37]
print('*2: ', base * 2) # [20 40 60 80]
print('/10: ', base / 10) # [1. 2. 3. 4.]
print('**2: ', base ** 2) # [ 100  400  900 1600]

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
c = np.array([2, 3])
print('a + b', a + b) # [11 22 33]
print('a * b', a * b) # [10 40 90]
#print('a + c', a + c) # ValueError, 요소 수가 다르면 연산 불가

# 10. 집계 함수와 axis
# 집계 함수 (aggregation function) : 여러 데이터로 하나의 결과를 내는 함수
scores = np.array([ # 학생 4명, 과목 3개
    [78, 85, 92],
    [88, 90, 76],
    [95, 82, 89],
    [67, 74, 80]
])
print('전체 합계: ', scores.sum())
print('전체 평균: ', scores.mean())
print('전체 최대값: ', scores.max())
print('전체 최소값: ', scores.min())
print('과목별 평균: ', scores.mean(axis=0)) # 열, [82.   82.75 84.25]
students_avg = scores.mean(axis=1)
print('학생별 평균: ', students_avg) # 행, [85.         84.66666667 88.66666667 73.66666667]

# 평균이 85 이상인 학생의 인덱스
excellent_students = np.where(students_avg>=85)[0]
print(excellent_students) # [0 2]

# 11. reshape(), flatten()

sequence = np.arange(1, 13)
print(sequence) # [1 2 3 ... 12]

reshaped = sequence.reshape(3, 4) # 3행 4열로 모양 변경
print(reshaped) # [[ 1  2  3  4] [ 5  6  7  8] [ 9 10 11 12]]

auto_reshape = sequence.reshape(2, -1) # 열의 개수를 자동 계산
print(auto_reshape) # [[ 1  2  3  4  5  6] [ 7  8  9 10 11 12]]

flattened = sequence.flatten() # 평탄화, 2차원 배열 > 1차원 배열
print(flattened) # [ 1  2  3  4  5  6  7  8  9 10 11 12]

# 전치 : 행과 열을 뒤바꿈
print('전치 결과: ', reshaped.T) # [[ 1  5  9] [ 2  6 10] [ 3  7 11] [ 4  8 12]]

# 12. 브로드캐스팅 (broadcasting)
# 배열간 연산에서 모양이 다른 경우 연산을 위해서 내부적으로 모양을 변경하여
# 연산을 수행

# 아래 점수 보정 연산에서 2차원 배열에 1차원 배열 연산을 하기 위해서
# 내부적으로 1차원 배열을 2차원 배열로 맞춘 후 연산

# 원래 점수 : 2차원 배열
raw_scores = np.array([
    [70, 80, 90],
    [75, 85, 95]
])

# 보정 점수 : 1차원 배열
bonus = np.array([2, 3, 1])

# 보정 후 점수 : 2차원 배열
adjusted_scores = raw_scores + bonus # 2차원 배열 + 1차원 배열

print('원래 점수: ', raw_scores) # [[70 80 90] [75 85 95]]
print('보정 점수: ', bonus) # [2 3 1]
print('보정 후 점수: ', adjusted_scores) # [[72 83 91] [77 88 96]]















































































