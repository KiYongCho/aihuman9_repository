# day7_challenge.py

from pathlib import Path
import day7_challenge_utils as cutils # 생성한 모듈 사용

DATA_DIR = Path('day7_challenge_data')
DATA_DIR.mkdir(exist_ok=True)
CSV_PATH = DATA_DIR / 'challenge_scores.csv'

if not CSV_PATH.exists():
    cutils.save_sample_csv(CSV_PATH)

students = cutils.load_score_csv(CSV_PATH)

if len(students) > 0:
    # 리스트 컴프리헨션 (list comprehension)
    # 리스트 생성시 반복문과 조건문 사용하는 pythonic한(파이썬다운) 문법
    # students의 name, score에서 score들로 리스트를 구성
    scores = [score for name, score in students] # 점수 리스트
    student_count = len(scores) # 학생 수
    total_score = sum(scores) # 총점
    average_score = total_score / student_count # 평균
    max_score = max(scores) # 최고점
    min_score = min(scores) # 최저점

    print(f'정상 학생 수: {student_count}명')
    print(f'평균: {average_score:.2f}점')
    print(f'최고점: {max_score}')
    print(f'최저점: {min_score}')

    print('\n[PASS 학생]')
    for name, score in students:
        if score >= 80:
            print(f'{name}: {score}점')
else:
    print('학생 데이터가 없어 통계를 계산하지 않습니다.')



































