# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 10:18:02 2023

@author: ohshi
"""

# =============================================================================
# ２．Pandasデータフレームの作成:
# 
# 　Pandasを使用して、以下のデータを持つデータフレームを作成してください。
# 
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