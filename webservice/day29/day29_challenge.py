# day29_challenge.py

import psycopg
from db import get_connection, load_sql
from util.print_util import pp, up

def create_table(conn):
    with conn.cursor() as cur:
        cur.execute(load_sql('day29_challenge.sql'))

def add_run(conn, model_name, dataset_name, accuracy, epochs, memo):
    with conn.cursor() as cur:
        cur.execute(
            load_sql('day29_challenge2.sql'),
            (model_name, dataset_name, accuracy, epochs, memo)
        )
        return cur.fetchone()[0] # 등록 후 등록된 자동증가번호 리턴

def get_runs(conn):
    with conn.cursor() as cur:
        cur.execute(load_sql('day29_challenge3.sql'))
        return cur.fetchall()

def get_runs_by_accuracy(conn, min_accuracy):
    with conn.cursor() as cur:
        cur.execute(
            load_sql('day29_challenge4.sql'),
            (min_accuracy, )
        )
        return cur.fetchall()

def update_memo(conn, run_id, memo):
    with conn.cursor() as cur:
        cur.execute(
            load_sql('day29_challenge5.sql'),
            (memo, run_id)
        )
        return cur.rowcount

def delete_run(conn, run_id):
    with conn.cursor() as cur:
        cur.execute(
            load_sql('day29_challenge6.sql'),
            (run_id,)
        )
        return cur.rowcount

def main():
    try:

        with get_connection() as conn:

            create_table(conn)

            with conn.cursor() as cur:
                cur.execute(load_sql('day29_challenge7.sql'))
            conn.commit()

            pp('정상 Transaction')

            try:

                id1 = add_run(
                    conn, 'CNN', 'FashionMNIST',
                    0.9125, 15, '기본 모델'
                )

                id2 = add_run(
                    conn, 'MLP', 'FashionMNIST',
                    0.8870, 20, 'Dense 모델'
                )

                pp(f'생성 id: {id1}, {id2}')

                updated = update_memo(conn, id1, '튜닝 예정')
                pp(f'수정 Row 수: {updated}')

                conn.commit() # Transaction 완료

            except Exception as e:
                conn.rollback() # Transaction 취소
                pp(f'Transaction 취소: {e}')

            pp(get_runs(conn))

            pp('정확도 0.90 이상')
            pp(get_runs_by_accuracy(conn, 0.90))

            pp('의도적인 오류와 ROLLBACK')
            try:
                # model_name이 None이므로 예외발생되어 commit되지 않고 rollback됨
                add_run(
                    conn, None, 'Iris',
                    0.95, 10, '오류 실험'
                )
                conn.commit() # 예외 발생 없으면 commit 실행됨
            except Exception as e:
                conn.rollback() # 예외 발생하면 rollback 실행됨
                pp(f'ROLLBACK 실행: {e}')

            pp('ROLLBACK 이후 데이터')
            pp(get_runs(conn))

            pp('삭제')
            pp(f'삭제 Row 수: {delete_run(conn, id2)}')

            conn.commit()

            pp(get_runs(conn))

    except psycopg.Error as e:
        pp(f'PostgreSQL 에러: {e}')

if __name__ == '__main__':
    main()

up(5)










