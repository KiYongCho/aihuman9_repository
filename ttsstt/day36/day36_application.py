# day36_application.py
# 환승 방송 속도 A/B 테스트

import asyncio
import time
from pathlib import Path
import edge_tts
import pandas as pd
from mutagen import File as AudioFile
from util.print_util import pp, up

OUT = Path(__file__).resolve().parent / 'subway_output'

MESSAGES = [
    "이번 역은 시청역입니다. 이호선으로 갈아타실 수 있습니다.",
    "열차에서 내리실 때 발 빠짐에 주의해 주세요.",
]

RATES = ['-15%', '+0%', '+15%']

async def main():

    OUT.mkdir(parents=True, exist_ok=True)

    rows = []

    for index, message in enumerate(MESSAGES, start=1):

        for rate in RATES:

            tag = rate.replace('%', '').replace('+', 'p')
            tag = tag.replace('-', 'm')

            filename = f'subway_{index:02}_{tag}.mp3'
            path = OUT / filename

            tts = edge_tts.Communicate(message, 'ko-KR-InJoonNeural', rate=rate)

            start = time.perf_counter()
            try:

                await tts.save(str(path))

                elapsed = time.perf_counter() - start

                seconds = AudioFile(str(path)).info.length

                rows.append({
                    'group': index,
                    'file': filename,
                    'rate': rate,
                    'seconds': round(seconds, 2),
                    'elapsed': round(elapsed, 2),
                    'rtf': round(elapsed / seconds, 2)
                })

            except Exception as e:
                pp(f'실패: {filename}: {e}')

    if not rows:
        pp('성공한 합성이 없습니다.')
        return

    df = pd.DataFrame(rows)

    df.to_csv(OUT / 'subway_report.csv', index=False, encoding='utf-8-sig')

    for group, frame in df.groupby('group'):
        longest = frame.loc[frame['seconds'].idxmax()]
        shortest = frame.loc[frame['seconds'].idxmin()]
        pp(
            f"문장 {group}: 최장={longest['rate']}, 최단={shortest['rate']}"
        )

if __name__ == '__main__':
    asyncio.run(main())

up(5)









