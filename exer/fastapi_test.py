# fastapi_test.py

# 설치 : python -m pip install "fastapi[standard]" httpx pytest
# 설치 버젼 확인 : python -m pip show fastapi pydantic uvicorn (기본 8000번 포트로 서버 실행됨)

# 실행 : python -m uvicorn fastapi_test:app --reload
#       코드 수정시 서버를 자동 재시작하는 --reload 옵션은 개발시에만 사용
# 포트 변경 실행 : python -m uvicorn main:app --host 127.0.0.1 --port 변경할포트번호 --reload

# 서버 실행 후 아래 URL 확인
# http://127.0.0.1:8000/doc (Swagger UI)
# http://127.0.0.1:8000/redoc (ReDoc)
# http://127.0.0.1:8000/openapi.json (JSON 형태의 API)

from typing import Annotated
from fastapi import FastAPI, Header, Query, Path, status
from pydantic import BaseModel, Field, field_validator
from enum import Enum

app = FastAPI(title='AI Human API', version='1.0.0')

@app.get('/')
def home():
    return {'service': 'ai-human', 'status': 'ok'}

@app.get('/health')
def health():
    return {'health': True}

@app.get("/books/{book_id}")
def get_book(
    book_id: int,
    q: Annotated[str | None, Query(max_length=40)] = None, # Annotated: 값의 자료형과 검증 조건을 함께 표기
    x_client_id: Annotated[str | None, Header()] = None
):
    return {"book_id": book_id, "q": q, "client": x_client_id}

@app.get("/users/me")
def my_profile():
    return {"name": "demo"}

@app.get("/users/{user_id}")
def read_user(user_id: Annotated[int, Path(ge=1)]): # 1이상 정수
    return {"user_id": user_id}

# BaseModel(기본 데이터 모델 클래스)를 상속받은 데이터 모델 클래스
# Pydantic은 Python 데이터 모델의 입력 값과 타입을 검증 및 변환
class ProductCreate(BaseModel):
    name: str = Field(min_length=2, max_length=80)
    price: int = Field(ge=0, description="원 단위 가격")
    # default_factory=list: 요청 객체마다 독립적인 기본 리스트를 생성
    tags: list[str] = Field(default_factory=list)

example = ProductCreate(name="키보드", price=49000)

print(example.model_dump()) # 파이썬 객체 > 딕셔너리
print(example.model_dump_json()) # 파이썬 객체 > JSON문자열

# 문자열 값을 갖는 2개의 멤버(NORMAL, HIGH)를 정의한 열거형 클래스
# FastAPI에서는 Enum을 활용해 API 파라미터에 입력할 수 있는 값을 제한
class Priority(str, Enum):
    NORMAL = "normal"
    HIGH = "high"

class Job(BaseModel):
    title: str = Field(min_length=2)
    priority: Priority = Priority.NORMAL # Priority Enum 타입
    keywords: list[str] = Field(default_factory=list)
    # @field_validator("title"): Pydantic 모델의 title 필드를 검증할 함수로 등록
    # @classmethod:	함수를 인스턴스 메서드가 아닌 클래스 메서드로 정의
    @field_validator("title")
    @classmethod
    def clean_title(cls, value: str) -> str: # cls는 클래스 메서드에서 클래스 자신
        value = value.strip()
        if not value:
            raise ValueError("제목은 공백일 수 없습니다")
        return value


items: dict[int, dict] = {} # 키가 정수이고 값이 딕셔너리인 딕셔너리

class ItemIn(BaseModel):
    name: str = Field(min_length=1)
    price: int = Field(ge=0)

@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(item: ItemIn):
    new_id = len(items) + 1  # 실습용이며 운영에서는 DB 사용
    items[new_id] = {"id": new_id, **item.model_dump()}
    return items[new_id]















