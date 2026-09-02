# day7_challenge_utils.py

import csv

# 테스트용 CSV 파일을 저장하는 함수를 정의합니다.
def save_sample_csv(path):
    # 헤더와 샘플 학생 데이터를 준비합니다.
    rows = [
        ["name", "score"],
        ["김민수", 88],
        ["이서연", 93],
        ["박지훈", 76],
        ["최유진", 85],
        ["오류데이터", "점수없음"],
        ["한지민", 91],
    ]

    # 전달받은 경로의 CSV 파일을 쓰기 모드로 엽니다.
    with open(path, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

# CSV 파일을 안전하게 읽는 함수를 정의합니다.
def load_score_csv(path):
    result = []
    try:
        # 전달받은 CSV 파일을 읽기 모드로 엽니다.
        with open(path, "r", encoding="utf-8-sig") as file:
            reader = csv.reader(file)
            next(reader, None)
            # 실제 CSV 행 번호에 맞게 2부터 시작합니다.
            for row_number, row in enumerate(reader, start=2):
                # 필요한 열이 2개보다 적으면 잘못된 행으로 판단합니다.
                if len(row) < 2:
                    print(f"{row_number}행은 열 개수가 부족하므로 건너뜁니다.")
                    continue # 다음 번 반복 수행
                name = row[0].strip()
                score_text = row[1].strip()
                try:
                    score = int(score_text)
                except ValueError:
                    print(
                        f"{row_number}행의 점수 '{score_text}'은 숫자가 아니므로 건너뜁니다."
                    )
                    continue
                result.append((name, score))
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {path}")
    except UnicodeDecodeError: # 인코딩 에러
        print("CSV 파일의 문자 인코딩을 확인해 주세요.")
    return result