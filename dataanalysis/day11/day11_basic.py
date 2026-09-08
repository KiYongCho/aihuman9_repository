# day11_basic.py

from util.print_util import pp
import os
import pandas as pd

assets_dir = './assets'

csv_path = os.path.join(assets_dir, 'day11_library_raw.csv')

library_data = { # 7행 5열
    "대출ID": ["L001", "L002", "L003", "L004", "L005", "L002", "L006"],
    "도서분류": ["IT", "경제", "문학", "IT", "과학", "경제", "문학"],
    "대출일수": ["7", "14", "10", "unknown", "21", "14", "7"],
    "연체일수": [0, 3, 0, 2, 5, 3, 0],
    "회원등급": ["일반", "우수", None, "일반", "우수", "우수", "일반"],
}

source_df = pd.DataFrame(library_data) # 딕셔너리 > 데이터프레임

source_df.to_csv(csv_path, index=False, encoding='utf-8-sig') # 데이터프레임 > CSV 파일

df = pd.read_csv(csv_path, encoding='utf-8-sig') # CSV 파일 > 데이터프레임

pp(df.head()) # 상위 5행 출력
pp(df.shape) # (7, 5)
pp(df.dtypes) # 컬럼 타입

# 연체일수가 1일 이상인 행에서 필요한 컬럼
overdue_rows = df.loc[
    df['연체일수'] >= 1, # 행 조건
    ['대출ID', '도서분류', '연체일수'] # 필요한 컬럼
]
pp(overdue_rows)

# 앞 4행, 앞 3열
position_rows = df.iloc[0:4, 0: 3]
pp(position_rows)

pp(df.isna().sum()) # 컬럼별 결측치

duplicate_count = df.duplicated().sum() # 전체 중복 행 수
pp(duplicate_count)

# 대출일수 숫자로 변환, 변환불가시는 NaN
df['대출일수'] = pd.to_numeric(df['대출일수'], errors='coerce')

loan_days_median = df['대출일수'].median() # 대출일수 중앙값

# 대출일수 결측치를 중앙값 대체
df['대출일수'] = df['대출일수'].fillna(loan_days_median)

# 회원등급 결측치를 '일반' 대체
df['회원등급'] = df['회원등급'].fillna('일반')

df = df.drop_duplicates() # 중복 행 제거

df = df.reset_index(drop=True) # 기존 인덱스 제거 후 인덱스 0부터 리셋

df['대출일수'] = df['대출일수'].astype('int64') # 대출일수 정수로 변환

pp(df) # 전처리 완료 데이터
pp(df.shape) # 전처리 후 shape
pp(df.isna().sum()) # 전처리 후 결측치 개수
pp(df.duplicated().sum()) # 전처리 후 중복 행 수
pp(df.dtypes) # 전처리 후 데이터 타입



































