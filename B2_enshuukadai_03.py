# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 00:29:54 2023

@author: toshiro
"""
#3.棒グラフの作成:
#categories = ['Category1', 'Category2', 'Category3']、values = [4, 7, 1]のデータを利用して、棒グラフを作成してください。


import matplotlib.pyplot as plt
# データ
categories = ['Category1', 'Category2', 'Category3']
values = [4, 7, 1]

# 棒グラフ
plt.bar(categories, values)
plt.show()
