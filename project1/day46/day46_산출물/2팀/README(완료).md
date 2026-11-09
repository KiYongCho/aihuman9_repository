나랏말싸미 (NaraTalk)

> 듣고, 따라 말하고, 바로 교정받는 \\\\\\\*\\\\\\\*AI 한국어 발음 코치\\\\\\\*\\\\\\\*
> AI휴먼 과정 2팀 · 팀 집현전

1\. 프로젝트 개요

외국인 학습자가 정답 문장을 듣고 따라 말하면, STT 전사 결과를 정답과 글자 단위로 비교해 어느 글자가 다르게 인식됐는지 바로 알려 주는 Streamlit 웹앱입니다.

팀원 및 담당 기능

이름	역할	주요 담당

최지연	팀장 · PM	일정 관리, 코드 통합, 발표

박세정	데이터	연습 문장 34개 구성, 테스트 녹음, 전처리

성수경	AI 모델	STT(faster-whisper), 발음 평가(CER/WER)

신의진	서비스 · DB	PostgreSQL 스키마, `src/db.py`, SQL 파일

이승우	UI · 배포	Streamlit 화면, 실행 환경

> \\\\\\\[확인 필요] 팀원별 담당 파일을 정확히 적으려면 위 표를 팀에서 한 번 더 검토하세요.

주요 사용자 시나리오

동의: 시작 화면에서 음성 녹음 및 데이터 이용에 동의합니다.

이름 입력: 닉네임을 입력하면 홈으로 들어갑니다(신규 닉네임은 자동 등록).

문장 듣기: 카테고리와 난이도를 골라 정답 음성(TTS)과 로마자 발음 표기를 확인합니다.

따라 말하기: 브라우저에서 녹음하거나 음성 파일을 업로드합니다.

교정 결과: 점수, 등급, 다르게 인식된 글자와 위치를 확인합니다.

학습 이력: 연습 기록이 DB에 쌓이고, 이력과 대시보드에서 다시 볼 수 있습니다.

[서비스 화면]

1.시작</br>
![시작하기.jpg](readme/%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0.jpg)	

2.홈</br>
![홈.jpg](readme/%ED%99%88.jpg)

3.연습하기</br>
![연습하기.jpg](readme/%EC%97%B0%EC%8A%B5%ED%95%98%EA%B8%B0.jpg)

4.학습이력</br>
![학습이력.jpg](readme/%ED%95%99%EC%8A%B5%EC%9D%B4%EB%A0%A5.jpg)

5.결과</br>
![결과.jpg](readme/%EA%B2%B0%EA%B3%BC.jpg)

6.대시보드</br>
![대시보드.jpg](readme/%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C.jpg)

7.</br>
관리자![관리자.jpg](readme/%EA%B4%80%EB%A6%AC%EC%9E%90.jpg)

2\. 기능

구분	구현	파일

STT	faster-whisper `base` 모델, CPU · int8 양자화, 언어 한국어(`ko`) 고정. 원본 / 무음 제거(librosa trim) / 잡음 제거(noisereduce) 3가지 전처리 경로 제공	`src/stt.py`

핵심 AI (발음 평가)	문장부호와 공백을 정규화한 뒤 jiwer로 CER · WER 계산. 정렬 결과를 글자 단위 오류(대체 · 삭제 · 삽입)와 위치로 풀어서 저장. 점수 = `max(0, (1 − CER) × 100)`, 등급 = CER 15% 이하 "매우 우수", 45% 이하 "양호한 수준", 초과 "기초에 집중"	`src/core.py`

TTS	edge-tts `ko-KR-SunHiNeural`로 정답 음성을 즉석 생성하고, 16kHz · mono · PCM16 wav로 변환. korean-romanizer로 로마자 표기 표시	`src/tts.py`

DB	PostgreSQL 테이블 4개(`users`, `sentences`, `practice\\\\\\\_runs`, `error\\\\\\\_items`). SQL은 `sql\\\\\\\_schema\\\\\\\_sql/` 폴더의 개별 파일로 관리하고, `load\\\\\\\_sql()`로 불러 실행	`src/db.py`

