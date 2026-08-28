# day3_extra.py

# 제목 출력
print('=' * 60)
print('기업교육 견적/손익 계산기') # 프로그램 제목
print('=' * 60)

# 입력 처리
company_name = input('회사명: ')
course_name = input('교육과정명: ')
participants = int(input('참가 인원(명): '))
total_hours = float(input('총 교육시간(시간): '))
sales_hourly_rate = int(input('고객 청구 시간당 교육비(원): '))
instructor_hourly_pay = int(input('강사 지급 시간당 강사료(원): '))
material_unit_cost = int(input('1인당 교재/실습비(원): '))
venue_equipment_cost = int(input('장소 및 장비 비용(원): '))
discount_rate = float(input('고객 할인율(%): '))

print()

MIN_PARTICIPANTS = 5 # 최소 참가 인원, 상수
MAX_PARTICIPANTS = 30 # 최대 참가 인원, 상수
TARGET_MARGIN_RATE = 25.0 # 회사 목표 최소 이익률

# 연산

# 교육시간 * 시간당 교육비
training_sales = total_hours * sales_hourly_rate * participants # 교육 판매금액

# 참가 인원수 * 교재/실습비
material_cost = participants * material_unit_cost # 전체 교재/실습비

# 교육 판매금액 + 교재/실습비 + 장소/장비비
subtotal = training_sales + material_cost + venue_equipment_cost # 할인 전 견적금액

# 할인 전 견적금액 * 할인율
discount_amount = subtotal * discount_rate / 100 # 실제 할인금액

# 할인 전 견적금액 - 할인금액
final_contract_amount = subtotal - discount_amount # 최종 계약 예상금액

# 총 교육시간 * 시간당 강사료
instructor_cost = total_hours * instructor_hourly_pay # 전체 강사비

# 강사비 + 교재/실습비 + 장소/장비비
total_cost = instructor_cost + material_cost + venue_equipment_cost # 전체 원가

# 최종 계약 예상금액 - 전체 원가
expected_profit = final_contract_amount - total_cost # 예상 이익

# 예상 이익 / 최종 계약 예상금액 * 100
profit_margin_rate = expected_profit / final_contract_amount * 100 # 예상 이익률

# 예상 이익이 0보다 큰지 여부
is_profitable = expected_profit > 0

# 참가 인원이 최소 인원 이상인지 여부
is_min_participant_ok = participants >= MIN_PARTICIPANTS

# 참가 인원이 최대 인원 이하인지 여부
is_max_participant_ok = participants <= MAX_PARTICIPANTS

# 참가 인원 범위 충족 여부
is_participant_range_ok = is_min_participant_ok and is_max_participant_ok

# 예상 이익률이 목포 이익률 이상인지 여부
is_target_margin_ok = profit_margin_rate >= TARGET_MARGIN_RATE

# 세 조건을 모두 만족하면 사업 진행 여부
can_proceed = is_profitable and is_participant_range_ok and is_target_margin_ok

# 견적서 시작을 알리는 구분선을 출력합니다.
print("-" * 60)

# 리포트 제목을 출력합니다.
print("기업교육 견적 및 손익 리포트")

# 다시 구분선을 출력합니다.
print("-" * 60)

# 입력받은 회사명을 출력합니다.
print(f"회사명             : {company_name}")

# 입력받은 교육과정명을 출력합니다.
print(f"교육과정           : {course_name}")

# 참가 인원을 정수 그대로 출력합니다.
print(f"참가 인원          : {participants}명")

# 총 교육시간을 소수점 첫째 자리까지 출력합니다.
print(f"총 교육시간        : {total_hours:.1f}시간")

# 견적 부분과 앞 내용을 구분하기 위해 빈 줄을 출력합니다.
print()

# 견적 영역의 제목을 출력합니다.
print("[견적]")

# 교육 판매금액에 천 단위 콤마를 적용해 출력합니다.
print(f"교육 판매금액      : {training_sales:,.0f}원")

# 전체 교재/실습비에 천 단위 콤마를 적용해 출력합니다.
print(f"교재/실습비        : {material_cost:,}원")

# 장소 및 장비 비용에 천 단위 콤마를 적용해 출력합니다.
print(f"장소/장비비        : {venue_equipment_cost:,}원")

# 할인 전 견적금액에 천 단위 콤마를 적용해 출력합니다.
print(f"할인 전 견적금액   : {subtotal:,.0f}원")

# 할인율을 소수점 첫째 자리까지 출력합니다.
print(f"할인율             : {discount_rate:.1f}%")

# 할인금액에 천 단위 콤마를 적용해 출력합니다.
print(f"할인금액           : {discount_amount:,.0f}원")

# 최종 계약 예상금액에 천 단위 콤마를 적용해 출력합니다.
print(f"최종 계약 예상금액 : {final_contract_amount:,.0f}원")

# 손익 영역과 앞 내용을 구분하기 위해 빈 줄을 출력합니다.
print()

# 손익 영역의 제목을 출력합니다.
print("[예상 원가 및 손익]")

# 강사비에 천 단위 콤마를 적용해 출력합니다.
print(f"강사비             : {instructor_cost:,.0f}원")

# 총 원가에 천 단위 콤마를 적용해 출력합니다.
print(f"총 원가            : {total_cost:,.0f}원")

# 예상 이익에 천 단위 콤마를 적용해 출력합니다.
print(f"예상 이익          : {expected_profit:,.0f}원")

# 예상 이익률을 소수점 둘째 자리까지 출력합니다.
print(f"예상 이익률        : {profit_margin_rate:.2f}%")

# 사업성 점검 영역과 앞 내용을 구분하기 위해 빈 줄을 출력합니다.
print()

# 사업성 점검 영역의 제목을 출력합니다.
print("[사업성 점검]")

# 이익 발생 여부를 Boolean 값으로 출력합니다.
print(f"이익 발생 여부         : {is_profitable}")

# 권장 참가 인원 범위를 만족하는지 Boolean 값으로 출력합니다.
print(f"권장 인원 충족 여부    : {is_participant_range_ok}")

# 목표 이익률을 만족하는지 Boolean 값으로 출력합니다.
print(f"목표 이익률 충족 여부  : {is_target_margin_ok}")

# 전체 사업 진행 기준을 만족하는지 Boolean 값으로 출력합니다.
print(f"사업 진행 기준 충족    : {can_proceed}")

# 자료형 확인 영역과 앞 내용을 구분하기 위해 빈 줄을 출력합니다.
print()

# 자료형 확인 영역의 제목을 출력합니다.
print("[자료형 확인]")

# 회사명 변수의 자료형이 str인지 확인합니다.
print(f"company_name 자료형 : {type(company_name)}")

# 참가 인원 변수의 자료형이 int인지 확인합니다.
print(f"participants 자료형 : {type(participants)}")

# 총 교육시간 변수의 자료형이 float인지 확인합니다.
print(f"total_hours 자료형  : {type(total_hours)}")

# 사업 진행 기준 변수의 자료형이 bool인지 확인합니다.
print(f"can_proceed 자료형  : {type(can_proceed)}")

# 프로그램의 마지막 구분선을 출력합니다.
print("-" * 60)

# 프로그램 종료 메시지를 출력합니다.
print("견적 및 손익 계산이 완료되었습니다.")

# 마지막 구분선을 출력합니다.
print("-" * 60)



















