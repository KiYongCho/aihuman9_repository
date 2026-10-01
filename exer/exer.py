import streamlit as st

st.title('title')
st.header('header')
st.subheader('subheader')
st.write('write')
st.markdown('# 대제목')
st.markdown('## 중제목')
st.success('success')
st.error('error')

name = st.text_input('이름', placeholder='이름을 입력하세요!')
if name.strip():
    st.write(f'니 이름은 {name}이구나')

age = st.number_input(
    '나이',
    min_value=0,
    max_value=150,
    value=20,
    step=1
)
if age > 0:
    st.write(f'니 나이는 {age}이구나!')

model = st.selectbox(
    '모델',
    ['기본 모델', '개선 모델']
)
if model:
    st.write(f'니가 선택한건 {model}')

sex = st.radio(
    '성별',
    ['남성', '여성']
)
if sex:
    st.write(f'성별은 {sex}')

hobby = st.checkbox(
    '취미',
    ['공부', '음악감상', '운동']
)

# st.help(st.checkbox)

if st.button('확인'):
    st.success('확인버튼 누름!')

if 'count' not in st.session_state:
    st.session_state.count = 0

if st.button('증가'):
    st.session_state.count += 1

st.write('현재 값: ', st.session_state.count)

with st.sidebar:
    st.header('설정')
    model = st.selectbox(
        '모델',
        ['Model A', 'Model B']
    )

left, right = st.columns([3,1])

st.markdown("""
<style>

/* 왼쪽 컨테이너 */
.st-key-left_box {
    border: 2px solid #4A90E2;
    border-radius: 12px;
    padding: 20px;
    background-color: #f8fbff;
}

/* 오른쪽 컨테이너 */
.st-key-right_box {
    border: 2px solid #2E8B57;
    border-radius: 12px;
    padding: 20px;
    background-color: #f7fff9;
}

/* 왼쪽 컨테이너 내부 제목 */
.st-key-left_box h3 {
    color: #1f5f99;
}

/* 오른쪽 컨테이너 내부 제목 */
.st-key-right_box h3 {
    color: #257346;
}

</style>
""", unsafe_allow_html=True)

with left:
    with st.container(border=True, key='left_box'):
        st.write(model)
        st.subheader('입력')
        text = st.text_input('문장')

with right:
    with st.container(border=True, key='right_box'):
        st.subheader('결과')
        st.write(text)

tab1, tab2 = st.tabs(['서비스', '사용 안내'])

with tab1:
    st.write('AI 서비스 화면')

with tab2:
    st.write('사용 방법')

def reset_form():
    st.session_state.age = 0
    st.session_state.score = 50

with st.form(
        key="predict_form",
        clear_on_submit=True
    ):
    age = st.number_input("나이", 0, 120)
    score = st.slider("점수", 0, 100, 50)
    submitted = st.form_submit_button(
        "예측",
        type="primary",
        use_container_width=True
    )
    reset = st.form_submit_button(
        "초기화",
        on_click=reset_form,
        use_container_width=True
    )
if submitted:
    st.write(age, score)

