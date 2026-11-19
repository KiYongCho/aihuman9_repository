# day54_challenge.py
# Python 재고 계산 + OpenAI API 발주 제안서

import csv
import math
import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
from day54_ex import (
    call_llm, parse_json, save_json, object_schema, array_of_strings
)
from util.print_util import pp, up

ROOT = Path(__file__).resolve().parent

# 재고 검토 보고서의 4개 필드를 기존 명칭 그대로 유지
CHALLENGE_SCHEMA = object_schema({
    'risk_items': array_of_strings(), 'estimates': array_of_strings(),
    'evidence': array_of_strings(), 'purchase_plan': array_of_strings()
})

ITEMS = [
    {"item": "키보드", "stock": 24, "daily_sales": 8},
    {"item": "마우스", "stock": 80, "daily_sales": 10},
    {"item": "모니터", "stock": 9, "daily_sales": 3},
    {"item": "웹캠", "stock": 12, "daily_sales": 0},
]

# 재고 소진 예상일을 계산하는 함수
# stock : 현재 재고 수량
# daily_sales : 하루 평균 판매 수량
# 반환값 : 재고/일판매량(일), 0개 판매 시 None
def days_left(stock, daily_sales):
    if daily_sales <= 0:
        return None  # 분모가 0이면 소진일 계산 불가
    return round(stock / daily_sales, 2)

# 품목별 계산 기준을 생성하는 함수
# items : item/stock/daily_sales 사전의 목록
# 반환값 : 검증 기준을 포함한 품목별 사전 목록
def prepare_inventory(items):
    rows = []
    for item in items:
        days = days_left(item["stock"], item["daily_sales"])
        rows.append({**item, "days_left": days})
    return rows

# 계산 데이터와 재고 정책을 API에 전달하는 함수
# client : API 클라이언트
# model : 사용 모델 ID
# rows : Python에서 계산한 결과 목록
# 반환값 : JSON 응답 dict
def write_proposal(client, model, rows):
    instructions = (
        "물류 구매 담당자. 제공된 재고 수치만 근거로 발주 검토 의견 작성. "
        "출력은 JSON 객체 하나, 키는 risk_items, estimates, "
        "evidence, purchase_plan. "
        "risk_items는 소진 예상이 5일 이하인 품목 목록. "
        "판매량 0 품목은 소진일을 추정할 수 없음을 표시. "
        "발주 수량은 실제 납기·발주 정책 정보가 없으므로 확약 금지. "
        "모든 필드의 값은 문자열 목록으로 작성."
    )
    text = "재고자료:\n" + "\n".join(str(row) for row in rows)
    raw, tokens, seconds = call_llm(
        client, model, instructions, text, schema=CHALLENGE_SCHEMA
    )
    pp("API 토큰:", tokens, "실행 시간:", seconds)
    return parse_json(raw)

def main():

    load_dotenv(ROOT / ".env")

    key = os.getenv("OPENAI_API_KEY", "").strip()

    if not key or key.startswith("sk-your-own"):
        raise SystemExit(".env 파일에 개인 API 키를 입력해야 함")

    rows = prepare_inventory(ITEMS)

    pp("Python 계산 결과:", rows)

    client = OpenAI(api_key=key, timeout=60.0, max_retries=2)

    model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

    try:
        result = write_proposal(client, model, rows)
    except Exception as exc:
        pp('재고 분석 오류:', type(exc).__name__, exc)
        save_json(ROOT / 'output' / 'challenge_inventory_error.json', {
            'error_type': type(exc).__name__, 'message': str(exc)
        })
        return

    error_path = ROOT / 'output' / 'challenge_inventory_error.json'
    if error_path.exists():
        error_path.unlink()
    save_json(ROOT / "output" / "challenge_inventory.json", {
        "reference": rows, "llm_result": result
    })

    pp("완료: 모델의 품목별 예상 소진일을 Python 값과 대조해야 함")

if __name__ == "__main__":
    main()

up(5)













