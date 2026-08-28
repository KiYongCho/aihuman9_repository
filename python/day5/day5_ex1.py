# day5_ex1.py
# 반복문(for, while), 컬렉션(List,Tuple, Dictionary, Set)

# 1. for문으로 순차적 값 출력

scores = [72, 88, 95, 61] # len: 4, index range: 0~3
for score in scores:
    print(score, end=' ')

print()

greeting = 'hello python!'
for ch in greeting:
    print(ch, end=' ')

print()

# 2. for문 + 조건문

for score in scores:
    if score >= 80:
        print(score, 'PASS')
    else:
        print(score, 'RETRY')

print()

# 3. range()

for i in range(5): # 0 ~ 4
    print(i, end=' ')

print()

for i in range(1, 10): # 1 ~ 9
    print(i, end=' ')

print()

for i in range(1, 21, 2): # 1 ~ 20, step 2
    print(i, end=' ')

print()

# 4. while

count = 1
while count <= 5:
    print(count, end=' ')
    count += 1 # while 종료를 위해

print()

# 5. 리스트 합계/평균 계산

total = 0 # 합계 저장 변수
for score in scores:
    total += score # 누적, total = total + score
print(f'합계: {total}')
print(sum(scores)) # sum() 함수 사용
print(f'평균: {total / len(scores)}') # len() 함수 사용

# 6. 합격자 수 계산
pass_count = 0 # 합격자 수 저장 변수
for score in scores:
    if score >= 80:
        pass_count += 1 # 조건을 만족하면 1 증가
print(f'합격자 수: {pass_count}')

# 7. 최고점 계산
highest = scores[0] # 첫번째 수를 최고점으로
for score in scores:
    if score > highest: # 더 큰 수가 있다면
        highest = score
print(f'최고점: {highest}')
print(max(scores))

# 8. Dictionary에 이름과 점수 저장
students = { # item이 4개인 딕셔너리
    '민수': 72,
    '지연': 88,
    '준호': 95,
    '서연': 61
}
for name, score in students.items(): # item 수만큼 반복
    print(f'이름: {name}, 점수: {score}')

# 9. 학생별 등급 판정
for name, score in students.items():
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    else:
        grade = 'D'
    print(f'이름: {name}, 점수: {score}, 등급: {grade}')

# 10. 중첩 for
for i in range(2, 10): # 2 ~ 9, 각 단, outer for, 행의 의미
    for j in range(1, 10): # 1 ~ 9, 곱해지는 수, inner for, 열의 의미
        print(f'{i}*{j}={i*j}', end=' ')
    print() # 줄 바꿈

# break : 반복문내에 사용하고 가장 가까운 반복문을 즉시 빠져 나감
for i in range(2, 10):
    for j in range(1, 10):
        if i % 2 == 0: # i가 짝수라면
            break # inner for문 벗어남
        print(f'{i}*{j}={i*j}', end=' ')
    print()

# continue : 반복문내에서 continue를 만나면 하단 코드를
#            수행하지 않고 다음번 반복을 수행
for i in range(1, 11): # 1 ~ 10
    if i % 2 == 0: # i가 짝수면
        continue # 하단의 출력하지 않고 다음 반복을 수행
    print(i, end=' ')

print()

# enumerate(이터러블, 시작번호) 함수 : 요소 반복시 순서 번호 부여
scores = [95, 88, 76, 100]
for i, score in enumerate(scores, start=1):
    print(f'{i}번 요소 : {score}')

# zip(이터러블, 이터러블 ...) 함수 : 여러 이터러블 묶어서 반복
names = ['홍길동', '강감찬', '이순신']
ages = [20, 30, 40]
jobs = ['산적', '장군', '장군']
for name, age, job in zip(names, ages, jobs):
    print(f'이름: {name}, 나이: {age}, 직업: {job}')

# enumerate, zip 동시 사용
names = ['홍길동', '강감찬', '이순신']
scores = [90, 80, 70]
for i, (name, score) in enumerate(zip(names, scores), start=1):
    print(f'[{i}번] 이름: {name}, 성적: {score}')




































