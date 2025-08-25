# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 00:29:54 2023

@author: toshiro
"""
#6.複数のグラフを一つの図に表示:
#x = [1, 2, 3, 4, 5]、y1 = [2, 3, 5, 7, 11]、y2 = [1, 4, 9, 16, 25]のデータを利用して、2つのグラフを一つの図に表示してください。


import matplotlib.pyplot as plt
# データ
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 9, 16, 25]

# グラフ（同一グラフ上に描画）
plt.plot(x, y1, label='y1')  # ラベルを追加して、凡例に表示させることができます。
plt.plot(x, y2, label='y2')  # 同様にy2に対してもラベルを追加。

# 凡例の表示
plt.legend()

# グラフを表示
plt.show()

