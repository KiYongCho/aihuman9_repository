# day10_basic.py

import pandas as pd

# 직원 교육 데이터 딕셔너리
training_data = {
    "사번": ["E101", "E102", "E103", "E104", "E105", "E106"],
    "이름": ["김지훈", "이수빈", "박현우", "정예린", "최민석", "한서진"],
    "부서": ["개발", "기획", "영업", "개발", "기획", "영업"],
    "교육점수": [88, 92, 76, 95, 84, 81],
    "교육시간": [8, 10, 6, 12, 8, 7],
}

# 딕셔너리 > 데이터프레임
source_df = pd.DataFrame(training_data)

# 데이터프레임 > CSV 파일
source_df.to_csv('employee_training.csv', index=False, encoding='utf-8-sig')

# CSV 파일 > 데이터프레임
employee_df = pd.read_csv('employee_training.csv', encoding='utf-8-sig')

print(employee_df.head(3)) # 상위 3개 행

print(employee_df.tail(2)) # 하위 2개 행

print('행 수: ', employee_df.shape[0]) # 6

print('행 수: ', employee_df.shape[1]) # 5

#  ['사번', '이름', '부서', '교육점수', '교육시간']
print('컬럼: ', list(employee_df.columns))

print(employee_df.dtypes) # 컬럼 데이터타입

employee_df.info() # 전체 구조

score = employee_df['교육점수'] # 교육점수 컬럼 시리즈
print(f'평균: {score.mean():.2f}') # 교육점수 평균 소수 두째자리
print('최소값: ', score.min())
print('최대값: ', score.max())
print(employee_df['부서'].value_counts()) # 부서별 직원 수



































