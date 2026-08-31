# day5_extra.py

def printline(): # 가로줄 출력 함수
    print('-' * 9)

# 1. 왼쪽 직각삼각형
n = 5
for i in range(1, n+1): # 1 ~ 5, 줄의 수
    for j in range(i): # 별의 수
        print('*', end='')
    print()
printline()

# 2. 역직각삼각형
n = 5
for i in range(n, 0, -1): # 5 ~ 1, 줄의 수
    for j in range(i): # 별의 수
        print('*', end='')
    print()
printline()

# 3.
n = 5
for i in range(1, n+1): # 줄의 수
    for j in range(n-i): # 공백의 수
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print()
printline()

# 4. 피라미드
n = 5
for i in range(1, n + 1): # 1 ~ 5, 줄의 수
    for j in range(n - i): # 공백의 수
        print(' ', end='')
    for j in range(2 * i - 1): # 별의 수
        print('*', end='')
    print()
printline()

# 5. 역피라미드
n = 5
for i in range(1, n + 1): # 줄의 수, 1 ~ 5
    for j in range(i - 1): # 공백의 수, 0 ~ 4
        print(' ', end='')
    for j in range(2 * (n-i) + 1): # 별의 수, 9 ~ 1
        print('*', end='')
    print()
printline()

# 6. 다이아몬드
n = 5
# 위쪽
for i in range(1, n + 1): # 줄의 수 1 ~ 5
    for j in range(n - i): # 공백의 수, 4 ~ 0
        print(' ', end='')
    for j in range(2*i - 1): # 별의 수, 1 ~ 9
        print('*', end='')
    print()
# 아래쪽
for i in range(n - 1, 0, -1): # 줄의 수 4 ~ 1
    for j in range(n - i): # 공백의 수, 0 ~ 4
        print(' ', end='')
    for j in range(2 * i - 1): # 별의 수, 7 ~ 1
        print('*', end='')
    print()
printline()

# 7. 속이 빈 피라미드
n = 5
for i in range(1, n + 1): # 줄의 수, 1 ~ 5
    # 왼쪽 공백
    for j in range(n - i): # 공백의 수, 4 ~ 0
        print(' ', end='')
    for j in range(1, 2 * i): # 피라미드 내부
        if i == n: # 마지막 행은 모두 별
            print('*', end='')
        elif j == 1 or j == 2 * i - 1: # 양쪽 테두리
            print('*', end='')
        else:
            print(' ', end='') # 공백
    print()
printline()

# 8. 속이 빈 사각형
n = 5
for i in range(n): # 줄의 수 (행의 수), 0 ~ 4
    for j in range(n): # 열의 수, 0 ~ 4
        if i==0 or i==n-1 or j==0 or j==n-1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
printline()

# 9. X자
n = 9
for i in range(n): # 행의 수, 0 ~ 8
    for j in range(n): # 열의 수, 0 ~ 8
        # j == i : 왼쪽 위에서 오른쪽 아래
        # j == n - i - 1 : 오른쪽 위에서 왼쪽 아래
        if j == i or j == n - i - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
printline()

# 10. 속이 빈 모래시계
n = 5
# 위쪽
for i in range(n): # 줄의 수, 0 ~ 4
    # 왼쪽 공백
    print(' '*i, end='')
    width = 2 * (n - i) - 1 # 각 줄에서 별의 넓이, 9 ~ 1
    for j in range(width):
        if i == 0: # 첫번째 줄은 모두 별
            print('*', end='')
        elif j == 0 or j == width - 1: # 양끝 별
            print('*', end='')
        else:
            print(' ', end='') # 중간 공백
    print()
# 아래쪽
for i in range(n - 2, -1, -1): # 줄의 수, 3 ~ 0
    # 왼쪽 공백
    print(' '*i, end='')
    width = 2 * (n - i) - 1 # 각 줄에서 별의 넓이, 9 ~ 1
    for j in range(width):
        if i == 0: # 첫번째 줄은 모두 별
            print('*', end='')
        elif j == 0 or j == width - 1: # 양끝 별
            print('*', end='')
        else:
            print(' ', end='') # 중간 공백
    print()
printline()



























