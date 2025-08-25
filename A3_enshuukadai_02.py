# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 10:18:02 2023

@author: ohshi
"""

#2. 文字列操作ツール:
#
#（課題）
#文字列を受け取り、逆順にする関数reverse_stringを作成する。
#同じ文字列を使って、母音の数を数える関数count_vowelsを作成する。
#これらの関数を使用して、与えられた文字列に対する詳細な分析を実行する。


def reverse_string(s):
    """ 文字列を逆順にする関数 """
    return s[::-1]

def count_vowels(s):
    """ 文字列内の母音の数を数える関数 """
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# 文字列の例
text = "Hello, World!"

# 文字列を逆順にする
reversed_text = reverse_string(text)
print(f"逆順の文字列: {reversed_text}")

# 文字列内の母音の数を数える
vowel_count = count_vowels(text)
print(f"母音の数: {vowel_count}")

