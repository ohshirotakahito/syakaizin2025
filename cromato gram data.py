# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 02:16:38 2023

@author: toshiro
"""
import numpy as np
import matplotlib.pyplot as plt

# パラメータ設定
time = np.linspace(0, 15, 1000)  # 0-10分の間でデータを取得
baseline = 5

# 3つのピークをシミュレート
peak_centers = [3, 5, 8, 9.5]  # 保持時間
peak_heights = [10, 15, 7,9]  # ピークの高さ
peak_widths = [0.1, 0.3, 0.3, 0.5]
signal = baseline + np.zeros_like(time)

for center, height, width in zip(peak_centers, peak_heights, peak_widths):
    signal += height * np.exp(-((time - center)**2) / (2 * width**2))

# プロット
plt.plot(time, signal)
plt.xlabel('Retention Time (min)')
plt.ylabel('Signal Intensity')
plt.title('Simulated Chromatogram')
plt.grid(True)
plt.show()

# データをDataFrameに変換
#data = pd.DataFrame({'Time': time, 'Intensity': signal})

# CSVファイルに保存
#data.to_csv('chromato_data.csv', index=False)