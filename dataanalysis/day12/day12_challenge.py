# day12_challenge.py

from util.print_util import pp
import pandas as pd

# 활동 데이터
activity_data = { # 12행 6열
    "activity_id": ["E01", "E02", "E03", "E04", "E05", "E06", "E07", "E08", "E09", "E10", "E11", "E12"],
    "month": ["2026-01", "2026-01", "2026-01", "2026-02", "2026-02", "2026-02", "2026-03", "2026-03", "2026-03", "2026-03", "2026-02", "2026-01"],
    "course": ["Python", "AI", "Cloud", "Python", "AI", "Cloud", "Python", "AI", "Cloud", "Python", "AI", "Cloud"],
    "learner": ["민준", "서연", "지우", "민준", "하윤", "지우", "도윤", "서연", "시우", "하윤", "민준", "도윤"],
    "study_minutes": [120, 95, 80, 150, 110, 90, 130, 125, 100, 75, 140, 105],
    "completed": [1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1]
}

# 과정 데이터
course_data = { # 3행 3열
    "course": ["Python", "AI", "Cloud"],
    "category": ["Programming", "AI", "Infrastructure"],
    "instructor": ["김강사", "이강사", "박강사"]
}

activity_df = pd.DataFrame(activity_data)
course_df = pd.DataFrame(course_data)
activity_df.info()
course_df.info()

# 과정 데이터, 활동 데이터 결합
merged = activity_df.merge(
    course_df, # 결합할 데이터프레임
    on="course", # 키 컬럼
    how="left", # 결합 방식 : 왼쪽 것은 다 나오도록
    validate="many_to_one" # 왼쪽은 키값이 여러개, 오른쪽은 하나로 검증
)
pp(merged)

# 과정별 학습 활동 집계
course_summary = (
    merged.groupby("course")
    .agg(
        total_minutes = ('study_minutes', 'sum'), # 전체 학습 분 수
        avg_minutes = ('study_minutes', 'mean'), # 전체 학습 분 평균
        activity_count = ('activity_id', 'count'), # 활동 수
        completed_count = ('completed', 'count') # 완료 수
    )
    .reset_index() # 인덱스 갱신
)

course_summary['avg_minutes'] = course_summary['avg_minutes'].round(1) # 평균 분 수
course_summary['completion_rate_pct'] = ( # 완료율
    course_summary['completed_count'] / course_summary['activity_count'] * 100
).round(1)

# 완료율값으로 정렬
course_summary = course_summary.sort_values(
    'completion_rate_pct', # 정렬 기준 컬럼
    ascending=False, # 내림차순 정렬
    ignore_index=True # 인덱스 재구성
)
pp(course_summary)

# 월/과정 학습시간 피벗
study_pivot = merged.pivot_table(
    values = 'study_minutes', # 값 컬럼
    index = 'month', # 행 컬럼
    columns = 'course', # 열 컬럼
    aggfunc = 'sum', # 집계함수
    fill_value = 0, # 결측치는 0으로 채움
    margins = True, # 추가
    margins_name = 'Total' # Total이라는 이름을 추가시 사용
)
pp(study_pivot)

# 월/카테고리완료율 피벗
completion_pivot = merged.pivot_table(
    values = 'completed', # 값 컬럼
    index = 'month', # 행 컬럼
    columns = 'category', # 열 컬럼
    aggfunc = 'mean', # 집계함수
    fill_value = 0 # 결측치는 0으로 채움
)
completion_pivot = (completion_pivot * 100).round(1)
pp(completion_pivot)

# 전체 학습시간 검증
raw_total = merged['study_minutes'].sum() # 원본 학습분 합계
pivot_total = study_pivot.loc['Total', 'Total'] # 피벗 후 학습분 합계
pp(f'원본 학습분 합계: {raw_total}')
pp(f'피벗 후 학습분 합계: {pivot_total}')
pp(f'일치 여부: {raw_total == pivot_total}')
































