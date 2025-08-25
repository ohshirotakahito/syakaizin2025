# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 20:32:51 2023

@author: toshiro
"""
import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd

# パラメータ設定
mz = np.linspace(50, 500, 1000)  # m/z 50-500の範囲でデータを取得

# 4つのピークをシミュレート
peak_centers = [108, 122, 130, 168, 180, 238, 289, 371, 454]  # m/z

#ピークの数を作成
list_size = len(peak_centers)

# peak_heightsの大きさを100以上2000以下でランダムに決定
peak_heights = [random.randint(150, 2000) for _ in range(list_size)]

# peak_widthsの大きさを100以上2000以下でランダムに決定
peak_widths = random_floats = [random.uniform(0.5, 1.5) for _ in range(list_size)]


intensity = np.zeros_like(mz)

for center, height, width in zip(peak_centers, peak_heights, peak_widths):
    intensity += height * np.exp(-((mz - center)**2) / (2 * width**2))

# ノイズを追加
noise_level = 50  # ノイズの大きさを調整
noise = np.random.normal(0, noise_level, mz.shape)
intensity += noise

# プロット
plt.plot(mz, intensity)
plt.xlabel('m/z')
plt.ylabel('Intensity')
plt.title('Simulated Mass Spectrum with Noise')
plt.grid(True)
plt.show()

# データをDataFrameに変換
data = pd.DataFrame({'m/z': mz, 'Intensity': intensity})

# CSVファイルに保存
data.to_csv('data/ms_spectrum_data.csv', index=False)
