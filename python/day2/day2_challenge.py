# day2_challenge.py

raw_age = '25'
raw_score = '91.5'
name = '홍길동'

print('=== 원본 데이터 자료형 확인 ===')
print(f'raw_age: {type(raw_age)}')
print(f'raw_score: {type(raw_score)}')
print(f'name: {type(name)}')

# 정수로 변환 가능한 문자열을 실수로 변환한 경우
# 원하던 25는 아니지만 에러가 없음
# why? 실수의 범위가 정수의 범위보다 크므로 데이터 손실의 염려가 없음
#      그래서 에러가 나지 않음
age = float(raw_age)
print(age) # 25.0

# 정수로 변환 가능한 문자열을 정수로 변환한 경우
age = int(raw_age) # 문자열을 정수로  변환
print(age, type(age)) # 25, int

# 실수로 변환 가능한 문자열을 정수로 변환한 경우
# ValueError: invalid literal for int() with base 10: '91.5'
# why? 실수의 소수점 이하 데이터가 소실될 수 있음
#      데이터 손실이 있을 수 있으므로 에러
# score = int(raw_score)
# print(score)

# 실수로 변환 가능한 문자열을 실수로 변환한 경우
score = float(raw_score) # 문자열을 실수로 변환
print(score, type(score)) # 91.5, float

print('\n=== 최종 문장 ===')
print(f'{name}님의 나이는 {age}세이고 점수는 {score}점 입니다!')

portfolio_url = None
print('\nportfolio_url: ', portfolio_url, type(portfolio_url))













