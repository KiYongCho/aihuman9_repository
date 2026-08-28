# day2_ex.py
# Python 실행 흐름, 변수, 자료형, type()

# 1. Python 코드 실행 흐름
print('실습 시작')
print('Python 코드는 기본적으로 코드의 위에서 아래로 읽어가면서 실행됨')

# 2. 리터럴과 변수 만들기
name = '홍길동' # 홍길동이라는 문자열 타입의 값을 name 변수가 가리킴
age = 22 # 22라는 정수 타입의 값을 age 변수가 가리킴
score = 85.5 # 85.5라는 실수 타입의 값을 score 변수가 가리킴
is_job_seeker = True # True라는 불리언 타입의 값을 is_job_seeker 변수가 가리킴
portfolio_url = None # None이라는 NoneType의 값을 portfolio_url 변수가 가리킴

# 3. 변수의 값과 타입을 확인
print(name, type(name))
print(age, type(age))
print(score, type(score))
print(is_job_seeker, type(is_job_seeker))
print(portfolio_url, type(portfolio_url))

# 4. 변수에 값 재할당
status = '준비중'
print(status)
status = '학습중'
print(status)

# 5. 동적 타이핑
data = 100 # 100이라는 int타입의 값을 data변수가 가리킴, data변수의 타입은 int
print(data, type(data)) # 100, int
data = '백' # 백이라는 str타입의 값을 data변수가 가리킴, data변수의 타입은 str
print(data, type(data)) # 백, str
data = True # True라는 bool타입의 값을 data변수가 가리킴, data변수의 타입은 bool
print(data, type(data)) # True, bool

# 6. 변수명은 의미 있게 만드는게 중요
student_name = '김AI'
student_age = 24
desired_job = '데이터 분석가'
python_experience_years = 0.5 # 길 더라도 의미있는 이름이 좋은 이름
is_major = False

# 7. f-string으로 개인 프로필 출력
# f-string : 문자열 앞에 f를 사용, 변수의 값이나 연산결과를 포함
print('\n=== 개인 프로필 ===') # \n : newline, 줄바꿈 문자
print(f'이름: {student_name}')
print(f'나이: {student_age}')
print(f'희망 직무: {desired_job}')
print(f'파이썬 경력 년수: {python_experience_years}')
print(f'전공 여부: {is_major}')
print(f'10년 후 나이: {student_age + 10}')

# 8. 변수와 값의 참조(가리킴)
# 기본값의 경우는 값복사(value copy)가 일어남
first_score = 90
second_score = first_score # first_score = 90, second_score = 90
print(first_score)
print(second_score)
second_score = 50 # first_score = 90, second_score = 50
print(first_score)
print(second_score)
first_score = 30
print(first_score)
print(second_score)

# 9. 흔한 오류
# 2name = '홍길동' # SyntaxError: invalid decimal literal
# job = AI개발자 # NameError: name 'AI개발자' is not defined
# print(user_name) # NameError: name 'user_name' is not defined

# 10. 상수 (constant)
# - 상수는 한번 값을 할당하면 할당된 값을 변경할 수 없는 변수
# - 상수는 대문자로 만드는 관례가 있음
PI = 3.141592
print(PI)
TOTAL_OF_STUDENTS = 100
print(TOTAL_OF_STUDENTS)

# 11. extra
oct_num = 0o10 # 8진 정수 10
print(oct_num, type(oct_num)) # 8, int
hex_num = 0xff # 16진 정수 FF
print(hex_num, type(hex_num)) # 255, int

# 진법, 진수, 진법 변환
# 진법 : 수를 표현하는 방법
# 진수 : 진법에 의해서 사용되는 수  예) 2진수 : 0, 1
# 컴퓨터에서는 2, 8, 16진법을 사용, 일상 생활에서는 10진법을 사용
# 진법 변환
# 1. 10진수를 다른진수로 바꿀때는 계속 진법수로 나눠서 꺼꾸로 쓰기
# 2. 다른진수를 10진수로 바꿀때는 각 자리수에 진법수 제곱을 모두 더함




