UI	Streamlit 화면 6종(홈, 연습하기, 결과, 학습 이력, 분석 대시보드, 관리자)	`app/app.py`, `app/apps/`

폴더 구조

```
NaraTalk/
├── app/
│   ├── app.py              # 진입점: 세션 상태, 사이드바 메뉴
│   └── apps/               # 화면별 파일 (home, practice, result, history, dashboard, manager)
├── src/
│   ├── stt.py              # 음성 인식 + 전처리
│   ├── core.py             # 정규화, CER/WER, 오류 위치, 등급
│   ├── tts.py              # 정답 음성 생성
│   ├── db.py               # DB 연결과 저장·조회 함수
│   └── .env                # DATABASE\\\\\\\_URL (Git에 올리지 않음)
├── sql\\\\\\\_schema\\\\\\\_sql/         # 테이블 생성, 시드, 조회·저장 SQL (34개 파일)
├── assets/                 # 배경, 로고 이미지
├── .streamlit/config.toml  # 테마 설정
└── requirements.txt
```

3\. 실행 환경

Python: 3.11 이상 (팀 개발 환경 3.13에서 실행 확인)

운영체제: Windows 10/11 (PowerShell · PyCharm). Python과 ffmpeg가 동작하면 macOS · Linux에서도 실행 가능합니다.

외부 API 및 비용/접근 조건

서비스	용도	비용	접근 조건

edge-tts (Microsoft Edge 온라인 TTS)	정답 음성 생성	무료, API 키 불필요	인터넷 연결 필요. 비공식 엔드포인트라 서비스 정책이 바뀌면 중단될 수 있음

faster-whisper 모델 (Hugging Face)	STT 모델 파일	무료	첫 실행 때 모델을 내려받으므로 인터넷 필요. 이후에는 로컬 캐시 사용

PostgreSQL (예: Neon)	사용자, 연습 기록 저장	무료 플랜으로 충분	`DATABASE\\\\\\\_URL` 접속 정보 필요

4\. 설치

```bash
python -m venv .venv
# Windows PowerShell: .venv\\\\\\\\Scripts\\\\\\\\Activate.ps1
python -m pip install -r requirements.txt
```

설치 후 PyCharm의 Python Interpreter를 위의 `.venv`로 지정하세요. 터미널과 PyCharm이 서로 다른 Python을 쓰면 `No module named ...` 오류가 납니다.

PowerShell에서 스크립트 실행이 막히면 `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`를 한 번 실행합니다.

5\. 환경변수 및 DB

`src/.env` 파일을 만들고 접속 정보를 넣습니다. 이 파일은 절대 Git에 올리지 않습니다.

```
   DATABASE\\\\\\\_URL=postgresql://<사용자>:<비밀번호>@<호스트>/<DB이름>?sslmode=require
   ```

테이블과 연습 문장 34개를 만듭니다. 프로젝트 최상위 폴더에서 실행합니다.

```bash
   python -c "from src.db import initialize\\\\\\\_database; initialize\\\\\\\_database()"
   ```

아래 SQL 파일이 순서대로 적용됩니다. DBeaver에서 같은 순서로 직접 실행해도 됩니다.
`extension\\\\\\\_pgcrypto.sql` → `create\\\\\\\_users.sql` → `create\\\\\\\_sentences.sql` → `create\\\\\\\_practice\\\\\\\_runs.sql` → `create\\\\\\\_error\\\\\\\_items.sql` → `seed\\\\\\\_sentences\\\\\\\_34.sql`

환경변수 이름과 의미

이름	위치	의미	필수

`DATABASE\\\\\\\_URL`	`src/.env`	PostgreSQL 접속 주소. 없으면 DB 기능 실행 시 안내 오류 발생	필수

> \\\\\\\[확인 필요] 관리자 로그인은 `manager` 테이블을 사용하지만(`login\\\\\\\_manager.sql`), 이 테이블을 만드는 SQL이 저장소에 없습니다. 생성 SQL을 `sql\\\\\\\_schema\\\\\\\_sql/`에 추가하거나 설치 방법을 이 칸에 적어 주세요.

6\. 실행

프로젝트 최상위 폴더에서 실행합니다.

```bash
python -m streamlit run app/app.py
```

