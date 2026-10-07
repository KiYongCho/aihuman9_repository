# day28_application.py

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from include.graph_config import set_graph

set_graph(10, 8, 13)

st.set_page_config(
    page_title = '온라인 쇼핑 주문 대시보드',
    layout = 'wide'
)

df = pd.DataFrame(
    {
        "주문일": pd.date_range("2026-09-01", periods=12, freq="D"),
        "카테고리": [
            "전자기기", "식품", "도서", "생활", "전자기기", "식품",
            "도서", "생활", "전자기기", "식품", "도서", "생활"
        ],
        "주문금액": [
            120000, 35000, 28000, 54000, 85000, 42000,
            31000, 67000, 210000, 29000, 45000, 72000
        ],
        "주문수량": [
            1, 3, 2, 2, 1, 4,
            2, 3, 1, 2, 3, 2
        ]
    }
)

st.title('온라인 쇼핑 주문 대시보드')

with st.sidebar:
    categories = ['전체'] + sorted(df['카테고리'].unique().tolist())
    category = st.selectbox('카테고리', categories)

filtered = df.copy()
if category != '전체':
    filtered = filtered[filtered['카테고리'] == category]

c1, c2, c3 = st.columns(3)

c1.metric('주문 건수', len(filtered))

c2.metric('총 주문금액', f'{filtered["주문금액"].sum():,}원')

c3.metric('총 주문수량', f'{filtered["주문수량"].sum():,}개')

st.subheader('주문 목록')

st.dataframe(
    filtered,
    use_container_width=True,
    hide_index=True
)

st.subheader('카테고리별 총 주문 금액')

summary = (
    filtered.groupby('카테고리')['주문금액'].sum().sort_values(ascending=False)
)

fig, ax = plt.subplots()
ax.bar(summary.index, summary.values)
ax.set_title('카테고리별 총 주문금액')
ax.set_xlabel('카테고리')
ax.set_ylabel('주문금액')
st.pyplot(fig)
plt.close(fig)





























