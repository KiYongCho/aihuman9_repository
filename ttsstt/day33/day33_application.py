# day33_application.py

import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from util.print_util import pp, up

JOBS = {
    "백엔드 개발": "python api 서버 데이터베이스 개발",
    "데이터 분석": "python pandas 통계 시각화 분석",
    "프론트엔드": "javascript react ui 화면 개발",
    "ML 엔지니어": "python 머신러닝 모델 배포 api",
}

# 공고로 학습한 Vectorizer로 검색어를 변환하고 유사도를 정렬하는 함수
def search_jobs(query):

    names = list(JOBS.keys()) # 공고명들의 리스트
    documents = list(JOBS.values()) # 문서들의 리스트

    # 정규표현식 패턴으로 토크나이징하고 벡터화하는 벡터라이져
    vectorizer = TfidfVectorizer(token_pattern=r'(?u)\b\w+\b')

    # 공고 문서들로 어휘집과 IDF를 학습
    matrix = vectorizer.fit_transform(documents)

    # 공고에서 학습된 특성 공간으로 검색어를 변환
    query_vec = vectorizer.transform([query])

    # 검색어 1행과 공고 4행 비교해서 코사인유사도 획득
    scores = cosine_similarity(query_vec, matrix).ravel()

    # 큰 점수부터 정렬한 인덱스 획득
    order = np.argsort(scores)[::-1]

    pp(f'검색어: {query}')

    # 큰 점수부터 공고명과 코사인유사도 출력
    for index in order:
        pp(f'{names[index]}: {scores[index]:.4f}')

    # 코사인유사도가 0이면
    if scores[order[0]] == 0:
        pp('일치하는 등록 어휘가 없습니다.')
    else:
        # 4개 중 가장 코사인유사도가 높은 공고명을 출력
        pp('추천 공고: ', names[order[0]])

if __name__ == '__main__':
    search_jobs('python 모델 api')
    search_jobs('우주비행 로켓')

up(5)







