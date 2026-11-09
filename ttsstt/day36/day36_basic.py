# day36_basic.py
# 도서관 안내 자동 합성

import asyncio
import time
from pathlib import Path
import edge_tts
import pandas as pd
from mutagen import File as AudioFile
from util.print_util import pp, up

OUT = Path(__file__).resolve().parent / 'library_output'

MESSAGES = [
    "도서관은 오전 아홉 시부터 오후 여섯 시까지 운영합니다.",
    "열람실에서는 휴대전화를 진동으로 설정해 주세요.",
    "대출 도서는 반납함을 이용해 돌려주실 수 있습니다.",
]

async def main():

    OUT.mkdir(parents=True, exist_ok=True)

    rows = []

    for number, message in enumerate(MESSAGES, start=1):

        path = OUT / f'library_{number:02}.mp3'

        tts = edge_tts.Communicate(message, 'ko-KR-SunHiNeural')

        try:

            await tts.save(str(path))

            info = AudioFile(str(path)).info

            rows.append({
                'file': path.name,
                'message': message,
                'seconds': round(info.length, 2),
                'bytes': path.stat().st_size
            })

            pp(f'저장: {path.name}')

        except Exception as e:
            pp(f'합성 실패: {e}')

    pd.DataFrame(rows).to_csv(
        OUT / 'library_output.csv',
        index=False,
        encoding='utf-8-sig'
    )

    pp(f'성공: {len(rows)}개')

if __name__ == '__main__':
    asyncio.run(main())

up(5)
























