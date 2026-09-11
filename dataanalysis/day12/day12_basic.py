# day12_basic.py

from util.print_util import pp
import pandas as pd

# 도서관 대출 데이터
loan_data = {
    "loan_id": ["L001", "L002", "L003", "L004", "L005", "L006", "L007", "L008", "L009", "L010"],
    "branch": ["강남", "강남", "마포", "종로", "마포", "강남", "종로", "마포", "강남", "종로"],
    "category": ["IT", "경제", "IT", "문학", "경제", "IT", "IT", "문학", "문학", "경제"],
    "loan_days": [7, 14, 10, 21, 8, 12, 9, 18, 6, 15]
}
df = pd.DataFrame(loan_data)
df.info()

# 지점별 대출 현황 집계
branch_summary = (
    df.groupby('branch') # 지점 그룹핑
    .agg( # 집계
        loan_count = ('loan_id', 'count'), # 대출 수
        avg_loan_days = ('loan_days', 'mean') # 평균 대출 일수
    )
    .reset_index() # 인덱스 재구성
)

branch_summary['avg_loan_days'] = branch_summary['avg_loan_days'].round(1) # 소수점 이하 한자리

branch_summary = branch_summary.sort_values( # 값으로 정렬
    'loan_count', # 정렬 기준 컬럼
    ascending = False, # 내림차순 정렬
    ignore_index = True # 인덱스 재구성
)

pp(f'[지점별 대출 현황]\n{branch_summary}')

# 카테고리별 대출 건수
category_summary = (
    df.groupby('category', as_index = False)
    .agg(loan_count = ('loan_id', 'count'))
    .sort_values('loan_count', ascending = False, ignore_index = True)
)

pp(f'[카테고리별 대출 건수]\n{category_summary}')



































