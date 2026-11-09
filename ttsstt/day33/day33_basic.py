# day33_basic.py

import re
from collections import Counter
from util.print_util import pp, up

REVIEWS =[
    '배송이 정말 빨라요!!! ',
    '포장이 깔끔하고 배송도 좋네요.',
    '배송 늦음... 포장 불량',
    '상품 품질이 좋아요, 재구매!'
]

# 기호를 공백으로 바꾸고 중복 공백을 제거하는 함수
def clean_review(text):
    text = re.sub(r'[^가-힣A-Za-z0-9\s]', ' ', text)
    return re.sub(r'\s+', ' ', text).strip()

def main():

    # 정제된 문서 리스트
    cleaned = [clean_review(review) for review in REVIEWS]
    # 문서를 공백 기준으로 분할한 리스트
    tokens_by_review = [text.split() for text in cleaned]

    pp('리뷰별 토큰')
    for index, tokens in enumerate(tokens_by_review, 1):
        pp(index, tokens)

    counts = Counter()
    for tokens in tokens_by_review:
        counts.update(tokens) # 토큰별 출현 회수를 누적

    pp('리뷰 수: ', len(REVIEWS))
    pp('고유 단어 수: ', len(counts))
    pp('상위 5개: ', counts.most_common(5))

if __name__ == '__main__':
    main()

up(5)