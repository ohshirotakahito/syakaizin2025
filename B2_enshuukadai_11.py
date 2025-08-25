# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 00:29:54 2023

@author: toshiro
"""
#１１．Seabornを使ったヒートマップの作成:
#Seabornライブラリを使用して、10x12のランダムなデータを持つヒートマップを作成してください。ランダムなデータはuniform_data = np.random.rand(10, 12)をもちいてください。

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# データ
uniform_data = np.random.rand(10, 12)

# ヒートマップ
sns.heatmap(uniform_data)
plt.show()
