# day14_basic.py
# 도서관 대출 현황 시각화

import platform
import pandas as pd
import matplotlib.pyplot as plt

# 1. 그래프 기본 설정
if platform.system() == "Windows":
    plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

# 2. DataFrame 생성
df = pd.DataFrame({
    "월": ["1월", "2월", "3월", "4월", "5월", "6월"],
    "소설": [120, 135, 128, 150, 164, 172],
    "IT": [80, 95, 110, 118, 125, 140],
    "경제": [65, 72, 78, 85, 92, 98]
})

# 3. 월별 전체 대출 건수 계산
df["전체"] = df[["소설", "IT", "경제"]].sum(axis=1)

# 4. 월별 전체 대출 선그래프
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(df["월"], df["전체"], marker="o", linewidth=2)
ax.set_title("월별 전체 대출 건수")
ax.set_xlabel("월")
ax.set_ylabel("대출 건수")
ax.grid(alpha=0.3)
fig.tight_layout()
plt.show()

# 5. 장르별 총대출 건수 계산
genre_total = df[["소설", "IT", "경제"]].sum().sort_values(ascending=False)

# 6. 장르별 총대출 막대그래프
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(genre_total.index, genre_total.values)
ax.set_title("장르별 6개월 총대출 건수")
ax.set_xlabel("장르")
ax.set_ylabel("대출 건수")
ax.bar_label(bars, fmt="%.0f")
fig.tight_layout()
plt.show()

# 7. 관찰 결과 출력
print("월별 전체 대출 건수는 전반적으로 증가하는 흐름을 보입니다.")
print(f"6개월 총대출 건수가 가장 많은 장르는 {genre_total.index[0]}입니다.")


