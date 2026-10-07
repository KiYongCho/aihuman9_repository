# day28_challenge.py

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from include.graph_config import set_graph

set_graph(10, 8, 13)

st.set_page_config(
    page_title = '운동 기록 대시보드',
    layout = 'wide'
)

df = pd.DataFrame(
    {
        "날짜": pd.date_range("2026-09-01", periods=10, freq="D"),
        "운동종류": [
            "걷기", "달리기", "자전거", "걷기", "달리기",
            "자전거", "걷기", "달리기", "자전거", "걷기"
        ],
        "운동시간": [
            40, 30, 60, 50, 35,
            70, 45, 25, 55, 60
        ],
        "소모칼로리": [
            160, 280, 420, 200, 320,
            490, 180, 240, 390, 230
        ]
    }
)

st.title('운동 기록/음성 메모 대시보드')

record_tab, audio_tab = st.tabs(['운동 기록', '음성 메모'])

with record_tab:

    excercises = ['전체'] + sorted(df['운동종류'].unique().tolist())

    excercise = st.selectbox('운동종류', excercises)

    filtered = df.copy()
    if excercise != '전체':
        filtered = filtered[filtered['운동종류'] == excercise]

    c1, c2, c3 = st.columns(3)

    c1.metric('기록 건수', len(filtered))

    c2.metric('총 운동시간', f'{filtered["운동시간"].sum()}분')

    c3.metric('총 소모칼로리', f'{filtered["소모칼로리"].sum()}kcal')

    st.dataframe(
        filtered,
        use_container_width=True,
        hide_index=True
    )

    chart_df = filtered.sort_values('날짜')

    fig, ax = plt.subplots()
    ax.plot(chart_df['날짜'], chart_df['소모칼로리'], marker='o')
    ax.set_title('날짜별 소모칼로리')
    ax.set_xlabel('날짜')
    ax.set_ylabel('소모칼로리')
    fig.autofmt_xdate()
    st.pyplot(fig)
    plt.close(fig)

with audio_tab:

    audio_file = st.file_uploader(
        '운동 음성 메모 WAV',
        type = ['wav']
    )

    if audio_file is None:
        st.info('WAV 음성 메모를 선택하세요.')
    else:
        size_kb = len(audio_file.getvalue()) / 1024
        c1, c2 = st.columns(2)
        c1.metric('파일명', audio_file.name)
        c2.metric('파일크기', f'{size_kb:.1f}KB')
        st.audio(audio_file, format='audio/wav')

























