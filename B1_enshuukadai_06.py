# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 10:18:02 2023

@author: ohshi
"""

# =============================================================================
# ６．ソーティング:
# 
# 　Pandasのデータのソーティングを行います．Age列に基づいてデータフレームをソートしてください。データは以下のものを使います
# ・Name: 'Alice', 'Bob', 'Charlie'
# ・Age: 25, 30, 35
# =============================================================================

import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}
df = pd.DataFrame(data)

print(df)

sorted_df = df.sort_values(by='Age')

print(sorted_df)

