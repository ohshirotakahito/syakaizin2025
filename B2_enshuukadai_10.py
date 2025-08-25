# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 00:29:54 2023

@author: toshiro
"""
#１０．Seabornを使ったデータの可視化:
#Seabornライブラリを利用して、Titanicデータセットのペアプロットを作成してください。


import seaborn as sns
import matplotlib.pyplot as plt

# データ
data = sns.load_dataset('titanic')

# ペアプロット
sns.pairplot(data)
plt.show()