# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 13:28:55 2023

@author: ohshi
"""

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# データ生成関数
def generate_sine_wave_data(num_samples, num_steps, noise=False):
    X = np.linspace(0, 2 * np.pi, num_steps)
    data = np.array([np.sin(X + np.random.random() * 2 * np.pi) for _ in range(num_samples)])
    if noise:
        data += np.random.normal(0, 0.5, data.shape)  # ノイズの追加
    labels = np.zeros((num_samples, 1)) if not noise else np.ones((num_samples, 1))
    return data, labels

# パラメータ設定
num_samples = 1000  # サンプル数
num_steps = 50      # 時系列のステップ数
num_units = 50      # RNNユニット数

# データ生成
data_clean, labels_clean = generate_sine_wave_data(num_samples // 2, num_steps, noise=False)
data_noisy, labels_noisy = generate_sine_wave_data(num_samples // 2, num_steps, noise=True)

# データ結合
X = np.concatenate([data_clean, data_noisy], axis=0)
y = np.concatenate([labels_clean, labels_noisy], axis=0)

# データの形状変更
X = X.reshape((num_samples, num_steps, 1))

# データ分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# モデル構築
model = Sequential([
    SimpleRNN(num_units, input_shape=(num_steps, 1)),
    Dense(1, activation='sigmoid')
])

# モデルのコンパイル
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# モデルのトレーニング
#model.fit(X_train, y_train, epochs=10, batch_size=32, verbose=1)

history = model.fit(X_train, y_train, epochs=30, batch_size=32, verbose=1)

# エポックごとの損失と精度を取得
epoch_loss = history.history['loss']
epoch_accuracy = history.history['accuracy']

# 損失のプロット
plt.figure(figsize=(8, 4))
plt.plot(epoch_loss, label='Training Loss')
plt.title('Epoch vs Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.show()

# 精度のプロット
plt.figure(figsize=(8, 4))
plt.plot(epoch_accuracy, label='Training Accuracy')
plt.title('Epoch vs Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# モデルの評価
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Loss: {loss}, Test Accuracy: {accuracy}")