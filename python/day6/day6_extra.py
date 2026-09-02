# day6_extra.py

# [AI휴먼 6일차 추가 실습]
# 주제: Python 함수 실습
# 문항 수: 10문항

# ============================================================
# 1. 리스트에서 최댓값과 최솟값 찾기
# ============================================================
#
# 숫자 리스트를 매개변수로 전달받아 최댓값과 최솟값을 각각 구한 뒤
# 두 값을 튜플 형태로 반환하는 find_min_max() 함수를 작성하세요.
#
# 단, max(), min() 내장 함수는 사용하지 마세요.
#
# [실행 예]
# numbers = [17, 5, 23, 9, 11]
# result = find_min_max(numbers)
# print(result)
#
# [출력 예]
# (5, 23)

def find_min_max(numbers):
    minimum = numbers[0] # 최소값
    maximum = numbers[0] # 최대값
    for number in numbers:
        if number < minimum: # 더 작다면 최소값 교체
            minimum = number
        if number > maximum: # 더 크다면 최대값 교체
            maximum = number
    return minimum, maximum # 튜플로 두 값을 하나로 반환

numbers = [17, 5, 23, 9, 11]
print(find_min_max(numbers)) # (5, 23)

min_num = find_min_max(numbers)[0]
max_num = find_min_max(numbers)[1]
print(min_num, max_num)


# ============================================================
# 2. 합격자 점수만 추출하는 함수
# ============================================================
#
# 학생 점수 리스트를 전달받아 60점 이상인 점수만 새로운 리스트에
# 저장하여 반환하는 get_pass_scores() 함수를 작성하세요.
#
# 단, filter() 함수와 리스트 컴프리헨션은 사용하지 마세요.
#
# [실행 예]
# scores = [45, 72, 88, 59, 60, 91]
# print(get_pass_scores(scores))
#
# [출력 예]
# [72, 88, 60, 91]

def get_pass_scores(scores):
    pass_scores = [] # 조건을 만족하는 요소들을 넣을 빈 리스트
    for score in scores:
        if score >= 60: # 조건을 만족하면 리스트에 추가
            pass_scores.append(score)
    return pass_scores

scores = [45, 72, 88, 59, 60, 91]
print(get_pass_scores(scores))


# ============================================================
# 3. 문자열 분석 결과 반환 함수
# ============================================================
#
# 문자열 하나를 전달받아 다음 정보를 계산하는 analyze_text() 함수를 작성하세요.
#
# 1) 전체 문자 수
# 2) 공백을 제외한 문자 수
# 3) 문자열에 포함된 숫자 문자의 개수
#
# 계산 결과는 다음 형식의 딕셔너리로 반환하세요.
#
# {
#     "전체문자수": 값,
#     "공백제외문자수": 값,
#     "숫자개수": 값
# }
#
# [실행 예]
# text = "Python 3 Function 2026"
# print(analyze_text(text))
#
# [출력 예]
# {'전체문자수': 22, '공백제외문자수': 19, '숫자개수': 5}

def analyze_text(text):
    total_count = len(text) # 전체 문자 수
    non_space_count = 0 # 공백을 제외한 문자 수
    digit_count = 0 # 숫자 문자 수
    for char in text: # 문자열내의 문자 수만큼 반복
        if char != ' ': # 공백문자가 아니면
            non_space_count += 1
        if char.isdigit(): # 숫자인지
        # if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            digit_count += 1
    return {
        '전체문자수': total_count,
        '공백제외문자수': non_space_count,
        '숫자문자수': digit_count
    }

text = 'Python 3 Function 2026'
print(analyze_text(text))

# ============================================================
# 4. 학생별 총점과 평균 계산 함수
# ============================================================
#
# 다음과 같은 학생별 점수 딕셔너리가 있습니다.
#
# students = {
#     "김철수": [80, 90, 70],
#     "이영희": [95, 88, 92],
#     "박민수": [60, 75, 68]
# }
#
# 학생 이름과 점수 리스트를 전달받아 총점과 평균을 계산하여
# 딕셔너리로 반환하는 calculate_student() 함수를 작성하세요.
#
# 반환 형식은 다음과 같습니다.
#
# {
#     "이름": 학생이름,
#     "총점": 총점,
#     "평균": 평균
# }
#
# 그리고 반복문을 이용하여 모든 학생의 결과를 출력하세요.
#
# [출력 예]
# {'이름': '김철수', '총점': 240, '평균': 80.0}
# {'이름': '이영희', '총점': 275, '평균': 91.66666666666667}
# {'이름': '박민수', '총점': 203, '평균': 67.66666666666667}

