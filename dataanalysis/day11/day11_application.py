# day11_application.py

from util.print_util import pp
import os
import pandas as pd

assets_dir = './assets'

raw_path = os.path.join(assets_dir, 'day11_training_raw.csv')
clean_path = os.path.join(assets_dir, 'day11_training_clean.csv')

training_data = { # 8행 5열
    "사번": ["E101", "E102", "E103", "E104", "E105", "E102", "E106", "E107"],
    "부서": ["개발", "기획", None, "마케팅", "개발", "기획", "개발", "마케팅"],
    "과정": ["Python", "데이터분석", "Python", "데이터분석", "AI", "데이터분석", "AI", "Python"],
    "평가점수": ["88", "92", "76", "미응시", "95", "92", "84", None],
    "강사": ["김강사", "이강사", "김강사", "이강사", None, "이강사", "박강사", "김강사"],
}

source_df = pd.DataFrame(training_data)
source_df.to_csv(raw_path, index=False, encoding="utf-8-sig")

df = pd.read_csv(raw_path, encoding="utf-8-sig")

before_df = df.copy() # 데이터프레임 복사본

rows_before = df.shape[0] # 전처리 전 행 수

missing_before = before_df.isna().sum().sum() # 전처리 전 결측치 수

duplicates_before = before_df.duplicated().sum() # 전처리 전 중복 행 수

pp(before_df.dtypes)
pp(before_df.isna().sum())
pp(duplicates_before)

# 과정이 데이터 분석인 일부 컬럼 선택
data_course_rows = df.loc[
    df['과정'] == '데이터분석', # 행 조건
    ['사번', '부서', '평가점수'] # 선택 컬럼
]
pp(data_course_rows)

# 마지막 3행, 앞 3열
last_rows = df.iloc[-3:, 0:3]
pp(last_rows)

df['평가점수'] = pd.to_numeric(df['평가점수'], errors='coerce')

# 숫자 변환 후 평가점수 결측치 개수
score_missing_after_conversion = df['평가점수'].isna().sum()
pp(score_missing_after_conversion)

score_median = df['평가점수'].median() # 평가점수 중앙값

# 평가점수 결측치를 중앙값으로
df['평가점수'] = df['평가점수'].fillna(score_median)

# 부서 컬럼의 최빈값
department_mode = df['부서'].mode()[0]

# 부서 컬럼 결측치를 최빈값으로 대체
df['부서'] = df['부서'].fillna(department_mode)

# 강사 컬럼 결측치를 '미배정'으로 대체
df['강사'] = df['강사'].fillna('미배정')

df = df.drop_duplicates() # 중복행 제거

df = df.reset_index(drop=True) # 인덱스 정리

df['평가점수'] = df['평가점수'].astype('int64') # 평가점수 정수로

# 평가점수가 85 이상인 참여 기록
high_score_rows = df.loc[
    df['평가점수'] >= 85, # 행 조건
    ['사번', '부서', '과정', '평가점수']
]
high_score_rows = high_score_rows.reset_index(drop=True)
pp(high_score_rows)

rows_after = df.shape[0] # 전처리 후 행 수
missing_after = df.isna().sum().sum() # 전처리 후 결측치 수
duplicates_after = df.duplicated().sum() # 전처리 후 중복 행 수

# 전처리 전후 비교 데이터프레임
comparison_df = pd.DataFrame({
    '점검항목': ['행 수', '전체 결측치', '중복 행'],
    '전처리전': [rows_before, missing_before, duplicates_before],
    '전처리후': [rows_after, missing_after, duplicates_after]
})
pp(comparison_df)

print(df.dtypes)

# 정제한 데이터프레임 > CSV 파일
df.to_csv(clean_path, index=False, encoding="utf-8-sig")

































