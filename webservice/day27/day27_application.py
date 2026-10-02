# day27_application.py

import streamlit as st

st.set_page_config(
    page_title = '개인 지출 관리',
    layout = 'wide'
)

if 'expenses' not in st.session_state:
    st.session_state.expenses = []

st.title('개인 지출 관리')

with st.sidebar:
    month = st.selectbox(
        '조회 월',
        [f'{i}월' for i in range(1,13)]
    )

input_tab, summary_tab = st.tabs(
    ['지출 입력', '요약']
)

with input_tab:
    with st.form('expense_form'):
        item = st.text_input('항목명')
        category = st.selectbox(
            '분류',
            ['식비', '교통', '쇼핑', '기타']
        )
        amount = st.number_input(
            '금액',
            min_value=0,
            value=0,
            step=1000
        )
        submitted = st.form_submit_button('추가')
    if submitted:
        if not item.strip():
            st.warning('항목명을 입력하세요.')
        elif amount <= 0:
            st.warning('금액은 0보다 커야 합니다.')
        else:
            st.session_state.expenses.append({
                '월': month,
                '항목': item,
                '분류': category,
                '금액': amount
            })
            st.success('지출 내역을 추가했습니다.')

with summary_tab:
    selected = [
        row for row in st.session_state.expenses if row['월'] == month
    ]
    total = sum(row['금액'] for row in selected)
    left, right = st.columns(2)
    with left:
        st.metric('등록 건수', len(selected))
    with right:
        st.metric('총 지출액', f'{total:,}원')
    st.write('등록 내역')
    st.write(selected)























