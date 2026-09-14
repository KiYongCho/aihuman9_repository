# day15_basic.py
# 공공도서관 대출 데이터 EDA

from pathlib import Path
import platform
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from util.print_util import pp, up

DATA_FILE = Path(__file__).parent / 'assets' / 'day15_basic_data.csv'

sns.set_theme(style="whitegrid")

if platform.system() == "Windows":
    plt.rcParams["font.family"] = "Malgun Gothic"
elif platform.system() == "Darwin":
    plt.rcParams["font.family"] = "AppleGothic"
plt.rcParams["axes.unicode_minus"] = False

# 1. 데이터 점검
df = pd.read_csv(DATA_FILE, encoding="utf-8-sig")
pp("[크기]", df.shape)
pp("[자료형]\n", df.dtypes)
pp("[결측치]\n", df.isna().sum())
pp("[중복 행]", df.duplicated().sum())
pp("[대출ID 중복]", df.duplicated(subset="대출ID").sum())

# 2. 문자열 표준화
clean_df = df.copy()
clean_df["장르"] = clean_df["장르"].astype("string").str.strip().replace({"fiction": "소설"})
clean_df["대출상태"] = clean_df["대출상태"].astype("string").str.strip().replace({"반납완료": "반납"})

# 3. 날짜·수치형 변환
clean_df["대출일"] = pd.to_datetime(clean_df["대출일"], errors="coerce")
clean_df["대출일수"] = pd.to_numeric(clean_df["대출일수"], errors="coerce")
clean_df = clean_df.dropna(subset=["대출일"])
clean_df["대출일수"] = clean_df["대출일수"].fillna(clean_df["대출일수"].median())

# 4. 중복 제거
clean_df = clean_df.drop_duplicates(subset="대출ID", keep="last")

# 5. KPI 계산
total_loans = len(clean_df)
avg_days = clean_df["대출일수"].mean()
return_rate = clean_df["대출상태"].eq("반납").mean() * 100
pp("\n[KPI]")
pp(f"전체 대출 건수: {total_loans}건")
pp(f"평균 대출일수: {avg_days:.1f}일")
pp(f"반납 완료율: {return_rate:.1f}%")

# 6. 장르별 요약
summary = (
    clean_df.groupby("장르")
    .agg(대출건수=("대출ID", "count"), 평균대출일수=("대출일수", "mean"))
    .sort_values("대출건수", ascending=False)
)
pp("\n[장르별 요약]\n", summary.round(2))

# 7. 장르별 대출 건수
plot_df = summary.reset_index()
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=plot_df, x="장르", y="대출건수", color="C0", ax=ax)
ax.set_title("장르별 대출 건수")
ax.set_ylabel("건수")
plt.tight_layout()
plt.show()

# 8. 대출일수 분포
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(data=clean_df, x="대출일수", bins=8, color="C0", ax=ax)
ax.set_title("대출일수 분포")
ax.set_xlabel("대출일수")
plt.tight_layout()
plt.show()

# 9. 인사이트
top_genre = summary["대출건수"].idxmax()
long_genre = summary["평균대출일수"].idxmax()
pp("\n[인사이트]")
pp(f"1. 대출 건수가 가장 많은 장르는 '{top_genre}'입니다.")
pp(f"2. 평균 대출일수가 가장 긴 장르는 '{long_genre}'입니다.")
pp("3. 장르별 대출기간 차이의 원인을 확인하려면 연령대·예약대기·도서별 보유권수 데이터를 추가로 확인할 필요가 있습니다.")

up(5)