브라우저가 자동으로 열리지 않으면 터미널에 표시된 `Local URL`(기본값 http://localhost:8501)을 여세요.

첫 녹음 분석은 STT 모델 로딩 때문에 수십 초 걸릴 수 있습니다. 시연 전에 한 번 미리 실행해 두세요.

7\. 테스트·평가 재현

테스트 명령 (채점 + DB 저장 통합 테스트)

```bash
  python src/core.py
  ```

DB를 초기화하고 테스트 사용자를 등록한 뒤, 25번 문장에 예시 전사문을 넣어 채점 결과를 출력하고 `practice\\\\\\\_runs`에 저장합니다.

통합 시나리오 점검 (수동)

동의 → 연습 → 결과 → 이력 흐름

빈 녹음, 너무 짧은 녹음

DB 연결 실패 시 안내 문구

다른 팀원 PC에서 실행

모델 평가 명령: \[평가 스크립트 경로와 명령 입력]

전처리별 비교: `PronunciationPipeline.evaluate\\\\\\\_all\\\\\\\_pipelines(audio\\\\\\\_path, reference\\\\\\\_text)`로 원본, 무음 제거, 잡음 제거 결과를 한 번에 비교할 수 있습니다.

현재 측정값(발표 기준): 문장 1개 평균 처리 시간 1.6초(중앙값 1.1초). 판정 테스트 15건 정확도 80%, FPR(관대한 채점) 29%, FNR(억울한 감점) 12%(CER 15% 기준).

데이터셋 출처

연습 문장: 팀이 직접 구성한 34개 문장(5개 상황 × 쉬움 · 보통 · 어려움), `seed\\\\\\\_sentences\\\\\\\_34.sql`

테스트 녹음: 팀원이 직접 녹음한 음성(바르게 읽은 녹음 + 일부러 틀리게 읽은 녹음)

외국인 억양 테스트 음성: edge-tts 합성 음성(미국, 중국, 일본, 프랑스, 인도 억양을 음역 텍스트로 흉내 낸 음성). 실제 사람 녹음이 아님

8\. 주의사항·제약

음성 데이터 저장 정책

녹음 파일은 STT 분석을 위해 `temp\\\\\\\_audio/` 폴더에 임시 저장한 뒤, 분석이 끝나면 바로 삭제합니다.

DB에는 음성 원본을 저장하지 않고, 전사 텍스트, 점수, CER/WER, 글자 오류 위치만 저장합니다.

시작 화면의 동의서에 따라, 수집 데이터는 프로젝트 기간 동안만 활용하고 종료 후 파기합니다.

`temp\\\\\\\_audio/`, `src/.env`, `\\\\\\\*.wav`, `\\\\\\\*.mp3`는 `.gitignore`에 넣어 Git에 올리지 않습니다.

알려진 한계

"발음 정확도"가 아니라 "전사 일치도"를 측정합니다. STT가 다르게 받아 적은 글자를 기준으로 판정하므로 억양, 장단, 된소리 같은 발음 차이는 직접 평가하지 못합니다.

관대한 채점: Whisper가 틀린 발음을 문맥상 맞는 단어로 고쳐 적는 경우가 있어, 틀린 발음을 "맞음"으로 판정할 수 있습니다(FPR 29%).

환각: 무음이나 불명확한 발음에서 Whisper가 없는 말을 반복 생성하면 CER이 100%를 넘고 처리 시간도 길어집니다. 점수는 0점에서 멈춥니다.

앱 채점은 원본 경로만 사용: 무음 제거 경로(`run\\\\\\\_stt\\\\\\\_with\\\\\\\_vad`)는 구현되어 있지만 앱 채점에는 아직 연결하지 않았습니다.

짧은 문장에 엄격함: 5자 문장은 1글자만 달라도 CER 20%로 "매우 우수" 기준(15%)을 넘습니다.

로그인 인증 없음: 닉네임만으로 사용자를 구분하는 프로토타입 구조입니다.

표본이 작음: 평가 지표는 15\~34건 기준이라 신뢰구간이 넓습니다.

배포 링크: \[https://naratalk-1.onrender.com/ 입력 또는 "로컬 실행만 지원"]

