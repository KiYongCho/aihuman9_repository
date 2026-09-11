# print_util.py
# 출력시 구분선과 함께 출력하는 함수
def pp(*obj):
    print(*obj)
    print('-' * 50)

def up(n):
    print('\n' * n)