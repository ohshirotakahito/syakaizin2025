# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 00:29:54 2023

@author: toshiro
"""
#4.箱ひげ図の作成:
#以下のデータセットに対して、'Gender'に応じた'Age'の箱ひげ図を作成してください。
#data = {'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'], 'Age': [23, 45, 34, 30, 25]}


import matplotlib.pyplot as plt
# データ
data = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]

# 箱ひげ図
plt.boxplot(data)
plt.show()
