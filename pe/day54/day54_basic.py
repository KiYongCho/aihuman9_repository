# day54_basic.py
# 예약 변경 문의를 실제 OpenAI API로 구조화

import json
import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
from day54_ex import call_llm, parse_json, save_json, object_schema
from util.print_util import pp, up

ROOT = Path(__file__).resolve().parent

# 기존 결과 필드의 자료형과 허용값을 강제
BASIC_SCHEMA = object_schema({
    'request_type': {
        'type': 'string', 'enum': ['변경', '취소', '긴급', '기타']
    },
    'urgency': {'type': 'string', 'enum': ['high', 'normal']},
    'answer': {'type': 'string'}, 'human_check': {'type': 'boolean'}
})

QUESTIONS = [
    "문화센터 강좌 날짜를 다른 날로 옮길 수 있을까요?",
    "체육관 예약을 오늘 취소하면 환불되는지 알고 싶습니다.",
    "예약 시간에 시설 정전이 발생했습니다. 지금 확인해 주세요.",
]

# 문의의 의도와 응답 초안을 만드는 함수
# client : OpenAI 클라이언트 객체
# model : 사용 가능한 OpenAI 모델 이름
# question : 하나의 가상 예약 문의
# 반환값 : 구조화한 응답 dict
def handle_question(client, model, question):
    rules = (
        "공공시설 예약 문의 담당자. JSON 객체 하나만 출력. "
        "request_type은 변경/취소/긴급/기타 중 하나. "
        "urgency는 high/normal. answer는 정중한 한국어 초안. "
        "human_check는 불리언. 확인하지 못한 환불 규정이나 "
        "예약 가능 여부를 단정하면 안 됨."
    )
    raw, tokens, seconds = call_llm(
        client, model, rules, question, schema=BASIC_SCHEMA
    )
    result = parse_json(raw)
    pp("토큰/초:", tokens, seconds)
    return result

def main():

    load_dotenv(ROOT / ".env")

    key = os.getenv("OPENAI_API_KEY", "").strip()

    if not key or key.startswith('sk-your-own'):
        raise SystemExit('.env 파일의 OPENAI_API_KEY를 확인해 주세요')

    client = OpenAI(api_key=key, timeout=60.0, max_retries=2)

    model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

    answers = []
    errors = []

    for question in QUESTIONS:
        try:
            answer = handle_question(client, model, question)
            answers.append({"question": question, "answer": answer})
        except Exception as exc:
            pp("문의 처리 오류:", type(exc).__name__, exc)
            errors.append({
                'question': question, 'error_type': type(exc).__name__,
                'message': str(exc)
            })

    save_json(ROOT / "output" / "basic_reservations.json", answers)
    # 성공과 실패를 모두 저장하여 처리 누락 여부를 확인
    save_json(ROOT / "output" / "basic_reservations_errors.json", errors)

    pp("완료:", len(answers), "건, 실패:", len(errors), "건")
    pp("실제 발송 전 사람 확인 필요")

if __name__ == "__main__":
    main()

up(5)






