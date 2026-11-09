# day36_ex1.py
# 한국어 TTS 합성 및 청취 품질 평가

# Alt + F12 > pip install edge-tts, mutagen

import asyncio # 비동기 IO
import csv
import time
from pathlib import Path
import edge_tts # 온라인 TTS 모델
from mutagen import File as AudioFile # 파일의 메타데이터
from util.print_util import pp, up

# 출력 파일 경로
OUT = Path(__file__).resolve().parent / 'outputs'

# edge-tts에서 제공하는 voice id
VOICE = 'ko-KR-SunHiNeural'
ALT_VOICE = 'ko-KR-InJoonNeural'

# TTS에 사용할 문장들
# SAMPLES = [
#     '안녕하세요. AI휴먼입니다.',
#     '오늘의 분석 결과를 안내하겠습니다.',
#     '잠시 후 다시 시도해 주세요.'
# ]
SAMPLES = [
   "[더팩트 | 문은혜 기자] 테슬라가 지상 주행을 넘어 공중 회전까지 가능한 전기 스포츠카를 선보였다. 로켓에 사용되는 추진 기술을 자동차에 접목해 차체를 공중으로 띄우는 데 성공하면서 일론 머스크 테슬라 최고경영자(CEO)가 구상해 온 '하늘을 나는 자동차'가 모습을 드러냈다.",
   "16일 경기도소방재난본부등에 따르면 오전 8시38분께 부천시 오정구 내동의 4층짜리 금속부품 도장공장 3층에서 화재가 발생했다.",
   "또한 백악관과의 관계 개선을 위한 러시아 에너지 시설 공격 중단 의향에 대해 그는 “미국산 패트리엇 요격 미사일을 더 많이 제공받는다면 동의할 수 있다”면서 “그것이 수용할 수 있는 최소한의 조건”이라고 강조했다. 이외에도 그는 트럼프 대통령이 블라디미르 푸틴 러시아 대통령을 노골적으로 칭찬하는 태도에 대한 불만을 숨기지 않았다."
]

# 문장을 지정한 음색 / 속도 / 피치로 MP3에 저장하는 함수
async def synthesize(text, filename, voice=VOICE, rate='+0%', pitch='+0%'):

    target = OUT / filename

    # 음성 합성 객체
    tts = edge_tts.Communicate(text, voice=voice, rate=rate, pitch=pitch)

    start = time.perf_counter() # 시작 시간
    await tts.save(str(target)) # 합성 결과를 MP3 저장
    end = time.perf_counter()  # 종료 시간
    elapsed = end - start # 소요 시간

    audio = AudioFile(str(target)) # MP3를 읽어서 메타데이터 조회

    # audio가 없거나 info라는 속성이 없다면
    if audio is None or not hasattr(audio, 'info'):
        raise ValueError(f'오디오 메타데이터 분석 실패: {target}')

    seconds = round(audio.info.length, 3) # 음성 재생 길이 (초)

    return {
        'file': filename, # 파일명
        'text': text, # 변환할 텍스트
        'voice': voice, # voice id
        'rate': rate, # 속도
        'pitch': pitch, # 높낮이
        'duration_sec': seconds, # 재생 시간
        'size_bytes': target.stat().st_size, # 파일의 바이트 수
        'elapsed_sec': round(elapsed, 3), # 처리 소요시간
        'rtf': round(elapsed / seconds, 3) if seconds else None # RTF
    }

async def main():

    OUT.mkdir(parents=True, exist_ok=True)

    cases = [
        (f'tts_{i:02}.mp3', text, VOICE, '+0%', '+0Hz')
        for i, text in enumerate(SAMPLES, start=1)
    ]

    base = '분석 결과를 확인하세요.'

    cases += [
        ('cmp_base.mp3', base, VOICE, '+0%', '+0Hz'), # 기본
        ('cmp_punct.mp3', '분석 결과를 확인하세요!', VOICE, '+0%', '+0Hz'), # text 교체
        ('cmp_slow.mp3', base, VOICE, '-20%', '+0Hz'), # 속도 -20% 감소
        ('cmp_fast.mp3', base, VOICE, '+20%', '+0Hz'), # 속도 +20% 증가
        ('cmp_pitch.mp3', base, VOICE, '+0%', '+20Hz'), # 피치 +20Hz 증가
        ('cmp_voice.mp3', base, ALT_VOICE, '+0%', '+0Hz') # voice id 교체
    ]

    rows = []

    for filename, text, voice, rate, pitch in cases:
        try:
            row = await synthesize(text, filename, voice, rate, pitch)
            rows.append(row)
            pp(f'완료: {filename} / {row['duration_sec']}초')
        except Exception as e:
            pp(f'실패: {filename}: {type(e).__name__}: {e}')

    # 빈 설문 CSV : 평가자가 실제 음성을 듣고 점수를 기입함
    with (OUT / 'listening_scores.csv') \
        .open('w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(['clip_id', 'evaluator', 'clarity', 'naturalness', 'comment'])
        for row in rows:
            writer.writerow([row['file'], '', '', '', ''])

    pp('생성 완료: tts_metadata.csv, listening_scores.csv')
    pp('평가표를 작성한 뒤 day36_ex2.py를 실행하세요.')

if __name__ == '__main__':
    asyncio.run(main())

up(5)



























