# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 13:19:43 2023

@author: ohshi
"""

import numpy as np
import matplotlib.pyplot as plt

def generate_sine_wave_data(num_samples, num_steps, noise=False):
    """
    正弦波時系列データを生成する関数。
    :param num_samples: サンプルの数
    :param num_steps: 各サンプルの時系列の長さ
    :param noise: ノイズを追加するかどうか
    :return: 時系列データと対応するラベル
    """
    X = np.linspace(0, 2 * np.pi, num_steps)
    data = np.array([np.sin(X + np.random.random() * 2 * np.pi) for _ in range(num_samples)])
    
    if noise:
        data += np.random.normal(0, 0.5, data.shape)  # ノイズの追加

    labels = np.zeros((num_samples, 1)) if not noise else np.ones((num_samples, 1))
    return data, labels

# パラメータ設定
num_samples = 100  # サンプル数
num_steps = 50     # 時系列のステップ数

# データ生成
data_clean, labels_clean = generate_sine_wave_data(num_samples, num_steps, noise=False)
data_noisy, labels_noisy = generate_sine_wave_data(num_samples, num_steps, noise=True)

# データの可視化（例として最初の5つのサンプルを表示）
for i in range(10):
    plt.plot(data_clean[i], label=f'Clean {i}')
    plt.plot(data_noisy[i], label=f'Noisy {i}')
plt.xlabel('Time Steps')
plt.ylabel('Amplitude')
plt.legend()
plt.show()