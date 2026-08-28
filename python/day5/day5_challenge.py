# day5_challenge.py

students = {
    "민수": 72,
    "지연": 88,
    "준호": 95,
    "서연": 61,
    "하늘": 84
}

total = 0 # 전체 점수 합계
pass_count = 0 # 합격자 수
top_name = '' # 최고점자 이름
top_score = -1 # 최고점 초기값을 -1로

print('학생 성적표')
print('-' * 34)

for name, score in students.items():
    total += score
    if score >= 80:
        pass_count += 1
    if score > top_score:
        top_score = score
        top_name = name
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    else:
        grade = 'D'

    status = 'PASS' if score >= 80 else 'RETRY'

    print(f'{name} | {score}점 | {grade}등급 | {status}')

student_count = len(students) # 전체 학생 수
average = total / student_count # 평균

print('-' * 34)
print(f'평균: {average:.2f}')
print(f'합격자 수: {pass_count}')
print(f'최고점: {top_name} / {top_score}점')

























