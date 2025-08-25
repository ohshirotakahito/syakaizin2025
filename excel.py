# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 09:43:43 2024

@author: ohshi
"""

import pandas as pd

def read_excel(file):
    input_book = pd.ExcelFile(file)

    df = pd.DataFrame()

    for sheet in input_book.sheet_names:
        temp_df = input_book.parse(sheet)

        df = pd.concat([df,temp_df])
    return df

file = 'data/Book1.xlsx'

print(read_excel(file) )