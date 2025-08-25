# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 10:18:02 2023

@author: ohshi
"""

# =============================================================================
# １０．データの結合:
# 
# 　2つのデータフレームを作成し、それらを結合して新しいデータフレームを作成してください。データは以下のものを用いてください
# ・data1:
# 　Name: 'David', 'Edward', 'Fiona'
# 　Age: 40, 45, 50
# ・data2:
# 　Name: 'George', 'Hannah', 'Ian'
# 　Age: 55, 60, 65
# =============================================================================


import pandas as pd

data1 = {'Name': ['David', 'Edward', 'Fiona'], 'Age': [40, 45, 50]}
data2 = {'Name': ['George', 'Hannah', 'Ian'], 'Age': [55, 60, 65]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print(df1, df2)

df_combined = pd.concat([df1, df2], ignore_index=True)

print(df_combined)