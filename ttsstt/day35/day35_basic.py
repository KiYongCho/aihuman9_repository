# day35_basic.py
# 물류 음성명령의 전사 오류 검증

import re
import unicodedata
import pandas as pd
from jiwer import wer, cer, process_words
from util.print_util import pp, up

PAIRS = [
    ("첫 번째 상자를 오른쪽 선반으로 이동", "첫 번째 상자를 오른쪽 선반으로 이동"),
    ("파란 상자를 창고 입구에 배치", "파란 상자를 창고에 배치"),
    ("재고 수량 다섯 개를 확인", "재고 수량 네 개를 확인"),
    ("출고 목록을 다시 확인", "출고 목록을 반드시 다시 확인"),
    ("작업 구역 조명을 켜 주세요", "작업 구역 조명 켜 주세요")
]

# 정규화 함수
def norm(value):
    value = unicodedata.normalize('NFC', value).lower()
    value = re.sub(r'[^가-힣a-z0-9\s]', r' ', value)
    return re.sub(r'\s+', ' ', value).strip()

def main():

    rows = []

    for idx, (reference, hypothesis) in enumerate(PAIRS, 1):
        ref, hyp = norm(reference), norm(hypothesis) # 정답과 예측 정규화
        info = process_words(ref, hyp) # S, D, I
        rows.append({
            '번호': idx,
            '정답': reference,
            '인식': hypothesis,
            'WER': wer(ref, hyp),
            'CER': cer(ref, hyp),
            'S': info.substitutions,
            'D': info.deletions,
            'I': info.insertions
        })

    df = pd.DataFrame(rows)
    pp(df.to_string(index=False))

    worst = df.loc[df['WER'].idxmax()] # WER 최대

    pp(f"가장 높은 WER: {worst['번호']}번, {worst['WER']:.2%}")
    pp('개선: 마이크 거리 표준화, 현장 용어 정답 사전 구축')

if __name__ == '__main__':
    main()

up(5)





























