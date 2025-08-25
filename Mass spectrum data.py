# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 20:32:51 2023

@author: toshiro
"""
import numpy as np
import matplotlib.pyplot as plt

# パラメータ設定
mz = np.linspace(50, 500, 1000)  # m/z 50-500の範囲でデータを取得

# 4つのピークをシミュレート
peak_centers = [100, 200, 300, 450]  # m/z
peak_heights = [500, 1000, 600, 250]  # ピークの高さ
peak_widths = [0.5, 1, 0.8, 1.5]  # ピークの幅

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
