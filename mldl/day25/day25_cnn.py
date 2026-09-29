# day25_cnn.py
# CNN 꽃 이미지 분류

import pathlib
import matplotlib.pyplot as plt
import tensorflow as tf
from PIL import Image
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from util.print_util import pp, up
from include.graph_config import set_graph

set_graph(10, 8, 13)

# ---------------------------------------------------------
# 꽃 이미지 데이터 다운로드
# ---------------------------------------------------------

dataset_url = (
    "https://storage.googleapis.com/"
    "download.tensorflow.org/example_images/"
    "flower_photos.tgz"
)

# Keras 버전에 따라 반환값이
# flower_photos.tar 또는 flower_photos_extracted 같은
# 경로가 될 수 있습니다.
download_path = tf.keras.utils.get_file(
    fname="flower_photos.tar",
    origin=dataset_url,
    extract=True
)

download_path = pathlib.Path(download_path)

pp("get_file() 반환 경로:", download_path)
pp("반환 경로 존재 여부:", download_path.exists())


# ---------------------------------------------------------
# 실제 flower_photos 데이터 폴더 탐색
# ---------------------------------------------------------

# flower_photos 데이터셋에 반드시 존재해야 하는 클래스 폴더
expected_classes = {
    "daisy",
    "dandelion",
    "roses",
    "sunflowers",
    "tulips"
}


def is_flower_data_dir(path):
    """해당 폴더가 실제 꽃 데이터 루트인지 확인합니다."""

    if not path.exists() or not path.is_dir():
        return False

    # 바로 아래 하위 폴더 이름 집합
    subdirs = {
        child.name
        for child in path.iterdir()
        if child.is_dir()
    }

    # 5개의 꽃 클래스 폴더가 모두 존재하면 실제 데이터 루트
    return expected_classes.issubset(subdirs)


def find_flower_data_dir(start_path):
    """Keras 버전과 관계없이 실제 flower_photos 폴더를 찾습니다."""

    candidates = []

    # get_file() 반환값 자체가 디렉토리일 수 있음
    if start_path.is_dir():
        candidates.append(start_path)

    # 반환 경로에서 확장자를 제거한 경로
    candidates.append(start_path.with_suffix(""))

    # 반환 경로와 같은 위치의 대표적인 후보
    candidates.append(start_path.parent / "flower_photos")
    candidates.append(start_path.parent / "flower_photos_extracted")

    # 대표 후보 먼저 검사
    for candidate in candidates:
        if is_flower_data_dir(candidate):
            return candidate

        # flower_photos_extracted/flower_photos 같은
        # 한 단계 중첩 구조도 검사
        nested = candidate / "flower_photos"

        if is_flower_data_dir(nested):
            return nested

    # 위 후보에서 찾지 못하면 datasets 폴더 내부를 재귀적으로 탐색
    search_root = start_path.parent

    for path in search_root.rglob("*"):

        if path.is_dir() and is_flower_data_dir(path):
            return path

    return None


# 실제 이미지 클래스 폴더가 들어 있는 경로 탐색
data_dir = find_flower_data_dir(download_path)
data_dir = pathlib.Path(data_dir)
if (data_dir / 'flower_photos').exists():
    data_dir = data_dir / 'flower_photos'

if data_dir is None:
    raise FileNotFoundError(
        "실제 flower_photos 데이터 폴더를 찾을 수 없습니다.\n"
        f"검색 시작 위치: {download_path.parent}\n"
        "daisy, dandelion, roses, sunflowers, tulips "
        "폴더가 있는지 확인하세요."
    )

pp("실제 데이터 폴더:", data_dir)


# ---------------------------------------------------------
# 데이터 확인
# ---------------------------------------------------------

# 모든 JPG 이미지 검색
image_files = list(data_dir.glob("*/*.jpg"))

image_count = len(image_files)

pp("전체 이미지 수:", image_count)

# 클래스 폴더 확인
folder_names = sorted([
    path.name
    for path in data_dir.iterdir()
    if path.is_dir()
])

pp("클래스 폴더:", folder_names)


# ---------------------------------------------------------
# 장미 이미지 확인
# ---------------------------------------------------------

