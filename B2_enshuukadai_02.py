# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 00:29:54 2023

@author: toshiro
"""
#2.ヒストグラムの作成:
#以下のデータセットに対して、'Age'列のヒストグラムを作成してください。
#data = {'Age': [23, 45, 34, 30, 25, 40, 35, 50, 45]}

import matplotlib.pyplot as plt
# データ
data = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]

# ヒストグラム
plt.hist(data, bins=4)
plt.show()

