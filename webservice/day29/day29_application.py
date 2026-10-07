# day29_application.py

import psycopg
from db import get_connection, load_sql
from util.print_util import pp, up

def create_table(conn):
    with conn.cursor() as cur:
        cur.execute(load_sql('day29_application.sql'))

def add_job(conn, company, position, location, salary, status):
    with conn.cursor() as cur:
        cur.execute(
            load_sql('day29_application2.sql'),
            (company, position, location, salary, status)
        )

def get_jobs(conn):
    with conn.cursor() as cur:
        cur.execute(load_sql('day29_application3.sql'))
        return cur.fetchall()

def get_jobs_by_location(conn, location):
    with conn.cursor() as cur:
        cur.execute(load_sql('day29_application4.sql'),
            (location,)
        )
        return cur.fetchall()

def update_salary(conn, job_id, salary):
    with conn.cursor() as cur:
        cur.execute(
            load_sql('day29_application5.sql'),
            (salary, job_id)
        )
        return cur.rowcount

def delete_job(conn, job_id):
    with conn.cursor() as cur:
        cur.execute(
            load_sql('day29_application6.sql'),
            (job_id,)
        )
        return cur.rowcount

def main():
    try:

        with get_connection() as conn:

            create_table(conn)

            with conn.cursor() as cur:
                cur.execute(load_sql('day29_application7.sql'))

            add_job(
                conn, "ABC Tech", "AI Engineer",
                "서울", 4800, "모집중"
            )

            add_job(
                conn, "Data Lab", "Data Analyst",
                "부산", 4200, "모집중"
            )

            add_job(
                conn, "Cloud Works", "Backend Developer",
                "서울", 4500, "마감"
            )

            conn.commit()

            pp("전체 공고")
            pp(get_jobs(conn))

            pp("서울 공고")
            pp(get_jobs_by_location(conn, "서울"))

            pp("연봉 수정")
            pp(f"수정 Row 수: {update_salary(conn, 1, 5100)}")
            conn.commit()

            pp("공고 삭제")
            pp(f"삭제 Row 수: {delete_job(conn, 3)}")
            conn.commit()

            pp(get_jobs(conn))

    except psycopg.Error as e:
        pp(f"DB 오류: {e}")

if __name__ == "__main__":
    main()

up(5)