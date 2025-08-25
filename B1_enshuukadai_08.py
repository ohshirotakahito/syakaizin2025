# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 10:18:02 2023

@author: ohshi
"""

# =============================================================================
# ８．欠損値の処理:
# 
# 　任意の欠損値を含むデータフレームを作成し、欠損値を0で埋めてください。データとしては以下のものを用います．
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, np.nan, 35]
# 
# =============================================================================

import numpy as np
import pandas as pd

data_missing = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, np.nan, 35]
}

df_missing = pd.DataFrame(data_missing)

print(df_missing)

df_filled = df_missing.fillna(0)

print(df_filled)

