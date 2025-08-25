# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 10:18:02 2023

@author: ohshi
"""

# =============================================================================
# ９．列の追加と削除:
# 
# 　新しい列Cityをデータフレームに追加し、任意の値を割り当ててください。その後、City列を削除してください。もともとのデータとして以下のものを用います．
#  'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 35]
# 追加するCityのデータは以下のものです．
# 'City'：['New York', 'Los Angeles', 'Chicago']
# 
# =============================================================================

import numpy as np
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}
df = pd.DataFrame(data)

print(df)


df['City'] = ['New York', 'Los Angeles', 'Chicago']

print(df)

df = df.drop(columns=['City'])

print(df)
