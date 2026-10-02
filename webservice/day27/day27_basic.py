# day27_basic.py

import streamlit as st

st.title('교육과정 상담 신청')

name = st.text_input(
    '이름',
    placeholder='이름을 입력하세요.'
)

course = st.selectbox(
    '희망 과정',
    ['Python', '데이터분석', 'AI']
)

consult_time = st.radio(
    '상담 희망 시간',
    ['오전', '오후', '저녁']
)

if st.button('신청'):
    if not name.strip():
        st.warning('이름을 입력하세요.')
    else:
        st.success('상담 신청이 접수되었습니다.')
        st.write('이름: ', name)
        st.write('희망 과정: ', course)
        st.write('상담 시간: ', consult_time)

























