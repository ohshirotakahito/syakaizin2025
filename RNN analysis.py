# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 12:20:41 2023

@author: ohshi
"""

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# データ生成（サンプル）
def generate_data(num_samples, num_steps):
    X = np.random.rand(num_samples, num_steps, 1)
    y = np.random.randint(0, 2, num_samples)
    return X, y

# パラメータ設定
num_samples = 1000  # サンプル数
num_steps = 10      # 時系列のステップ数
num_units = 50      # RNNユニット数

# データ生成
X, y = generate_data(num_samples, num_steps)
y = to_categorical(y)  # ラベルをone-hotエンコーディング

# データ分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# モデル構築
model = Sequential([
    SimpleRNN(num_units, input_shape=(num_steps, 1)),  # RNNレイヤー
    Dense(2, activation='softmax')                     # 出力レイヤー
])

# モデルのコンパイル
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# モデルのトレーニング
history = model.fit(X_train, y_train, validation_split=0.1, epochs=10, batch_size=32)

# モデルの評価
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Loss: {loss}, Test Accuracy: {accuracy}")

# 混同行列と分類レポート
y_pred = model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis=1)
y_true_classes = np.argmax(y_test, axis=1)

print(confusion_matrix(y_true_classes, y_pred_classes))
print(classification_report(y_true_classes, y_pred_classes))

