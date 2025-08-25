# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 06:58:27 2024

@author: ohshi
"""

import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt


# MNISTデータセットの読み込み
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# データを正規化（0〜255の範囲を0〜1に）
x_train, x_test = x_train / 255.0, x_test / 255.0

# モデルの定義（シンプルなニューラルネットワーク）
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(10, activation='softmax')
])

# モデルのコンパイル
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# モデルの訓練
model.fit(x_train, y_train, epochs=5)

# テストデータで精度を評価
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f'\nテスト精度: {test_acc}')

# 学習済みモデルの保存（後で使うため）
model.save('data/mnist_model.h5')

