# day4_challenge.py

score = int(input('점수: '))
attendance = int(intput('출석률: '))

if score < 0 or score > 100 or attendance < 0 or attendance > 100: # 범위 벗어남
    print('입력 오류')
elif score >= 90 and attendance >= 95: # 우수 합격 기준
    print('최종 판정: 우수 합격')
elif score >= 70 and attendance >= 80: # 합격 기준
    print('최종 판정: 합격')
elif attendance < 80: # 불합격, 출석 기준 미달
    print('최종 판정: 불합격 - 출석률 미달')
else: # 불합격, 출석 기준 충족, 점수 기준 미달
    print('최종 판정: 불합격 - 점수 미달')