# day3_application.py

product = input('상품명: ')
unit_price = int(input('상품 단가: '))
quantity = int(input('구매 수량: '))
discount_rate = float(input('할인율(%): '))
subtotal = unit_price * quantity # 주문 금액
discount_amount = subtotal * discount_rate / 100 # 할인 금액
final_amount = subtotal - discount_amount # 최종 결제 금액

print('='*35)
print(f'주문 금액: {subtotal:,.0f}원')
print(f'할인율: {discount_rate:,.1f}%')
print(f'할인 금액: {discount_amount:,.0f}원')
print(f'최종 결제 금액: {final_amount:,.0f}원')
print('='*35)













