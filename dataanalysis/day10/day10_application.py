# day10_application.py

import pandas as pd

# 온라인 주문데이터 딕셔너리
order_data = { # 8 X 5
    "주문번호": ["O001", "O002", "O003", "O004", "O005", "O006", "O007", "O008"],
    "채널": ["모바일", "웹", "모바일", "웹", "모바일", "앱", "앱", "웹"],
    "상품분류": ["전자기기", "생활용품", "패션", "전자기기", "생활용품", "패션", "전자기기", "패션"],
    "수량": [1, 3, 2, 1, 5, 1, 2, 3],
    "주문금액": [120000, 45000, 78000, 210000, 65000, 52000, 330000, 99000],
}

# 딕셔너리 > 데이터프레임
source_df = pd.DataFrame(order_data)

# 데이터프레임 > CSV 파일
source_df.to_csv('online_orders.csv', index=False, encoding='utf-8-sig')

# CSV 파일 > 데이터프레임
orders_df = pd.read_csv('online_orders.csv', encoding='utf-8-sig')

print(type(orders_df)) # <class 'pandas.DataFrame'>

print(orders_df)

print('shape: ', orders_df.shape) # (8, 5)

print('ndim: ', orders_df.ndim) # 2

print('size: ', orders_df.size) # 40

print('columns: ', list(orders_df.columns)) # 컬럼 리스트

print(orders_df.dtypes) # 각 컬럼 데이터 타입

# 3개 컬럼 추출한 데이터프레임
selected_df = orders_df[['주문번호', '상품분류', '주문금액']]
print(selected_df)

# 주문금액 Series
amount = orders_df['주문금액']
print(type(amount)) # <class 'pandas.Series'>

print('합계: ', amount.sum())
print('평균: ', amount.mean())
print('중앙값: ', amount.median())
print('최대: ', amount.max())
print('최소: ', amount.min())

print(orders_df.describe()) # 기초 통계

# 채널별 주문 건수
print(orders_df['채널'].value_counts())

# 상품분류 고유값 목록
print('고유값: ', orders_df['상품분류'].unique())

# 상품분류 고유값 개수
print('고유값 개수: ', orders_df['상품분류'].nunique())

# 채널, 주문금액 2개 컬럼의 데이터 프레임
channel_amount_df = pd.read_csv(
    'online_orders.csv',
    encoding='utf-8-sig',
    usecols=['채널', '주문금액']
)
print(channel_amount_df)

# 가장 많이 사용된 채널의 이름
# print(orders_df['채널'].value_counts())
top_channel = orders_df['채널'].value_counts().index[0]

# 데이터 크기를 한 줄로 요약해 출력
print(f'데이터는 {orders_df.shape[0]}행, {orders_df.shape[1]}열 입니다.')

# 주문금액 평균을 한 줄로 요약해 출력
# ,.0f : 숫자 3자리마다 콤마, 소수점 이하 없는 실수
print(f'평균 주문금액은 {amount.mean():,.0f}원 입니다.')

# 가장 많이 사용된 채널을 한 줄로 요약해 출력
print(f'가장 많이 사용된 주문 채널은 {top_channel}입니다.')













