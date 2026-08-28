# day5_application.py

scores = [72, 88, 95, 61, 83, 90]

total = 0 # 전체 합계
pass_count = 0 # 합격자 수
highest = scores[0] # 첫번째 요소를 최고점으로

for score in scores:
    total += score
    if score >= 80:
        pass_count += 1
    if score > highest:
        highest = score

student_count = len(scores) # 전체 학생 수
average = total / student_count # 평균

print(f'전체 학생 수: {student_count}')
print(f'점수 합계: {total}')
print(f'평균 점수: {average:.2f}') # 소수 두째자리까지
print(f'합격자 수: {pass_count}')
print(f'최고점: {highest}')







