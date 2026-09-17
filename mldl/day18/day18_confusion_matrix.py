# day18_confusion_matrix.py

# 혼동행렬 (Confusion Matrix)
# : 실제 클래스와 모델이 예측한 클래스간의 4가지 예측 지표
# 1) TN (True Negative) : 실제 0인데 0으로 맞춤
# 2) FP (False Positive) : 실제 0인데 1로 틀림
# 3) FN (False Negative) : 실제 1인데 0으로 틀림
# 4) TP (True Positive) : 실제 1인데 1로 맞춤
# True/False = 맞춤/틀림
# Negative/Positive = 0으로예측/1로예측

from sklearn.metrics import confusion_matrix
from util.print_util import pp

y_true = [0, 0, 0, 0, 1, 1, 1, 1, 1, 0] # 실제
y_pred = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0] # 예측

# 혼동행렬 생성
cm = confusion_matrix(y_true, y_pred)
pp(cm)
# [[4 1]   [[TN, FP]
#  [2 3]]   [FN, TP]]

# ravel() : 2차원 배열을 1차원 값으로 분리
tn, fp, fn, tp = cm.ravel()

pp('TN: ', tn) # 4, 0으로 예측했는데 맞춤 => 실제 0
pp('FP: ', fp) # 1, 1로 예측했는데 틀림 => 실제 0
pp('FN: ', fn) # 2, 0으로 예측했는데 틀림 => 실제 1
pp('TP: ', tp) # 3, 1로 예측했는데 맞춤 => 실제 1






















