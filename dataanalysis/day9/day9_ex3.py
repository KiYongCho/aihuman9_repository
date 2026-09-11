# day9_ex3.py
# numpy 난수 생성

from util.print_util import pp, up
import numpy as np

# 난수 (Random Number)
# - 난수란 일정한 규칙 없이 무작위로 생성되는 숫자
# - numpy에서는 최신 방식으로 np.random.default_rng() 사용을 권장
# - rng (Random Number Generator) : 난수 생성기

# 난수 생성기 만들기
rng = np.random.default_rng() # 시드를 지정하지 않은 난수 생성기
pp(rng) # Generator(PCG64)
pp(rng.random()) # 0.0 <= rn < 1.0 범위의 소수점 이하 16자리 랜덤 실수

# random()
pp('난수 1개: ', rng.random())
pp('난수 5개: ', rng.random(5)) # 5개 리스트로

# seed(시드)
# - 시드는 난수 생성의 시작값
# - 시드를 고정하게 되면 동일한 패턴의 난수를 생성
#   => 생성된 수의 재현율을 높임
rng = np.random.default_rng(42) # 시드를 42로 고정
pp(rng.random())
pp(rng.random(5))

# integers() : 정수 난수 생성
# rng.integers(low, high, size) : low 이상 high 미만의 정수를 size개 생성
pp('정수 1개: ', rng.integers(1, 10)) # 1이상 10미만의 정수 1개
pp('정수 5개: ', rng.integers(1, 10, 5)) # 1이상 10미만의 정수 5개

# uniform()
# - 균등 분포 실수 난수 생성
# - 지정한 범위에서 모든 값이 비슷한 확률로 선택됨
# - 생성되는 난수가 어떤 값에 몰리는 걸 방지하려고 사용
# rng.uniform(low, high, size)
pp(rng.uniform(10, 30, size=5)) # 10.0 <= rn < 30, 5개

# normal()
# - 정규 분포 실수 난수 생성
# - 정규 분포 (Normal Distribution) : 평균을 중심으로 좌우 대칭의 종 모양을 가지는 분포
# rng.normal(loc=평균, scale=표준편차, size=개수)
scores = rng.normal(
    loc = 70,
    scale = 10,
    size = 10
)
pp(scores)

# choice() : 여러 값 중에서 무작위 선택
jobs = ['Backend', 'Frontend', 'Data']
result = rng.choice(jobs, size=10)
pp(result)

result = rng.choice(
    ['A', 'B', 'C'],
    size = 20,
    p = [0.5, 0.3, 0.2] # A가 나올 확률 50%, B 확률 30%, C 확률 20
)
pp(result)

# shuffle() : 배열 순서 섞기, 원본 배열 자체의 순서를 변경함
numbers = np.array([1, 2, 3, 4, 5])
rng.shuffle(numbers)
pp(numbers)

# permutation()
# - 순서를 섞은 새로운 배열 반환
# - 원본 배열을 변경하지 않음
numbers = np.array([1, 2, 3, 4, 5])
new_numbers = rng.permutation(numbers)
pp('원본: ', numbers)
pp('섞은 결과: ', new_numbers)

up(5)




































