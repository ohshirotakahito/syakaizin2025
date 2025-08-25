# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 00:29:54 2023

@author: toshiro
"""
#８．凡例と注釈の追加:
#x = [1, 2, 3, 4, 5]、y1 = [2, 3, 5, 7, 11]、y2 = [1, 4, 9, 16, 25]のデータをプロットし、凡例と注釈を追加してください。

import matplotlib.pyplot as plt
# データ
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 9, 16, 25]


# グラフ
plt.plot(x, y1, label='Line 1')
plt.plot(x, y2, label='Line 2')
plt.legend()
plt.annotate('Annotation', xy=(3, 5), xytext=(4, 10),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()
