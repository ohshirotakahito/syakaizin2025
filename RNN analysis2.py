# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 14:28:41 2023

@author: ohshi
"""

from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense
import matplotlib.pyplot as plt
import pandas as pd

# Reading the newly uploaded CSV file and plotting the data
df = pd.read_csv('data/time_series_data.csv')


# データの形状変更
num_samples, num_steps = df.shape[0], 50  # サンプル数とステップ数を設定
X = df.drop('label', axis=1).values.reshape(num_samples, num_steps, 1)
y = df['label'].values

# データ分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# モデル構築
num_units = 50  # RNNユニット数
model = Sequential([
    SimpleRNN(num_units, input_shape=(num_steps, 1)),
    Dense(1, activation='sigmoid')
])

# モデルのコンパイル
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# モデルのトレーニング
history = model.fit(X_train, y_train, epochs=100, batch_size=32, verbose=1)

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