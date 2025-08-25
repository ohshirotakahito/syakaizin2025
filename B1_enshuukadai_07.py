# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 10:18:02 2023

@author: ohshi
"""

# =============================================================================
# ７．集計:
# 　Pandasのデータの集計を行います．Age列の平均値を計算してください。データは以下のものを使います
# ・Name: 'Alice', 'Bob', 'Charlie'
# ・Age: 25, 30, 35
# 
# =============================================================================

import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}
df = pd.DataFrame(data)

print(df)

average_age = df['Age'].mean()

print(average_age)


