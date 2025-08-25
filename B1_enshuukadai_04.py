# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 10:18:02 2023

@author: ohshi
"""

# =============================================================================
# ４．データのエクスポート:
# 　作成したPandasデータフレームをCSVファイルとして保存してください。
# 　この演習では，absorbance_data.csvを読み込み，これを新しい名前（output.csv）をつけて，保存してみましょう．
# 
# =============================================================================

import pandas as pd

#データのインポート
df= pd.read_csv('data/absorbance_data.csv')

print(df)

#インポートデータのエクスポート
df.to_csv('data/output.csv', index=False)