roses = list(data_dir.glob("roses/*.jpg"))

pp("장미 이미지 수:", len(roses))

if roses:
    rose_image = Image.open(str(roses[0]))

    pp("첫 번째 장미 이미지:", roses[0])
    pp("장미 이미지 크기:", rose_image.size)

    # 필요하면 주석 해제
    # rose_image.show()


# ---------------------------------------------------------
# 튤립 이미지 확인
# ---------------------------------------------------------

tulips = list(data_dir.glob("tulips/*.jpg"))

pp("튤립 이미지 수:", len(tulips))

if tulips:
    tulip_image = Image.open(str(tulips[0]))

    pp("첫 번째 튤립 이미지:", tulips[0])
    pp("튤립 이미지 크기:", tulip_image.size)

    # 필요하면 주석 해제
    # tulip_image.show()


# ---------------------------------------------------------
# 학습 설정
# ---------------------------------------------------------

img_height = 180   # 이미지 높이
img_width = 180    # 이미지 너비
batch_size = 32    # 한 번에 학습하는 이미지 수
epochs = 10        # 전체 학습 반복 횟수


# ---------------------------------------------------------
# 훈련 데이터셋
# ---------------------------------------------------------

train_ds = tf.keras.utils.image_dataset_from_directory(
    data_dir,

    # 전체 데이터 중 20%를 검증 데이터로 사용
    validation_split=0.2,

    # 나머지 80%를 학습 데이터로 사용
    subset="training",

    # 같은 seed를 사용해야 학습/검증 데이터가 일관되게 분리됨
    seed=123,

    # 크기가 다른 이미지를 180×180으로 통일
    image_size=(img_height, img_width),

    # 한 번에 모델에 전달할 이미지 수
    batch_size=batch_size
)


# ---------------------------------------------------------
# 검증 데이터셋
# ---------------------------------------------------------

val_ds = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size
)


# ---------------------------------------------------------
# 클래스 확인
# ---------------------------------------------------------

class_names = train_ds.class_names
class_count = len(class_names)

pp("클래스명:", class_names)
pp("클래스 수:", class_count)


# ---------------------------------------------------------
# 한 batch의 shape 확인
# ---------------------------------------------------------

for images, labels in train_ds.take(1):

    # 예: (32, 180, 180, 3)
    # 32장 × 높이 180 × 너비 180 × RGB 3채널
    pp("이미지 batch shape:", images.shape)

    # 예: (32,)
    pp("라벨 batch shape:", labels.shape)

    pp("첫 번째 이미지 라벨:", int(labels[0]))

    pp(
        "첫 번째 이미지 클래스명:",
        class_names[int(labels[0])]
    )


# ---------------------------------------------------------
# 이미지 9장 시각화
# ---------------------------------------------------------

# 필요하면 아래 show_samples를 True로 변경
show_samples = True

if show_samples:

    plt.figure(figsize=(8, 8))

    for images, labels in train_ds.take(1):

        for i in range(9):

            plt.subplot(3, 3, i + 1)

            plt.imshow(
                images[i].numpy().astype("uint8")
            )

            plt.title(
                class_names[int(labels[i])]
            )

            plt.axis("off")

    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------
# 데이터 로딩 성능 개선
# ---------------------------------------------------------

# 모델이 현재 batch를 학습하는 동안
# 다음 batch를 미리 준비
AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.prefetch(
    buffer_size=AUTOTUNE
)

val_ds = val_ds.prefetch(
    buffer_size=AUTOTUNE
)


# ---------------------------------------------------------
# CNN 모델 생성
# ---------------------------------------------------------

