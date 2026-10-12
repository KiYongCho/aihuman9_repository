# day30_basic.py
# 스터디 일정 관리 웹앱

import os
import pandas as pd
import psycopg
import streamlit as st
from dotenv import load_dotenv
from psycopg.rows import dict_row

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    """환경변수의 접속정보로 PostgreSQL Connection을 생성합니다."""
    return psycopg.connect(DATABASE_URL)

def create_table():
    """스터디 일정을 저장할 테이블을 생성합니다."""
    sql = """
    CREATE TABLE IF NOT EXISTS study_schedule (
        id SERIAL PRIMARY KEY,
        subject VARCHAR(100) NOT NULL,
        study_date DATE NOT NULL,
        place VARCHAR(100) NOT NULL
    )
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)

def save_schedule(subject, study_date, place):
    """Form에서 받은 일정 정보를 DB에 저장합니다."""
    sql = """
    INSERT INTO study_schedule (subject, study_date, place)
    VALUES (%s, %s, %s)
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (subject, study_date, place))

def load_schedules():
    """일정을 날짜 오름차순으로 조회합니다."""
    sql = """
    SELECT id, subject, study_date, place
    FROM study_schedule
    ORDER BY study_date ASC, id ASC
    """
    with get_connection() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute(sql)
            return cur.fetchall()

def main():
    """일정 등록 Form과 조회 표를 구성합니다."""
    st.title("스터디 일정 관리")
    if not DATABASE_URL:
        st.error("DATABASE_URL을 설정하세요.")
        st.stop()
    try:
        create_table()
        with st.form("schedule_form", clear_on_submit=True):
            subject = st.text_input("학습 주제")
            study_date = st.date_input("학습 날짜")
            place = st.text_input("장소")
            submitted = st.form_submit_button("일정 저장")
        if submitted:
            if not subject.strip() or not place.strip():
                st.warning("학습 주제와 장소를 입력하세요.")
            else:
                save_schedule(
                    subject.strip(),
                    study_date,
                    place.strip(),
                )
                st.success("일정을 저장했습니다.")
        rows = load_schedules()
        st.dataframe(
            pd.DataFrame(rows),
            use_container_width=True,
            hide_index=True,
        )
    except psycopg.Error:
        st.error("데이터베이스 처리 중 문제가 발생했습니다.")

if __name__ == "__main__":
    main()