students = {
    '김철수': [80, 90, 70],
    '이영희': [95, 88, 92],
    '박민수': [60, 75, 68]
}

def calculate_student(name, scores):
    total = 0 # 총점
    for score in scores:
        total += score
    average = total / len(scores) # 평균
    return { # 딕셔너리 반환
        '이름': name,
        '총점': total,
        '평균': average
    }

for name, scores in students.items():
    print(calculate_student(name, scores))

# ============================================================
# 5. 가변 인수를 이용한 합계 함수
# ============================================================
#
# 전달되는 숫자의 개수가 정해져 있지 않을 때 사용할 수 있도록
# 가변 인수 *args를 이용하여 모든 숫자의 합을 반환하는
# sum_all() 함수를 작성하세요.
#
# 파이썬의 내장 함수 sum()은 사용하지 마세요.
#
# [실행 예]
# print(sum_all(10, 20, 30))
# print(sum_all(1, 2, 3, 4, 5))
#
# [출력 예]
# 60
# 15

# 인수의 수에 상관없이 모든 인수를 args에 튜플 형태로 저장
def sum_all(*args):
    total = 0 # 합계
    for number in args: # 튜플의 요소 수만큼 반복
        total += number
    return total

print(sum_all(10, 20, 30))
print(sum_all(1, 2, 3, 4, 5))

# ============================================================
# 6. 기본값 매개변수를 이용한 급여 계산 함수
# ============================================================
#
# 기본 급여와 보너스율을 전달받아 최종 급여를 계산하는
# calculate_salary() 함수를 작성하세요.
#
# 최종 급여 = 기본 급여 + (기본 급여 × 보너스율)
#
# 보너스율의 기본값은 0.1(10%)로 설정하세요.
#
# [실행 예]
# print(calculate_salary(3000000))
# print(calculate_salary(3000000, 0.2))
#
# [출력 예]
# 3300000.0
# 3600000.0

# bonus_rate 파라미터에 인수가 전달되면 인수를 사용, 그렇지 않으면 0.1을 사용
def calculate_salary(base_salary, bonus_rate=0.1):
    final_salary = base_salary + (base_salary * bonus_rate)
    return final_salary

# 숫자 세자리마다 _ 사용 가능
print(calculate_salary(3_000_000))
print(calculate_salary(3_000_000, 0.2))

# ============================================================
# 7. 함수를 이용한 학생 성적 처리
# ============================================================
#
# 아래와 같은 학생 점수 딕셔너리가 있습니다.
#
# students = {
#     "김철수": 85,
#     "이영희": 92,
#     "박민수": 76,
#     "최지우": 64
# }
#
# 다음 2개의 함수를 작성하세요.
#
# 1) get_grade(score)
#    - 점수를 전달받아 A, B, C, D, F 중 하나를 반환
#
# 2) make_report(students)
#    - 학생 딕셔너리를 전달받아
#      "이름 : 점수점 / 등급"
#      형식의 문자열 리스트를 반환
#
# [출력 예]
# 김철수 : 85점 / B
# 이영희 : 92점 / A
# 박민수 : 76점 / C
# 최지우 : 64점 / D

students = {
    "김철수": 85,
    "이영희": 92,
    "박민수": 76,
    "최지우": 64
}

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def make_report(students):
    report = [] # 결과문자열 저장 리스트
    for name, score in students.items():
        grade = get_grade(score)
        line = f'{name} : {score}점 / {grade}'
        report.append(line) # 리스트에 한 줄 저장
    return report

result = make_report(students)

for line in result:
    print(line)

# ============================================================
# 8. 고차함수 - 계산 함수를 인수로 전달하기
# ============================================================
#
# 함수를 다른 함수의 인수로 전달하는 고차함수를 작성하세요.
#
# 다음 함수들을 작성하세요.
#
# 1) add(a, b)      : 두 수의 합 반환
# 2) subtract(a, b) : 두 수의 차 반환
# 3) multiply(a, b) : 두 수의 곱 반환
# 4) calculate(a, b, operation)
#    - a, b와 함께 계산 함수를 operation으로 전달받아
#      해당 함수의 실행 결과를 반환
#
# [실행 예]
# print(calculate(10, 5, add))
# print(calculate(10, 5, subtract))
# print(calculate(10, 5, multiply))
#
# [출력 예]
# 15
# 5
# 50

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

