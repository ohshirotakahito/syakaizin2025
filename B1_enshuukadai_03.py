# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 10:18:02 2023

@author: ohshi
"""

# =============================================================================
# ３．データのインポート:
# 
# 　任意のCSVファイルを読み込み、データフレームとして表示してください。
# 　この演習では，absorbance_data.csvを用いましょう．
# 
# =============================================================================

import pandas as pd

df_import = pd.read_csv('data/absorbance_data.csv')

print(df_import)