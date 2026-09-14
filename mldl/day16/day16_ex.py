# day16_ex.py
# 머신러닝의 전체 흐름, 문제 정의

from util.print_util import pp, pt, up
import pandas as pd
import sklearn
from sklearn.datasets import load_iris
from sklearn.dummy import DummyRegressor, DummyClassifier
from sklearn.utils.multiclass import type_of_target
from sklearn.utils.validation import check_X_y

# 현재 설치된 scikit-learn 버젼 확인
pp(sklearn.__version__)

RANDOM_STATE = 42 # 재현성 확보를 위한 난수 시드값

# 모델 입력에 사용할 Feature 컬럼명 리스트
FEATURES = ['공부시간', '출석률', '실습횟수']

# 모델이 예측할 Label 또는 Target 컬럼명
TARGET = '최종점수'

# 12행 5열 데이터프레임
df = pd.DataFrame({
    "공부시간": [3, 5, 8, 10, 6, 7, 4, 9, 2, 11, 5, 8],
    "출석률": [72, 80, 92, 97, 85, 90, 76, 95, 68, 99, 82, 93],
    "실습횟수": [2, 4, 7, 9, 5, 6, 3, 8, 1, 10, 4, 7],
    "최종점수": [58, 68, 84, 93, 74, 80, 63, 89, 52, 97, 70, 86],
    "합격여부": [0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1]
})

# X(Feature)와 y(Label or Target) 구성
X = df[FEATURES]
pp(X)
pt(X) # <class 'pandas.DataFrame'>
pp(X.shape) # (12, 3)
y = df[TARGET]
pp(y)
pt(y) # <class 'pandas.Series'>
pp(y.shape) # (12,)

# iris데이터 : 붓꽃 품종 분류에 사용하는 scikit-lean 내장 데이터셋
iris_default = load_iris()
pp(iris_default)
pt(iris_default) # <class 'sklearn.utils._bunch.Bunch'>
pp(iris_default.data) # X, 2차원 넘파이 배열
pp(iris_default.target) # y, 1차원 넘파이 배열 (품종 번호)
# Feature 이름 1차원 넘파이 배열
# ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
# sepal: 꽃받침, petal: 꽃잎
pp(iris_default.feature_names)
# 품종명 1차원 넘파이 배열, ['setosa' 'versicolor' 'virginica']
pp(iris_default.target_names)
# dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename', 'data_module'])
pp(iris_default.keys())
# ['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename', 'data_module']
pp(list(iris_default.keys()))

# iris 데이터셋을 데이터프레임 형태로
iris = load_iris(as_frame=True)
pp(iris)
pt(iris) # <class 'sklearn.utils._bunch.Bunch'>

# Feature, Target
iris_X = iris.data
iris_y = iris.target

# type_of_target(y)
# : y가 연속형(continuous), 이진분류(binary), 다중분류(multiclass
#   중 어떤 형태인지 문자열로 반환

# 회귀
regression_target = df['최종점수'].astype(float)
pp(type_of_target(regression_target)) # multiclass

# 이진분류
binary_target = df['합격여부']
pp(type_of_target(binary_target)) # binary

# 다중분류
multiclass_target = iris.target
pp(type_of_target(multiclass_target)) #  multiclass

# check_X_y(X, y) : X와 y의 길이, 차원, 자료형, 결측치 여부 등을 검증
# dtype='numeric' : X가 숫자형 데이터로 변환 가능한지 검증
X_checked, y_checked = check_X_y(X, y, dtype='numeric')
pp(X_checked.shape) # (12, 3)
pp(X_checked)
pp(y_checked.shape) # (12,)
pp(y_checked)

X_bad = df[['공부시간', '출석률']]
y_bad = df['최종점수'].iloc[:-1] # 잘못된 y
try:
    check_X_y(X_bad, y_bad, dtype='numeric')
except ValueError as e:
    pp('X와 y 길이 불일치 오류: ', e)

df_text = pd.DataFrame({
    '직무': ['Backend', 'Frontend', 'Data'],
    '경력개월': [12, 6, 18],
    '합격여부': [1, 0, 1]
})

try:
    check_X_y(df_text[['직무', '경력개월']], df_text['합격여부'], dtype='numeric')
except ValueError as e:
    pp('문자열 Feature 오류: ', e)

df_missing = df.copy()
df_missing.loc[2, '출석률'] = None # 3행의 출석률 컬럼값을 None으로
pp(df_missing.isna().sum())

# 데이터 누수 (Data Leakage)
# : 예측 시점에는 알 수 없는 정답이 포함되어서 예측 결과에 영향을 미침

job_df = pd.DataFrame({
    "경력개월": [0, 12, 24, 6, 18],
    "포트폴리오수": [2, 5, 7, 3, 6],
    "최종합격통보발송": [0, 1, 1, 0, 1],
    "합격여부": [0, 1, 1, 0, 1]
})

TARGET_JOB = '합격여부' # 타겟
# 잘못된 패쳐 : 최종합격통보발송은 예측 시점에 알 수 없는 패쳐임 => 데이터 누수
BAD_FEATURES = ['경력개월', '포트폴리오수', '최종합격통보발송']
GOOD_FEATURES = ['경력개월', '포트폴리오수']

# DummyRegressor : 다른 회귀모델과 비교하기 위해서 기준을 스스로 정하는 더미 회귀 모델
reg_model = DummyRegressor(strategy='mean') # 정답 기준이 평균

pp(reg_model.get_params()) # 모델을 생성할때 설정한 하이퍼파라미터 딕셔너리

reg_model.fit(X, y) # 모델 학습

pp(reg_model.n_features_in_) # 3, 모델 학습 후 패쳐 수

# ['공부시간' '출석률' '실습횟수'], 모델 학습 후 패쳐 이름들
pp(reg_model.feature_names_in_)

# 새로운 패쳐에 대한 예측값을 반환
reg_pred = reg_model.predict(X.iloc[[0, 1]])
pp(reg_pred) # 모델 예측 결과
pp(y.mean()) # 평균
















































