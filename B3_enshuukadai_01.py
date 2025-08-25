# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 13:06:31 2023

@author: ohshi
"""

# =============================================================================
# 1.気候変動データの長期的な傾向分析
# 課題の背景
# 近年、気候変動は重要な環境問題となっています。この問題を理解するためには、過去の気候データを分析し、長期的な傾向を把握することが重要です。
# 
# 課題
# 1910年から2010年までの気温、太陽黒点、森林面積、工業生産高のデータを用いて、以下の分析を行います。
# 
# データの読み込みと概観：
# 
# 提供されたCSVファイルからデータを読み込み、基本的な統計情報を確認します。
# データの可視化：
# 
# 気温、太陽黒点、森林面積、工業生産高の時間に対する変化を可視化します。
# 各変数の年間の変化傾向を把握するために、折れ線グラフや散布図を作成します。
# データの相関分析：
# 
# 気温と他の変数（太陽黒点、森林面積、工業生産高）との相関を分析します。
# 相関関係を可視化するために、散布図やヒートマップを使用します。
# 結論の導出：
# 
# 分析結果を基に、気温の長期的な傾向や他の変数との関連性について結論を導き出します。
# データセット
# Climate_Data.csv：1910年から2010年までの気温、太陽黒点、森林面積、工業生産高を含むデータセット。
# 
# 
# =============================================================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# データの読み込み
data = pd.read_csv('data/Climate_Data.csv')

# データの概観
print(data.describe())

# データの可視化
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
plt.plot(data['Year'], data['Temperature'], label='Temperature')
plt.xlabel('Year')
plt.ylabel('Temperature')
plt.title('Temperature Over Years')

plt.subplot(2, 2, 2)
plt.plot(data['Year'], data['Sunspots'], label='Sunspots')
plt.xlabel('Year')
plt.ylabel('Sunspots')
plt.title('Sunspots Over Years')

plt.subplot(2, 2, 3)
plt.plot(data['Year'], data['Forest Area'], label='Forest Area')
plt.xlabel('Year')
plt.ylabel('Forest Area')
plt.title('Forest Area Over Years')

plt.subplot(2, 2, 4)
plt.plot(data['Year'], data['Industrial Output'], label='Industrial Output')
plt.xlabel('Year')
plt.ylabel('Industrial Output')
plt.title('Industrial Output Over Years')

plt.tight_layout()
plt.show()

# 相関分析
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True)
plt.title('Correlation Analysis')
plt.show()
