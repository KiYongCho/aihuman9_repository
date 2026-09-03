# day8_basic.py

# 클래스 정의
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

# 객체 2개 생성
student1 = Student("김민수", 85)
student2 = Student("이서연", 92)

# 속성 출력
print(student1.name, student1.score)
print(student2.name, student2.score)