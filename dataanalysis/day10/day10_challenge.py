# day10_challenge.py
from dataanalysis.day10.day10_ex import data_dictionary
from util.print_util import pp
import pandas as pd

# 채용 지원자 데이터 딕셔너리 (10행 6열)
applicant_data = {
    "지원ID": ["A001", "A002", "A003", "A004", "A005", "A006", "A007", "A008", "A009", "A010"],
    "지원직무": ["백엔드", "데이터분석", "프론트엔드", "AI엔지니어", "백엔드", "데이터분석", "AI엔지니어", "프론트엔드", "백엔드", "데이터분석"],
    "전공": ["컴퓨터공학", "통계학", "디자인", "전자공학", "경영학", "수학", "컴퓨터공학", "컴퓨터공학", "전자공학", "경영학"],
    "경력년수": [1, 0, 2, 1, 3, 1, 2, 0, 1, 2],
    "코딩테스트": [82, 91, 78, 94, 75, 89, 96, 84, 87, 81],
    "영어점수": [845, 910, 800, 880, 920, 870, 935, 825, 860, 905],
}

#  딕셔너리 > 데이터프레임
source_df = pd.DataFrame(applicant_data)

# 데이터프레임 > CSV 파일
source_df.to_csv('./applicants.csv', index=False, encoding='utf-8-sig')

# CSV 파일 > 데이터프레임
applicants_df = pd.read_csv('./applicants.csv', encoding='utf-8-sig')

pp(applicants_df.head()) # 처음 5개 행

pp(applicants_df.tail()) # 마지막 5개 행

pp(applicants_df.shape) # (10, 6), 행과 열의 수

pp(list(applicants_df.columns)) # 컬럼명들

pp(applicants_df.dtypes) # 컬럼 데이터타입들
pp(type(applicants_df.dtypes)) # <class 'pandas.Series'>

applicants_df.info()

# 2개 컬럼만 추출한 데이터프레임
score_df = applicants_df[['코딩테스트', '영어점수']]
pp(score_df)

pp(score_df.describe()) # 기초 통계

pp(applicants_df['지원직무'].value_counts()) # 지원직무별 지원자 수
pp(type(applicants_df['지원직무'].value_counts())) # <class 'pandas.Series'>

pp(applicants_df['전공'].unique()) # 고유 전공 배열
pp(type(applicants_df['전공'].unique())) # <class 'pandas.arrays.StringArray'>

pp(applicants_df['전공'].nunique()) # 고유 전공 수

dictionary_rows = [] # 데이터 사전의 각 행을 저장할 리스트

for column in applicants_df.columns: # 컬럼 수만큼 반복
    series = applicants_df[column] # 컬럼 > 시리즈
    dictionary_rows.append({ # 리스트에 딕셔너리(행) 추가
        '컬럼명': column,
        'dtype': str(series.dtype),
        '전체행수': len(series),
        'Non-Null개수': series.count(),
        '고유값수': series.nunique(),
        '첫번째예시값': series.iloc[0] # 시리즈에서 0번 인덱스 값
    })

# 리스트 > 딕셔너리
data_dictionary = pd.DataFrame(dictionary_rows)
pp(data_dictionary)

# 데이터 사전 > CSV 파일
data_dictionary.to_csv(
    './applicants_data_dictionary.csv',
    index=False,
    encoding='utf-8-sig'
)

applicant_count = applicants_df.shape[0] # 전체 지원자 수 = 행의 수
column_count = applicants_df.shape[1] # 열의 수
job_type_count = applicants_df['지원직무'].nunique() # 지원직무 종류 수
coding_average = applicants_df['코딩테스트'].mean() # 코딩테스트 평균

pp('전체 지원자 수', applicant_count)
pp('전체 컬럼 수', column_count)
pp('지원직무 종류 수', job_type_count)
pp('코딩테스트 평균', coding_average)

pp('현재 단계에서는 데이터 구조와 통계만 확인했으며, 정제 작업은 수행하지 않았다.')













































