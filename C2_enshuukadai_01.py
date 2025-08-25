# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 00:29:54 2023

@author: toshiro
"""
#１．t検定:
#
#t検定は、2つのグループの平均値が統計的に異なるかどうかを評価します。以下の2つのサンプルデータセットが与えられたとき、t検定を利用して、これら2つのグループの平均値が統計的に異なるかどうかを判断してください。
#group1 = [12.23, 15.45, 14.67, 18.56, 14.29]
#group2 = [23.45, 25.67, 22.34, 21.56, 25.89]

import scipy.stats as stats

# サンプルデータセット
group1 = [12.23, 15.45, 14.67, 18.56, 14.29]
group2 = [23.45, 25.67, 22.34, 21.56, 25.89]

# t検定を実行
t_stat, p_value = stats.ttest_ind(group1, group2)

# 結果を表示
print(f'T-statistic: {t_stat}')
print(f'P-value: {p_value}')

# p値が0.05未満の場合、2つのグループの平均値は統計的に異なると結論付ける
if p_value < 0.05:
    print('The means of the two groups are statistically significantly different.')
else:
    print('The means of the two groups are not statistically significantly different.')


