# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 00:29:54 2023

@author: toshiro
"""
#７．グラフのカスタマイズ:
#x = [1, 2, 3, 4, 5]、y1 = [2, 3, 5, 7, 11]、y2 = [1, 4, 9, 16, 25]のデータを利用して、グラフのタイトル、軸ラベル、グリッドをカスタマイズしてください。

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]


# プロット
plt.plot(x, y)
plt.title('Title Here')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.grid(True)
plt.show()
