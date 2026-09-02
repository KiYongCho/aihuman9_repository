# make_daily_folder.py
# 학습 일차를 입력하면 일차에 필요한 폴더구조와 파일 생성

from pathlib import Path

# 폴더 생성 함수
def make_directory(path):
    if not path.exists():
        path.mkdir()

# 파일 생성 함수
def make_file(path):
    with open(path, 'w', newline='') as f:
        f.write('# ' + path.__str__ + "\n")
        f.write('# ')

SUBJECT = 'python'
subject_path = Path(SUBJECT)

day_str = input('학습 일차를 입력하세요!')
day_path = subject_path.joinpath('day'+day_str)

ex_path = day_path.joinpath('day' + day_str + '_ex.py')
basic_path = day_path.joinpath('day' + day_str + '_basic.py')
application_path = day_path.joinpath('day' + day_str + '_application.py')
challenge_path = day_path.joinpath('day' + day_str + '_challenge.py')

make_directory(subject_path)
make_directory(day_path)

make_file(ex_path)
make_file(basic_path)
make_file(application_path)
make_file(challenge_path)

