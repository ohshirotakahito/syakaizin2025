# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 00:29:54 2023

@author: toshiro
"""
#5.散布図の作成:
#以下のデータセットに対して、'Gender'に応じた'Age'の箱ひげ図を作成してください。
#data = {'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'], 'Age': [23, 45, 34, 30, 25]}

import matplotlib.pyplot as plt
# データ
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]

# 散布図
plt.scatter(x, y)
plt.show()

