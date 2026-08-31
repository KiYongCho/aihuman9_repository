# day6_ex.py
# function, parameter, argument, return, score, ...

# 1. 함수 정의 / 호출
# 함수 정의
def say_hello():
    print('안녕하세요! AI휴먼과정입니다!')
    # return None 이 생략된 것!
# 함수 호출
say_hello()

# 2. 매개변수와 인수
def greet(name):
    print(f'{name}님 안녕하세요!')
greet('김민수')
greet('이서연')

# 3. 여러 매개변수와 return
def add(a, b):
    result = a + b
    return result # 값을 리턴시는 return구문 생략 불가
sum_result = add(10, 20)
print(f'10 + 20 = {sum_result}')

# 4. print()와 return의 차이
def add_print(a, b):
    print(a + b)
def add_return(a, b):
    return a + b
add_print(10, 20)
returned_value = add_return(10, 20)
print(f'반환값: {returned_value}')

# 5. 위치 인수와 키워드 인수
def introduce(name, job):
    print(f'이름: {name} | 희망직무: {job}')
introduce('박준호', 'AI개발자') # 위치 인수
introduce(job='데이터 분석가', name='최지우') # 키워드 인수

# 6. 기본값 매개변수
# message파라미터에 인수 전달이 안되면 '환영합니다'를 사용
def welcome(name, message='환영합니다'):
    print(f'{name}님 {message}')
welcome('김하늘') # message='환영합니다'
welcome('정우진', '오늘도 파이팅!') # message='오늘도 파이팅!'

# 7. 조건문을 함수로 분리
def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

grade = get_grade(87) # B

test_scores = [95, 84, 76, 59]
for score in test_scores:
    current_grade = get_grade(score)
    print(f'{score}점 -> {current_grade}등급')

# 8. 리스트를 매개변수로 전달받아 평균 구하기
def get_average(scores):
    total = 0 # 총점
    for score in scores:
        total += score # 총점 누적
    return total / len(scores) # 평균 반환

my_scores = [85, 90, 78]

my_average = get_average(my_scores)
print(f'평균: {my_average:.1f}') # 소수 첫째자리 평균

my_grade = get_grade(my_average) # 평균으로 등급 계산
print(f'등급: {my_grade}')

# 9. 여러 값을 반환
def get_total_average(score1, score2):
    total = score1 + score2
    average = total / 2
    return total, average # 2개 값을 반환

# 반환된 2개의 값을 각 변수에 할당 (unpacking, 구조분해할당)
total_score, average_score = get_total_average(88, 92)

print(f'총점: {total_score}, 평균: {average_score:.1f}')

# 10. 전역변수의 변경은 함수내에서 하지 않도록!
#     why? 외부스코프의 변수값에 내부스코프가 영향을 주는 건 좋지 않음
#          명확한 스코프 분리가 모듈화에 유리

# count : increase함수의 지역변수
# count는 increase함수가 호출되어야 메모리에 생성됨
# increate함수가 return하면 메모리에서 제거됨
# 즉, count는 외부 전역변수의 값에 영향을 주지 않음
# 이런 함수를 순수함수(pure function)이라 함
# 순수함수로 프로그래밍하는 기법을 함수형프로그래밍이라 함
def increase(count):
    return count + 1

# 전역변수
current_count = 0

current_count = increase(current_count)
current_count = increase(current_count)
current_count = increase(current_count)

print(f'current_count = {current_count}')

# scope chain
x = 100 # 전역 변수

def outer(): # outer(enclosing) function
    y = 200 # outer function의 지역 변수
    def inner(): # inner(nested) function
        z = 300 # inner function의 지역 변수
        print(z)
        print(y)
        print(x)
    inner()

outer()

# closure
def outer():
    x = 10 # outer함수의 지역변수
    def inner(): # inner함수에서 outer함수의 변수를 사용
        print(x)
    return inner # inner함수를 리턴

func = outer()

func() # 10 , x변수가 살아있음!

# lambda function
squarex = lambda x : x**2
print(squarex(5)) # 25

students  = [
    ('철수', 85),
    ('영희', 92),
    ('민수', 78),
    ('지영', 90)
]
students_asc = sorted(students, key=lambda x : x[1]) # 이터러블, 정렬기준
print(students)
print(students_asc)
students_asc = sorted(students, key=lambda x : x[1], reverse=True) # reverse=True : 내림차순정렬
print(students)
print(students_asc)

# 고차함수, 콜백함수

# 고차함수
def calc(a, b, f): # 2개의 값, 1개의 함수
    return f(a, b) # 2개의 값을 인자로하는 함수의 실행결과를 리턴

print(calc(3, 5, lambda a, b: a + b)) # 콜백함수
print(calc(3, 5, lambda a, b: a - b))
print(calc(3, 5, lambda a, b: a * b))
print(calc(3, 5, lambda a, b: a / b))

# map(람다함수, 이터러블) 고차함수
# : 이터러블의 각 요소에 람다함수를 적용하는 함수
# 고차함수: map, 콜백함수: 람다함수
scores = [90, 85, 75]
new_scores = list(map(lambda x : x+10, scores))
print(new_scores)

# filter(람다함수, 이터러블) 고차함수
# : 이터러블의 각 요소 중 람다함수 조건에 맞는 요소를 추출하는 함수
# 고차함수: filter, 콜백함수: 람다함수
scores = [90, 85, 75]
new_scores = list(filter(lambda x : x>80, scores))
print(new_scores)




























