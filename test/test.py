# day33_ex.py
# 텍스트 전처리, TF-IDF, 코사인 유사도, WAV 파형

# Alt + F12 > pip install librosa

import re
from collections import Counter
from pathlib import Path
import librosa
import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from util.print_util import pp, up
from include.graph_config import set_graph

set_graph(10, 8, 13)

BASE_DIR = Path(__file__).resolve().parent

DOCS = [
    "AI 음성 인식 모델은 말을 텍스트로 변환합니다!",
    "음성 합성 모델은 텍스트를 말소리로 바꿉니다.",
    "텍스트 분석에는 AI 모델과 전처리가 중요합니다.",
    "음성 인식과 텍스트 분석은 입력 데이터가 다릅니다.",
]

# 텍스트 정규화 함수
def normalize(text):
    # 특수기호를 공백으로 치환하고 중복 공백을 축소
    text = re.sub(r"[^가-힣A-Za-z0-9\s]", " ", text)
    # \s+는 공백·탭·줄바꿈이 한 번 이상 이어진 부분에 매칭
    return re.sub(r"\s+", " ", text).strip().lower()

# 문서 토큰화 반환 함수
def inspect_documents(documents):
    # 문서별 정제 결과와 공백 단위 토큰을 확인
    cleaned = [normalize(doc) for doc in documents]
    pp("문서 전처리와 토큰화")
    for index, doc in enumerate(cleaned, 1):
        tokens = doc.split()
        pp(f"문서 {index}: {doc}")
        pp("토큰:", tokens)
    counts = Counter(" ".join(cleaned).split())
    pp("전체 토큰 빈도 TOP 7:", counts.most_common(7))
    return cleaned

# 어휘집과 BoW/TF-IDF 특성행렬 확인 함수
def inspect_vectors(documents):
    '''
      r"..." : Raw String, 백슬래시를 이스케이프 처리하지 않고 그대로 전달
      (?u) : Unicode 모드, 유니코드 문자 기준으로 처리
      \b : Word Boundary, 단어의 경계
      \w : Word Character, 한글, 영문, 숫자, 밑줄 등 문자
      + : 반복, 바로 앞의 문자가 1개 이상 반복
    '''
    token_pattern = r"(?u)\b\w+\b"
    count_vec = CountVectorizer(token_pattern=token_pattern)

    # fit_transform(): 어휘집 학습 후 문서를 카운트 행렬로 변환
    bow = count_vec.fit_transform(documents)
    pt("BoW(단어 빈도)")
    pp("어휘집:", count_vec.get_feature_names_out().tolist())
    pp("행렬 shape:", bow.shape)  # (문서 수, 어휘 수)
    pp(bow.toarray())  # 학습용 작은 데이터에서만 밀집 변환

    # TF-IDF 벡터화
    tfidf_vec = TfidfVectorizer(
        token_pattern=token_pattern,
        norm="l2",       # L2정규화, 행별 벡터의 L2 크기를 1로 조정
        smooth_idf=True, # 문서 빈도 계산에 평활화 적용
    )
    # fit_transform(): 어휘집과 IDF 통계를 학습해 가중치 계산
    matrix = tfidf_vec.fit_transform(documents)
    pp("TF-IDF와 문서 유사도")
    pp("TF-IDF 행렬 shape:", matrix.shape)
    pp("어휘별 IDF:")

    for term, value in zip(tfidf_vec.get_feature_names_out(), tfidf_vec.idf_):
        pp(f"  {term}: {value:.3f}")

    scores = cosine_similarity(matrix) # 행별 특징벡터 사이 코사인 유사도
    pp("문서별 코사인 유사도:\n", np.round(scores, 3))

    new_doc = normalize("음성 인식과 텍스트 변환")

    vector = tfidf_vec.transform([new_doc]) # 기존 어휘와 IDF를 사용, 재학습하지 않음
    pp("새 문서 벡터 shape:", vector.shape)
    pp("새 문서와 기존 문서 유사도:",
       np.round(cosine_similarity(vector, matrix), 3))

# 직접 생성한 가상 음성 신호를 WAV로 저장하고 읽는 함수
def inspect_audio():
    pp("오디오 파형, 샘플 수, 샘플링레이트")

    sr = 16000  # Hz: 1초당 저장되는 진폭 샘플 수
    seconds = 1.5
    time = np.arange(int(sr * seconds)) / sr

    # 220Hz 및 440Hz 합성: 실제 발화가 아닌 실습용 신호.
    samples = 0.35 * np.sin(2 * np.pi * 220 * time)
    samples += 0.15 * np.sin(2 * np.pi * 440 * time)

    path = BASE_DIR / "sample.wav"
    sf.write(path, samples, sr) # WAV 파일로 저장.

    # sr=None: 원본 샘플링레이트 유지, mono=True: 모노 로딩
    signal, loaded_sr = librosa.load(path, sr=None, mono=True)
    duration = len(signal) / loaded_sr
    pp("파일:", path.name)
    pp("자료형 및 배열 크기:", signal.dtype, signal.shape)
    pp("샘플링레이트(Hz):", loaded_sr)
    pp("샘플 수:", len(signal))
    pp(f"길이(초): {duration:.3f}")

    x = np.arange(len(signal)) / loaded_sr # 그래프 x축은 샘플 인덱스를 Hz로 나눈 시간(초)

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(x, signal, linewidth=0.8)
    ax.set(xlabel="Time (s)", ylabel="Amplitude", title="Synthetic audio waveform")
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(BASE_DIR / "day33_waveform.png", dpi=130)
    plt.show()

if __name__ == "__main__":
    cleaned_docs = inspect_documents(DOCS)
    inspect_vectors(cleaned_docs)
    inspect_audio()
