# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 07:06:08 2024

@author: ohshi
"""

import cv2
import numpy as np
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt

# 手書き文字画像の読み込み関数
def preprocess_image(image_path):
    # 画像をグレースケールで読み込み
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # 画像を28x28ピクセルにリサイズ
    img_resized = cv2.resize(img, (28, 28))
    
    # 画像の色を反転（白背景に黒文字なら）
    img_resized = cv2.bitwise_not(img_resized)
    
    # 画像の正規化（0-1にスケーリング）
    img_normalized = img_resized / 255.0
    
    # 形状をMNISTの形式に変換 (1, 28, 28) → 1枚の画像として認識させるため
    img_reshaped = np.reshape(img_normalized, (1, 28, 28))
    
    return img_reshaped

# 手書き文字画像のパスを指定
image_path = 'data/tegaki7.png'

# 画像の前処理
processed_image = preprocess_image(image_path)

# 前処理後の画像を表示して確認
plt.imshow(processed_image[0], cmap='gray')
plt.show()

# 学習済みモデルの読み込み
model = load_model('data/mnist_model.h5')

# 手書き画像の予測
predictions = model.predict(processed_image)

# 予測結果の出力
predicted_digit = np.argmax(predictions)
print(f'予測された数字は: {predicted_digit}')
