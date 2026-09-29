# Team 3 강사용 보고서 작성 예시

## 프로젝트
제품 표면 패턴 판별

## 문제 유형
이진 분류

## 핵심 모델
CNN

## 예시 결론
16×16 흑백 이미지의 가로/세로 패턴을 CNN으로 분류했습니다. 입력은 (samples, height, width, channels)의 4차원 구조입니다. Conv2D에서 지역 패턴을 추출하고 MaxPooling2D로 공간 크기를 줄인 뒤 Flatten과 Dense로 최종 분류했습니다. Sigmoid와 Binary Crossentropy를 사용했으며 EarlyStopping으로 과도한 학습을 줄였습니다. model.summary()를 통해 Conv2D의 filters가 출력 채널 수를 결정하고 Pooling이 높이와 너비를 줄이는 것을 확인했습니다.

> 실제 수치는 학생의 TensorFlow 버전, 난수 상태, 학습 환경에 따라 달라질 수 있으므로
> 특정 숫자를 정답으로 평가하기보다 학습 과정과 해석을 중심으로 확인하는 것을 권장합니다.
