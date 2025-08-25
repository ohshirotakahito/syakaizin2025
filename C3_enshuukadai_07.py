# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 11:39:34 2023

@author: ohshi
"""
# =============================================================================
# ７．ニューラルネットワークを用いた化学データのパターン認識
# 
# 目的
# 生成された「Solubility」データセットを用いて、化合物の特性からその溶解度を予測するニューラルネットワークモデルを構築する。
# 深層学習の基本的な概念を理解し、実際のデータに適用する。
# データセット
# 「Solubility」データセットには、化合物の分子量、極性、水素結合ドナー数、水素結合アクセプター数、および溶解度が含まれています。
# データはCSV形式で提供されます。
# タスク
# データの読み込みと前処理：
# 
# Pandasを使用してCSVファイルからデータセットを読み込みます。
# 特徴（分子量、極性など）とターゲット（溶解度）にデータを分割します。
# データの正規化または標準化を行うことを検討します。
# ニューラルネットワークモデルの構築：
# 
# KerasやTensorFlowなどのライブラリを使用してニューラルネットワークモデルを構築します。
# 少なくとも一つの隠れ層を持つシンプルなモデルから始めます。
# 損失関数と最適化アルゴリズムを選択し、モデルをコンパイルします。
# モデルの訓練：
# 
# データを訓練セットとテストセットに分割します。
# ニューラルネットワークを訓練セットで訓練し、適切なエポック数とバッチサイズを選択します。
# モデルの評価と予測：
# 
# テストセットを使用してモデルの性能を評価します。
# 精度と損失を計算し、モデルの予測能力を確認します。
# 結果の解析：
# 
# 訓練とテストの結果を分析し、モデルの改善点を特定します。
# モデルが化学データのパターンをどの程度正しく認識しているかを考察します。
# =============================================================================

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt

# データセットの読み込み
data = pd.read_csv('data/Solubility_Dataset.csv')

# 特徴とターゲットの分割
X = data.drop('Solubility', axis=1)
y = data['Solubility']

# データの正規化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 訓練セットとテストセットに分割
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=0)

# ニューラルネットワークモデルの構築
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(X_train.shape[1],)))
model.add(Dense(32, activation='relu'))
model.add(Dense(1))

# モデルのコンパイル
model.compile(optimizer='adam', loss='mean_squared_error')

# モデルの訓練
model.fit(X_train, y_train, epochs=10, batch_size=32)

# モデルの評価
loss = model.evaluate(X_test, y_test)
print('Test Loss:', loss)

# いくつかのサンプルで予測を行う
predictions = model.predict(X_test[:5])
print('Predictions:', predictions)
print('Actual Values:', y_test[:5].values)

# 予測値と実際の値を抽出
num_samples = 5  # 表示するサンプル数
predictions_sample = model.predict(X_test[:num_samples]).flatten()
actual_values = y_test[:num_samples].values

# サンプルのインデックス
index = range(1, num_samples + 1)

# 棒グラフの作成
plt.figure(figsize=(10, 6))
plt.bar(index, actual_values, width=0.4, label='Actual Values', align='center')
plt.bar(index, predictions_sample, width=0.4, label='Predictions', align='edge')
plt.xlabel('Sample Index')
plt.ylabel('Solubility')
plt.title('Comparison of Predictions and Actual Values')
plt.legend()
plt.show()


