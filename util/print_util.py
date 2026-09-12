# print_util.py

def pp(*args):
    print(*args)
    pl(80)

def pt(*args):
    print(type(*args))
    pl(80)

def pl(n):
    print('-' * n)

def up(n):
    print('\n' * n)
