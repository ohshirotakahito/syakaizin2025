# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 00:19:54 2023

@author: toshiro
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

# データセットの読み込み
df = pd.read_csv('data/material_science_dataset3.csv')

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

def predict_durability(model, scaler, mixture_ratios):
    # 混合比率を含むDataFrameを作成
    mixture_df = pd.DataFrame([mixture_ratios], columns=['Mixture_Ratio_A_Percent', 'Mixture_Ratio_B_Percent', 'Mixture_Ratio_C_Percent'])
    
    # 残りの特徴量を平均値で埋める
    for col in features.columns:
        if col not in mixture_df.columns:
            mixture_df[col] = features[col].mean()

    # 特徴量のスケーリング
    mixture_df_scaled = scaler.transform(mixture_df)

    # 予測された耐久性を返す
    predicted_durability = model.predict(mixture_df_scaled)[0]
    return predicted_durability

# 例：材料の混合比率を入力して耐久度を予測
mixture_ratios = {'Mixture_Ratio_A_Percent': 10, 'Mixture_Ratio_B_Percent': 30, 'Mixture_Ratio_C_Percent': 30}
predicted_durability = predict_durability(model, scaler, mixture_ratios)
print(f"Predicted Durability: {predicted_durability[0]:.2f} years")
