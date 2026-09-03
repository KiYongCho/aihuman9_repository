# day8_application.py

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
    Student('정하늘', 88)
]

# 객체 리스트에서 객체 순회 출력
for student in students:
    student.show()










