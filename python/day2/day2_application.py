# day2_application.py

learner_name = '김AI'
age = 24
target_job = '데이터 분석가'
python_experience_years = 0.5
is_job_seeker = True
portfolio_url = None

print('=== AI휴먼 학습 프로필 카드 ===')
print(f'이름: {learner_name}')
print(f'나이: {age}')
print(f'희망 직무: {target_job}')
print(f'Python 경험: {python_experience_years}')
print(f'취업준비 여부: {is_job_seeker}')
print(f'포트폴리오: {portfolio_url}')

print('\n=== 자료형 점검 ===')
print(f'learner_name -> {type(learner_name)}')
print(f'age -> {type(age)}')
print(f'target_job -> {type(target_job)}')
print(f'python_experience_years -> {type(python_experience_years)}')
print(f'is_job_seeker -> {type(is_job_seeker)}')
print(f'portfolio_url -> {type(portfolio_url)}')

print('\n=== 상태 변경 ===')
status = '학습 시작'
print(f'변경 전: {status}')
status = 'Day2 완료'
print(f'변경 후: {status}')









