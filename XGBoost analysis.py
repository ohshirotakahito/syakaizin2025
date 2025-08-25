# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 10:16:06 2021

@author: ohshi
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import metrics
from sklearn import preprocessing

import xgboost as xgb

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import f1_score
from sklearn.model_selection import KFold

from imblearn.under_sampling import RandomUnderSampler


smn1 ='0'
smn2 ='1'

# データの読み込みと前処理
file_path = 'data/time_series_data.csv' # ファイルパスを適切に設定してください
df = pd.read_csv(file_path)
X = df.drop('label', axis=1).values.reshape(-1, 50, 1)  # 50タイムステップ、1特徴量
y = df['label'].values



# データの標準化
X = preprocessing.scale(X)


#訓練データと検証データの分離
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#データの不均衡の補正（アンダーサンプリング）
count0 = y_train[y_train==0].shape[0]
count1 = y_train[y_train==1].shape[0]

count = min(count0, count1)
strategy = {0:count, 1:count}

rus = RandomUnderSampler(random_state=0, sampling_strategy = strategy)

X_train, y_train = rus.fit_resample(X_train, y_train)



#訓練用データをxgb.DMatrixで，XGBoost用のデータ型に変換
dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test)

#学習パラメータ設定
params = {'max_depth': 10, 
          'eta': 1, 
          'objective': 'multi:softmax', 
          'num_class': 3}

num_round = 200

#学習
bst = xgb.train(params, dtrain, num_round)

#予想
y_pred = bst.predict(dtest)

#評価
acc = accuracy_score(y_test, y_pred)

mtx = confusion_matrix(y_test, y_pred)
MX = pd.DataFrame(mtx, index=['pred_'+smn1, 'pred_'+smn2,], columns=['real_'+smn1,'read_'+smn2])

# 予測結果と、正解（本当の答え）がどのくらい合っていたかを表す混合行列の標準化
x_sm=(sum(mtx[0]))
y_sm=(sum(mtx[1]))
x_arry=mtx[0]/x_sm*100
y_arry=mtx[1]/y_sm*100

#混同行列（％）のデータとカラムラベル挿入
n_mtx=x_arry,y_arry

MX1=pd.DataFrame(n_mtx, index=['pred_'+smn1, 'pred_'+smn2], columns=['real_'+smn1,'read_'+smn2])

f = f1_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print('f-measure_value:', f)
#print(MX)


#モデルをもちいた予想の可視化
fig, ax = plt.subplots(figsize=(4, 3)) # 混合行列のカラムの大きさ設定
sns.heatmap(MX, annot=True, fmt="d",center=250)
ax.set_ylim(len(mtx), 0)# 混合行列の軸の下限を設定し，値がみえるようにする（バグ）
ax.set_title('Confusion_Matrix')

#モデルをもちいた予想の標準化後の可視化
fig, ax = plt.subplots(figsize=(4, 3)) # 混合行列のカラムの大きさ設定
sns.heatmap(MX1, annot=True, fmt="1.1f",center=250)
ax.set_ylim(len(n_mtx), 0)# 混合行列の軸の下限を設定し，値がみえるようにする（バグ）
ax.set_title('normalized Confusion_Matrix')

