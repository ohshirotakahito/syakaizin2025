# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 00:29:54 2023

@author: toshiro
"""
#９．3Dグラフの作成:
#X、Y、Zデータを利用して、3Dサーフェスプロットを作成してください。次の条件を満たす3Dグラフを作成してください。
#　・X の範囲は [−5,5] で、50のデータポイントを持つ。
#　・Y の範囲は [−5,5] で、50のデータポイントを持つ。
#・Z は X と Y の関数として、Z = sin(√(x^2+y^2))

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# データ
X = np.linspace(-5, 5, 50)
Y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# 3Dグラフ
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)
plt.show()