model = Sequential([

    # 입력:
    # 180×180 RGB 이미지
    keras.Input(
        shape=(img_height, img_width, 3)
    ),

    # 픽셀값
    # 0~255 → 0~1
    layers.Rescaling(
        1.0 / 255
    ),

    # -----------------------------------------------------
    # Conv2D 1
    # -----------------------------------------------------

    # filters=16
    #   : 특징을 찾는 필터 16개
    #
    # kernel_size=3
    #   : 필터 하나의 크기는 3×3
    #
    # padding="same"
    #   : 높이와 너비 유지
    #
    # 출력:
    # 180×180×16
    layers.Conv2D(
        filters=16,
        kernel_size=3,
        padding="same",
        activation="relu"
    ),

    # 2×2 영역마다 가장 큰 값 선택
    #
    # 180×180×16
    # → 90×90×16
    layers.MaxPooling2D(
        pool_size=2
    ),

    # -----------------------------------------------------
    # Conv2D 2
    # -----------------------------------------------------

    # 출력:
    # 90×90×32
    layers.Conv2D(
        filters=32,
        kernel_size=3,
        padding="same",
        activation="relu"
    ),

    # 90×90×32
    # → 45×45×32
    layers.MaxPooling2D(
        pool_size=2
    ),

    # -----------------------------------------------------
    # Conv2D 3
    # -----------------------------------------------------

    # 출력:
    # 45×45×64
    layers.Conv2D(
        filters=64,
        kernel_size=3,
        padding="same",
        activation="relu"
    ),

    # 45×45×64
    # → 22×22×64
    #
    # 45는 홀수이므로 2×2 pooling 후
    # 기본 valid 방식에서는 22가 됨
    layers.MaxPooling2D(
        pool_size=2
    ),

    # -----------------------------------------------------
    # Flatten
    # -----------------------------------------------------

    # 22×22×64
    # → 30,976개의 1차원 값
    layers.Flatten(),

    # -----------------------------------------------------
    # Dense
    # -----------------------------------------------------

    # 추출한 특징을 128개 뉴런으로 조합
    layers.Dense(
        units=128,
        activation="relu"
    ),

    # -----------------------------------------------------
    # Output
    # -----------------------------------------------------

    # 꽃 종류 5개에 대응하는 출력값 5개
    #
    # softmax를 사용하지 않고 logits 출력
    layers.Dense(
        units=class_count
    )
])


# ---------------------------------------------------------
# 모델 구조 확인
# ---------------------------------------------------------

model.summary()


# ---------------------------------------------------------
# 모델 컴파일
# ---------------------------------------------------------

model.compile(

    # 가중치를 조정하는 최적화 알고리즘
    optimizer="adam",

    # 정수 라벨을 사용하는 다중 분류 손실 함수
    #
    # 마지막 Dense에 softmax가 없으므로
    # from_logits=True
    loss=tf.keras.losses.SparseCategoricalCrossentropy(
        from_logits=True
    ),

    # 학습 중 정확도 측정
    metrics=["accuracy"]
)


# ---------------------------------------------------------
# 모델 훈련
# ---------------------------------------------------------

history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=epochs
)


# ---------------------------------------------------------
# 학습 결과
# ---------------------------------------------------------

acc = history.history["accuracy"]
val_acc = history.history["val_accuracy"]

loss = history.history["loss"]
val_loss = history.history["val_loss"]

pp(
    "최종 훈련 정확도:",
    round(acc[-1], 4)
)

pp(
    "최종 검증 정확도:",
    round(val_acc[-1], 4)
)

pp(
    "최종 훈련 손실:",
    round(loss[-1], 4)
)

pp(
    "최종 검증 손실:",
    round(val_loss[-1], 4)
)


# ---------------------------------------------------------
# 정확도 / 손실 그래프
# ---------------------------------------------------------

epoch_range = range(
    1,
    len(acc) + 1
)

# 정확도
plt.subplot(1, 2, 1)

plt.plot(
    epoch_range,
    acc,
    label="훈련 정확도"
)

plt.plot(
    epoch_range,
    val_acc,
    label="검증 정확도"
)

plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend(loc="lower right")
plt.title("훈련/검증 정확도")


# 손실
plt.subplot(1, 2, 2)

plt.plot(
    epoch_range,
    loss,
    label="훈련 손실"
)

plt.plot(
    epoch_range,
    val_loss,
    label="검증 손실"
)

plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend(loc="upper right")
plt.title("훈련/검증 손실")

plt.tight_layout()
plt.show()


# ---------------------------------------------------------
# 종료 대기
# ---------------------------------------------------------

up(5)
