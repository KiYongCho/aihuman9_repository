# day7_basic.py

from pathlib import Path

DATA_DIR = Path('day7_basic_data') # 경로
DATA_DIR.mkdir(exist_ok=True) # 경로가 없으면 생성
FILE_PATH = DATA_DIR / 'learning_log.txt' # 학습 기록 파일 경로

# 처음 저장할 학습기록
first_log = (
    '과정명: AI휴먼\n'
    '학습주제: 파일 입출력과 예외처리\n'
    '핵심 개념: with open()은 파일을 자동으로 닫아준다.\n'
)

# 파일 생성해서 첫번째 학습기록 쓰가
with open(FILE_PATH, 'w', encoding='utf-8') as file:
    file.write(first_log)

# 추가할 기록
review_log = '다음에 복습할 내용: try-except\n'

# 파일에 추가할 기록 추가
with open(FILE_PATH, 'a', encoding='utf-8') as file:
    file.write(review_log)

# 파일 내용 읽어서 저장
with open(FILE_PATH, 'r', encoding='utf-8') as file:
    content = file.read()

print('저장 파일: ', FILE_PATH.resolve()) # 저장된 파일 위치 출력
print('\n[학습 기록]') # 제목 출력
print(content) # 파일 내용 출력
























