# day29_basic.py

import psycopg
from db import get_connection, load_sql
from util.print_util import pp, up

def main():
    try:

        with get_connection() as conn:
            with conn.cursor() as cur:

                sql = load_sql('day29_basic.sql')
                cur.execute(sql)

                sql = load_sql('day29_basic2.sql')
                cur.execute(sql)

                books = [
                    ('데이터 분석 입문', '김데이터', 3),
                    ('파이썬 웹서비스', '이파이썬', 1),
                    ('AI 프로젝트', '박에이아이', 5)
                ]
                sql = load_sql('day29_basic3.sql')
                cur.executemany(sql, books)
                conn.commit()

                pp('전체 도서')
                sql = load_sql('day29_basic4.sql')
                cur.execute(sql)
                pp(cur.fetchall())

                pp('재고 2권 이상')
                sql = load_sql('day29_basic5.sql')
                cur.execute(sql, (2,))
                pp(cur.fetchall())

                pp('재고 수정')
                cur.execute(load_sql('day29_basic6.sql'), (4, 2))
                pp(f'수정 Row 수: {cur.rowcount}')
                conn.commit()

                pp('도서 삭제')
                cur.execute(load_sql('day29_basic7.sql'), (1,))
                pp(f'삭제 Row 수: {cur.rowcount}')
                conn.commit()

                cur.execute(load_sql('day29_basic4.sql'))
                pp(cur.fetchall())

    except psycopg.Error as e:
        pp(f'DB오류: {e}')

if __name__ == '__main__':
    main()

up(5)





































