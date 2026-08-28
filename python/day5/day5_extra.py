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

# 2.

# 3.
n = 5
for i in range(1, n+1): # 줄의 수
    for j in range(n-i): # 공백의 수
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print()
printline()

# 4 ~ 7

# 8
n = 5
for i in range(n): # 줄의 수 (행의 수)
    for j in range(n): # 열의 수
        if i==0 or i==n-1 or j==0 or j==n-1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
printline()

# 9 ~ 10



