# 고차함수 : 두 인수와 콜백함수를 파라미터로
def calculate(a, b, operation):
    # 콜백함수에 두 인수를 전달해 처리한 결과를 리턴
    return operation(a, b)

print(calculate(10, 5, add))
print(calculate(10, 5, subtract))
print(calculate(10, 5, multiply))

# ============================================================
# 9. 콜백함수 - 주문 처리 완료 후 함수 호출하기
# ============================================================
#
# 온라인 주문 처리 상황을 함수로 구현하세요.
#
# 다음 함수를 작성하세요.
#
# 1) payment_complete(order_name)
#    - "[주문명] 결제가 완료되었습니다." 출력
#
# 2) send_message(order_name)
#    - "[주문명] 주문 완료 메시지를 전송했습니다." 출력
#
# 3) process_order(order_name, callback)
#    - "[주문명] 주문을 처리합니다." 출력
#    - 처리가 끝난 후 callback(order_name)을 호출
#
# process_order()에 서로 다른 콜백함수를 전달하여
# 다른 후속 작업이 실행되는 것을 확인하세요.
#
# [실행 예]
# process_order("노트북", payment_complete)
# process_order("키보드", send_message)
#
# [출력 예]
# [노트북] 주문을 처리합니다.
# [노트북] 결제가 완료되었습니다.
# [키보드] 주문을 처리합니다.
# [키보드] 주문 완료 메시지를 전송했습니다.

def payment_complete(order_name):
   print(f'[{order_name}] 결제가 완료되었습니다.')

def send_message(order_name):
   print(f'[{order_name}] 주문 완료 메세지를 전송했습니다.')

# 고차함수 : 주문명, 콜백함수를 파라미터로
def process_order(order_name, callback):
    print(f'[{order_name}] 주문을 처리합니다')
    callback(order_name) # 콜백함수 호출

process_order('노트북', payment_complete)
process_order('키보드', send_message)

# ============================================================
# 10. 고차함수 + 콜백함수 - 점수 데이터 처리 시스템
# ============================================================
#
# 학생 점수 리스트를 다양한 기준으로 처리할 수 있는 프로그램을 작성하세요.
#
# scores = [55, 72, 88, 91, 67, 100, 83]
#
# 다음 함수를 작성하세요.
#
# 1) is_pass(score)
#    - 60점 이상이면 True, 아니면 False 반환
#
# 2) is_excellent(score)
#    - 90점 이상이면 True, 아니면 False 반환
#
# 3) filter_scores(scores, condition)
#    - 점수 리스트와 조건 함수를 매개변수로 전달받음
#    - condition(score)의 결과가 True인 점수만 새로운 리스트에 저장
#    - 결과 리스트 반환
#    - filter() 내장 함수는 사용하지 마세요.
#
# 4) print_result(title, result)
#    - 제목과 결과 리스트를 출력
#
# 5) process_scores(scores, condition, callback)
#    - filter_scores()를 이용해 점수를 필터링
#    - callback()을 호출하여 결과를 출력
#    - 필터링된 리스트도 반환
#
# [실행 예]
# process_scores(scores, is_pass, print_result)
# process_scores(scores, is_excellent, print_result)
#
# [출력 예]
# 결과 : [72, 88, 91, 67, 100, 83]
# 결과 : [91, 100]

scores = [55, 72, 88, 91, 67, 100, 83]

# 60이상이면 True 반환
def is_pass(score):
    return score >= 60

# 90이상이면 True 반환
def is_excellent(score):
    return score >= 90

# 고차함수 : 점수리스트와 콜백함수를 파라미터로
def filter_scores(scores, condition):
    result = [] # 조건을 만족하는 점수 저장 리스트
    for score in scores:
        if condition(score): # 콜백함수에 점수를 전달하고 받은 리턴값으로 분기
            result.append(score) # 조건 만족시 리스트에 추가
    return result

# 제목과 결과 출력 함수
def print_result(title, result):
    print(f'{title} : {result}')

# 고차함수 : 점수리스트, 점수판정콜백함수, 출력콜백함수, 제목 파라미터로
def process_scores(scores, condition, callback, title='결과'):
    filtered_scores = filter_scores(scores, condition) # 조건 만족 점수리스트
    callback(title, filtered_scores) # 콜백함수를 제목과 조건 만족 점수리스트를 인수로 호출

process_scores(scores, is_pass, print_result, '합격자 점수')
process_scores(scores, is_excellent, print_result, '우수자 점수')













