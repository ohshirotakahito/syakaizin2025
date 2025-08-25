# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 00:29:54 2023

@author: toshiro
"""
#1. データの可視化:
#Matplotlibを利用して、x = [1, 2, 3, 4, 5]、y = [2, 3, 5, 7, 11]のデータをプロットしてください。
import matplotlib.pyplot as plt

# データ
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# プロット
plt.plot(x, y)
plt.show()