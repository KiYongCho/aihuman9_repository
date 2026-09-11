# day12_application.py

from util.print_util import pp
import pandas as pd

# 지원 데이터
apply_data = {
    "applicant_id": ["A01", "A02", "A03", "A04", "A05", "A06", "A07", "A08"],
    "job_code": ["J01", "J02", "J01", "J03", "J02", "J04", "J03", "J01"],
    "result": ["합격", "불합격", "합격", "서류검토", "합격", "합격", "불합격", "불합격"],
    "score": [88, 72, 91, 81, 86, 90, 69, 77]
}

# 직무 데이터
job_data = {
    "job_code": ["J01", "J02", "J03"],
    "job_name": ["백엔드", "데이터분석", "AI서비스"],
    "team": ["플랫폼", "데이터", "AI"]
}

apply_df = pd.DataFrame(apply_data)
apply_df.info()
job_df = pd.DataFrame(job_data)
job_df.info()

# 지원 데이터를 왼쪽 기준으로 결합

merged = apply_df.merge(
    job_df,
    on = 'job_code',
    how = 'left',
    indicator = True,
    # validate = 'm:1',
    validate = 'many_to_one'
)
pp(f'[지원 데이터 결합 결과]\n{merged}')

# 결합되지 않은 직무 코드
unmatched_codes = merged.loc[
    merged['_merge'] == 'left_only', # 왼쪽에만 존재, 행 조건
    'job_code' # 열 조건
].unique() # 유일 값
pp(f'[미등록 직무 코드]\n{unmatched_codes}')

# 미등록 직무명 보완
merged['job_name'] = merged['job_name'].fillna('미등록 직무')

# 직무별 지원 통계 계산
job_summary = (
    merged.groupby('job_name') # job_name 그룹핑
    .agg(
        applicant_count = ('applicant_id', 'count'), # 지원자 수
        avg_score = ('score', 'mean'), # 평균 점수
        max_score = ('score', 'max') # 최고 점수
    )
    .reset_index()
)

job_summary['avg_score'] = job_summary['avg_score'].round(1)

# 평균 점수 내림차순 정렬
job_summary = job_summary.sort_values(
    by='avg_score',
    ascending=False,
    ignore_index=True
)

pp(f'[직무별 지원 통계]\n{job_summary}')

# 보완된 결합 결과 확인
pp(merged[['applicant_id', 'job_code', 'job_name', 'score', '_merge']])


































