# day6_application.py

students = {
    '김민수': 87,
    '이서연': 95,
    '박준호': 73,
    '최지우': 61,
    '정하늘': 55
}

# 점수를 받아서 등급을 반환하는 함수
def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# 아이템들에서 키(이름)와 값(점수) 순회
for name, score in students.items():
    grade = get_grade(score) # 등급
    print(f'{name} | {score}점 | {grade}등급')














