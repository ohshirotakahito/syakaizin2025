# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 10:18:02 2023

@author: ohshi
"""

# =============================================================================
# ５．フィルタリング:
# 
# 　Pandasのデータのフィルタリングを行います． Age列が30以上の行だけを抽出してください。データは以下のものを使います
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

filtered_df = df[df['Age'] >= 30]

print(filtered_df)


