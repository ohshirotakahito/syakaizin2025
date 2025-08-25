# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 02:13:39 2023

@author: toshiro
"""
import numpy as np
import matplotlib.pyplot as plt

# CVパラメータ
start_potential = -0.2  # 開始電圧 (V)
vertex_potential = 0.2  # 頂点電圧 (V)
scan_rate = 0.1  # スキャン速度 (V/s)
points_per_volt = 100  # 電圧1Vあたりのポイント数

# シミュレーションパラメータ
E0 = 0.0  # 標準電極ポテンシャル (V)
alpha = 0.5  # 電荷移動係数
n = 1  # 電子の数
F = 96485  # ファラデー定数 (C/mol)
R = 8.314  # 気体定数 (J/(mol*K))
T = 298  # 温度 (K)

# 電圧範囲の生成
total_volt_range = abs(start_potential - vertex_potential) * 2
total_points = int(total_volt_range * points_per_volt)
potential_step = total_volt_range / total_points

forward_potentials = np.arange(start_potential, vertex_potential, potential_step)
reverse_potentials = np.arange(vertex_potential, start_potential, -potential_step)
potentials = np.concatenate((forward_potentials, reverse_potentials))

# 電流計算関数
def calculate_current(E, E0, alpha, n, F, R, T, scan_rate):
    k0 = 1  # 標準速度定数 (cm/s)
    ks = k0 * np.exp(-alpha * n * F * (E - E0) / (R * T))  # 酸化または還元速度定数
    current_density = n * F * ks  # 電流密度 (A/cm^2)
    return current_density

# CVカーブ生成
currents = np.array([calculate_current(E, E0, alpha, n, F, R, T, scan_rate) for E in potentials])

# プロット
plt.plot(potentials, currents)
plt.xlabel('Potential (V)')
plt.ylabel('Current (A/cm^2)')
plt.title('Cyclic Voltammetry (CV) Simulation')
plt.grid(True)
plt.show()
