# day16_application.py

import pandas as pd
from sklearn.utils import check_X_y
from sklearn.utils.multiclass import type_of_target
from util.print_util import pp, up

FEATURES = ['login_days_30', 'support_tickets', 'contract_months', 'autopay']
TARGET = 'churned'

df = pd.DataFrame({
    "login_days_30": [27, 5, 18, 2, 25, 8, 21, 4, 29, 11],
    "support_tickets": [0, 4, 1, 5, 0, 3, 1, 4, 0, 2],
    "contract_months": [18, 2, 10, 1, 24, 5, 15, 3, 30, 7],
    "autopay": ["Y", "N", "Y", "N", "Y", "N", "Y", "N", "Y", "N"],
    "churned": [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
})

# 문자열 범주를 숫자로 변환
df['autopay'] = df['autopay'].map({
    'Y': 1,
    'N': 0
})

X = df[FEATURES]
y = df[TARGET]

pp('Target type: ', type_of_target(y))

X_checked, y_checked = check_X_y(X, y, dtype='numeric')
pp(X_checked.shape)
pp(y_checked.shape)

new_X = pd.DataFrame([{
    'login_days_30': 9,
    'support_tickets': 2,
    'contract_months': 6,
    'autopay': 0
}])[FEATURES] # 학습 데이터와 같은 컬럼 순서로 재배열

pp('new_X shape: ', new_X.shape)
pp('new_X columns: ', new_X.columns.tolist())
pp('feature order: ', new_X.columns.tolist() == X.columns.tolist())
pp('문제 유형: 분류')
pp(new_X)

up(5)
















