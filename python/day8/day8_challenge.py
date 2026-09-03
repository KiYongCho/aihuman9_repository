# day8_challenge.py

# 클래스 정의
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    # 합격 여부 계산 메서드
    def grade(self):
        if self.score >= 80:
            return 'PASS'
        return 'RETRY'
    # 학생 정보 출력 메서드
    def show(self):
        print(f'이름: {self.name}, 점수: {self.score}, 결과: {self.grade()}')

# 객체 리스트
students = [
    Student('김민수', 85),
    Student('이서연', 92),
    Student('박지훈', 76),
    Student('정하늘', 88),
    Student('오세진', 69)
]

# 전체 학생 정보 출력
print('[전체 학생]')
for student in students:
    student.show()

# 합격 학생 정보 출력
print('[합격 학생]')

pass_count = 0 # 합격 학생 수
total = 0 # 점수 합계

for student in students:
    total += student.score # 점수 누적
    if student.grade() == 'PASS': # 합격 학생이라면
        student.show() # 합격 학생 출력
        pass_count += 1 # 합격 학생 수 증가

average = total / len(students) # 평균

print(f'\n전체 평균: {average:.1f}')
print(f'\nPASS 학생 수: {pass_count}')

# 결과 파일로 저장
try:
    with open('day8_challenge_result.txt', 'w', encoding='utf-8') as file:
        for student in students:
            file.write(f'{student.name},{student.score},{student.grade()}\n')
        file.write(f'평균,{average:.1f}\n')
        file.write(f'PASS 학생 수,{pass_count}\n')
    print('결과를 day8_challenge_result.txt 파일에 저장했습니다.')
except Error as error:
    print(f'파일 저장 중 오류가 발생했습니다: {error}')
































