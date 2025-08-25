# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 00:19:54 2023

@author: toshiro
"""
# =============================================================================
# 10.機械学習(ディープニューラルネットワーク)を使用した新規材料の耐久度予測
# 背景
# 新型樹脂材料の開発において、耐久度の予測は重要な要素です。この演習では、深層学習を用いて、材料A、B、Cの異なる混合比率に基づいて、新規材料の耐久度を予測するモデルを構築します。
# 
# データセット
# 提供されるデータセットには、以下の情報が含まれます：
# 
# 既存材料の耐久性 (年)
# 材料A、B、Cの混合比率 (%)
# 引張強度 (MPa)
# 熱耐性 (°C)
# 弾性率 (GPa)
# 硬度 (モース硬度)
# 耐食性 (スケール1-10)
# 電気伝導率 (S/m)
# 密度 (g/cm^3)
# 
# ータセット名 (material_science_dataset.csv, material_science_dataset1.csv, material_science_dataset2.csv, material_science_dataset3.csv)
# 
# 的
# ディープニューラルネットワークを使用して、材料A、B、Cの混合比率に基づいて新規材料の耐久度を予測する。
# 
# 手順
# データセットを読み込み、特徴量とターゲットを選択する。
# データを標準化し、訓練データとテストデータに分割する。
# ディープニューラルネットワークモデルを構築し、訓練する。
# モデルを評価し、平均二乗誤差（MSE）を計算する。
# 学習済みモデルとスケーラーを使用して、任意の混合比率から予測された耐久度を算出する。
# 期待される成果
# 混合比率に基づいた新規材料の耐久度の予測値。
# ディープニューラルネットワークを用いた耐久度予測モデルの構築と評価。
# =============================================================================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

# データセットの読み込み
df = pd.read_csv('data/material_science_dataset1.csv')

# 特徴量とターゲットの選択
features = df.drop(['Existing_Durability_Years'], axis=1)
target = df['Existing_Durability_Years']

# データの標準化
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# 訓練データとテストデータに分割
X_train, X_test, y_train, y_test = train_test_split(features_scaled, target, test_size=0.2, random_state=0)

# モデルの構築
model = Sequential()
model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='linear'))

# モデルのコンパイル
model.compile(loss='mean_squared_error', optimizer=Adam(learning_rate=0.001))

# モデルの訓練
model.fit(X_train, y_train, epochs=100, batch_size=10, verbose=1)

# モデルの評価
mse = model.evaluate(X_test, y_test, verbose=0)
print(f"Mean Squared Error: {mse}")

def predict_durability(model, scaler, mixture_ratios, original_columns):
    # 混合比率を含むDataFrameを作成
    mixture_df = pd.DataFrame([mixture_ratios])

    # 残りの特徴量を平均値で埋める
    for col in original_columns:
        if col not in mixture_df.columns:
            mixture_df[col] = features[col].mean()

    # 特徴量の順序を訓練データと同じ順序にする
    mixture_df = mixture_df[original_columns]

    # 特徴量のスケーリング
    mixture_df_scaled = scaler.transform(mixture_df)

    # 予測された耐久性を返す
    predicted_durability = model.predict(mixture_df_scaled)[0]
    return predicted_durability

# 例：材料の混合比率を入力して耐久度を予測
mixture_ratios = {'Mixture_Ratio_A_Percent': 10, 'Mixture_Ratio_B_Percent': 30, 'Mixture_Ratio_C_Percent': 30}

# 予測の際に元の特徴量の列名を渡す
predicted_durability = predict_durability(model, scaler, mixture_ratios, features.columns)
print(f"Predicted Durability: {predicted_durability[0]:.2f} years")

