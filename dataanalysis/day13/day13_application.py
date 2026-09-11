# day13_application.py

from util.print_util import pp, up
import pandas as pd

# 온라인 강의 이용로그 데이터 준비
df = pd.DataFrame({
    "학습자ID": [" S001 ", "S002", " s003", "S004 ", "S005", "s006", "S007", "S008"],
    "강의명": [" Python Data ", "PYTHON DATA", "python  data", "LLM Basic", "llm basic ", "Prompt", "PROMPT ", "prompt"],
    "접속일": ["2026-08-01", "2026/08/02", "2026-08-03", "2026-08-04", "error", "2026/08/06", "2026-08-07", "2026-08-08"],
    "접속기기": ["PC", "mobile", "Mobile", "pc", "TABLET", "tablet", "PC", "mobile"],
    "시청분": [42, 58, 35, 70, 63, 51, 47, 720],
    "진도율": [35, 48, 62, 77, 85, 91, 100, 56]
})

# 식별자와 강의명 정제
df["학습자ID"] = df["학습자ID"].str.strip().str.upper()
df["강의명"] = (
    df["강의명"]
    .str.strip()
    .str.lower()
    .str.replace(r"\s+", " ", regex=True)
)
df["접속기기"] = df["접속기기"].str.strip().str.lower()

# 날짜 변환과 날짜 파생 변수 생성
df["접속일"] = pd.to_datetime(df["접속일"], errors="coerce", format="mixed")
df["접속월"] = df["접속일"].dt.month
df["접속요일"] = df["접속일"].dt.day_name()
df["접속연월"] = df["접속일"].dt.strftime("%Y-%m")

# 접속기기 범주형 변환
df["접속기기"] = df["접속기기"].astype("category")

# 진도율을 구간 범주로 변환
df["진도단계"] = pd.cut(
    df["진도율"],
    bins=[0, 49, 74, 99, 100], # 4개 구간
    labels=["시작", "진행", "마무리", "완료"], # 구간 레이블
    include_lowest=True # 하한값 포함
)
progress_order = ["시작", "진행", "마무리", "완료"] # 순서로 사용할 리스트
# 순서가 있는 범주형 타입 생성
progress_type = pd.CategoricalDtype(
    categories=progress_order, # 카테고리로 사용할 리스트
    ordered=True # 순서 있음
)
# 진도단계를 순서가 있는 범주형 타입으로
df["진도단계"] = df["진도단계"].astype(progress_type)

# 시청분 IQR 경계 계산
q1 = df["시청분"].quantile(0.25)
q3 = df["시청분"].quantile(0.75)
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

# 이상치 표시와 보정값 생성
df["시청분_이상"] = ~df["시청분"].between(lower, upper)
df["시청분_보정"] = df["시청분"].clip(lower=lower, upper=upper) # 하한, 상한 잘라냄

# 전처리 결과 확인
pp("날짜 변환 실패 건수:", df["접속일"].isna().sum())
pp("강의명 고유값:", sorted(df["강의명"].unique()))
pp("접속기기 범주:", list(df["접속기기"].cat.categories))
pp("\n[진도단계별 건수]")
pp(df["진도단계"].value_counts(sort=False))
pp("\n이상치 후보 수:", int(df["시청분_이상"].sum()))
pp(f"IQR 하한={lower:.2f}, 상한={upper:.2f}")
pp("\n[시청분 원본/보정 비교]")
pp(df[["학습자ID", "시청분", "시청분_보정", "시청분_이상"]])
