# day4_extra.py

# 1. 이름 입력 여부 확인
name = input('이름: ')
if name: # 입력받은 문자가 있으면 True (Truthy)
    print('이름 입력 완료')
else:
    print('이름 없음')

# 2. 회원등급 확인
# grade = input('회원등급(NORMAL/GOLD/VIP): ')
# if grade in ['NORMAL', 'GOLD', 'VIP']:
#     print('정상 등급')
# else:
#     print('입력 오류')

# 3. 홀수 / 짝수 판정
# number = int(input('정수: '))
# if number % 2 == 0:
#     print('짝수')
# else:
#     print('홀수')

# 4. 오전 / 오후 판정
# hour = int(input('시간(0~23): '))
# if hour < 0 or hour > 23: # 범위 확인
#     print('입력 오류')
# elif hour < 12:
#     print('AM')
# else:
#     print('PM')

# 5. 계절 판정
# month = int(input('월(1~12): '))
# if month in [12, 1, 2]:
#     print('겨울')
# elif month in [3, 4, 5]:
#     print('봄')
# elif month in [6, 7, 8]:
#     print('여름')
# elif month in [9, 10, 11]:
#     print('가을')
# else:
#     print('입력 오류')

# 6. 배송비 판정
# price = int(input('구매 금액: '))
# grade = input('회원등급(NORMAL/GOLD/VIP): ')
# if grade not in ['NORMAL', 'GOLD', 'VIP']:
#     print('입력 오류')
# elif price >= 50000 or grade in ['GOLD', 'VIP'] and price >= 30000: # 우수회원 조건
#     print('무료 배송')
# else:
#     print('배송비: 3,000원')

# 7. 장학금 대상 판정
# score = float(input('평균 점수: '))
# attendance = float(input('출석률: '))
# if score >= 95 and attendance >= 85: # 우수 장학금 조건
#     print('우수 장학금 대상')
# elif score >= 85 and attendance >= 90: # 일반 장학금 조건
#     print('일반 장학금 대상')
# else:
#     print('대상 아님')

# 8. 직원 성과등급 판정
# score = int(input('성과 점수: '))
# late = int(input('지각 회수: '))
# if score < 0 or score > 100 or late < 0: # 입력값 검증 조건
#     print('입력 오류')
# elif score >= 90 and late == 0: # S등급 조건
#     print('성과등급: S')
# elif score >= 80 and late <= 2: # A등급 조건
#     print('성과등급: A')
# elif score >= 70 and late <= 4: # B등급 조건
#     print('성과등급: B')
# else:
#     print('성과등급: C')

# 9. ATM 출금 검증
# balance = int(input('현재 잔액: '))
# amount = int(input('출금 금액: '))
# if amount <= 0:
#     print('잘못된 금액')
# elif amount % 10000 != 0: # 만원 단위가 아니라면
#     print('만원 단위로 입력')
# elif amount > balance: # 출금 금액이 현재 잔액보다 크면
#     print('잔액 부족')
# else:
#     balance = balance - amount # 출금 후 잔액 저장
#     print(f'출금 후 잔액: {balance}원') # 잔액 출력

# 10. 쇼핑몰 할인 계산
# price = int(input('구매 금액: '))
# grade = input('회원등급(NORMAL/GOLD/VIP): ')
# coupon = input('쿠폰보유(Y/N): ')
# if price <= 0 or grade not in ['NORMAL', 'GOLD', 'VIP'] or coupon not in ['Y', 'N']:
#     print('입력 오류')
# else:
#     if price >= 100000 and grade == 'VIP': # 20% 할인 조건
#         discount_rate = 0.20
#     elif coupon == 'Y' and price >= 50000: # 15% 할인 조건
#         discount_rate = 0.15
#     elif grade in ['GOLD', 'VIP'] and price >= 30000: # 10% 할인 조건
#         discount_rate = 0.10
#     elif price >= 30000: # 5% 할인 조건
#         discount_rate = 0.05
#     else: # 할인 비대상
#         discount_rate = 0.0
#
#     discount_price = int(price * discount_rate) # 할인 금액
#     final_price = price - discount_price # 최종 결제 금액
#
#     print(f'할인율: {discount_rate*100:0.f}%') # 할인율
#     print(f'할인금액: {discount_price:,}') # 할인 금액
#     print(f'최종 결제 금액: {final_price:,}원') # 최종 결제 금액





















