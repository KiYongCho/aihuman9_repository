# day55_ex1.py
# HTTP 요청과 라우팅: FastAPI앱 생성 > GET > Path> Query > POST > 응답상태코드 > Swagger UI

# 설치: python -m pip install fastapi[standard] pydantic httpx
# 실행: python -m uvicorn day55_ex1:app --reload (--reload는 코드 변경 시 재시작, 개발 전용 옵션)
# Swagger UI: http://127.0.0.1:8000/docs
# ReDoc: http://127.0.0.1:8000/redoc

from fastapi import FastAPI, HTTPException, Query, status
from pydantic import BaseModel, Field
from typing import Literal
from util.print_util import pp, up

# FastAPI 앱 생성
app = FastAPI(
    title='FastAPI 실습', # 앱 제목
    description='FastAPI 실습 입니다.', # 앱 설명
    version='0.0.1' # 앱 버젼
)

# @app.get(경로, 태그): 해당 경로에 접속하면 GET요청을 서버에 전송 (데코레이터)
# 함수명은 임의로 정하면 됨, 함수는 딕셔너리를 리턴하고 딕셔너리는 JSON문자열로 직렬화된 후에
# 요청한 클라이언트에 전송됨
@app.get('/', tags=['시작'])
def home():
    return {'message': 'FastAPI 실습'}

@app.get('/health')
def health():
    return {'status': 'ok'}

@app.get('/jobs/{job_id}') # Path 파라미터
def get_job(job_id: str): # Type Hint: 변수의 타입을 안내
    return {'job_id': job_id}

@app.get('/jobs')
# Query 파라미터, 기본값 10, 1보다 크거나 같고, 100보다 작거나 같다
# http://127.0.0.1:8000/jobs?limit=5 호출
def list_jobs(limit: int = Query(10, ge=1, le=100)):
    return {'limit': limit}

@app.get('/languages', tags=['기본 라우팅'])
# Python 딕셔너리 = JSON 객체, Python 리스트 = JSON 배열
def languages():
    # 전체는 JSON객체로, languages는 JSON 배열로 직렬화
    return {'languages': ['한국어', '영어', '일본어']}

# 두 개의 Path 파라미터를 동시에 전달
@app.get('/classes/{subject}/students/{student_id}')
# http://127.0.0.1:8000/classes/mathmatics/students/10 호출
def red_student(subject: str, student_id: int):
    return {'subject': subject, 'student_id': student_id}

# Query 파라미터에서 URL의 ? 뒤에서 선택 조건 전송
@app.get('/search')
# Python의 None = JSON에서는 null
# Python의 True/False = JSON에서는 true/false
def search(
    keyword: str | None = None, # 문자열이거나 None, 기본값은 None, 선택 파라미터
    limit: int = Query(default=5, ge=1, le=10), # 기본값 5, 1보다 크거나 같고 10보다 작거나 같다
    is_search: bool = Query(default=False)
):
    return {'keyword': keyword, 'limit': limit, 'is_search': is_search}

# BaseModel을 상속받은 데이터 모델 클래스
class VoiceRequest(BaseModel):
    # 최소 길이 2, 최대 길이 60
    title: str = Field(min_length=2, max_length=60)
    # 0보다 크거나 같은 정수
    media_seq: int = Field(gt=0)
    space_seq: int = Field(gt=0)
    # ko나 en이나 ja 중 하나
    target_language: Literal['ko', 'en', 'ja']

# JSON 요청 본문 수신
# BaseModel: POST 요청 JSON의 필드와 자료형을 정의하는 Pydantic 모델 클래스
# Field: 문자열 길이, 숫자 범위 등 입력 규칙을 설정
class MessageIn(BaseModel):
    sender: str = Field(min_length=1, description='메시지를 보낸 사람')
    text: str = Field(min_length=1, max_length=100)

@app.post('/messages', status_code=status.HTTP_201_CREATED)
def create_message(message: MessageIn): # message변수의 타입은 요청 모델
    data = message.model_dump() # Pydantic모델 > 딕셔너리
    return {'message': '메시지 접수 완료', 'data': data}

books: dict[int, dict] = {
    1: {'id': 1, 'title': '파이썬 입문', 'author': '김개발'},
    2: {'id': 2, 'title': '웹API 이해', 'author': '이코딩'}
}
next_book_id = 3

@app.get('/books') # Path 파라미터 없이 호출
def list_books():
    return {'count': len(books), 'books': list(books.values())}

@app.get('/books/{book_id}') # Path 파라미터 지정해서 호출
def get_book(book_id: int):
    if book_id not in books: # books 딕셔너리에 book_id 키가 없다면
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='도서가 없습니다.')
    return books[book_id]

# POST 입력용 모델
class BookIn(BaseModel):
    title: str = Field(min_length=1, max_length=80)
    author: str = Field(min_length=1, max_length=40)

@app.post('/books', status_code=status.HTTP_201_CREATED)
def add_book(book: BookIn):
    global next_book_id # 전역변수 사용
    # id, title, author 키로된 딕셔너리
    new_book = {'id': next_book_id, **book.model_dump()}
    books[next_book_id] = new_book # 새로운 book 추가
    next_book_id += 1
    return new_book

up(5)

































