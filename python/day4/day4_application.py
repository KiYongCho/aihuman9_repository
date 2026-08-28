# day4_application.py

score = int(input('점수: '))

if score < 0 or score > 100: # 점수가 0~100 범위 벗어남
    print('입력 오류')
elif score >= 90:
    print('등급: A')
elif score >= 80:
    print('등급: B')
elif score >= 70:
    print('등급: C')
elif score >= 60:
    print('등급: D')
else:
    print('등급: F')