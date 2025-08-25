# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 00:29:54 2023

@author: toshiro
"""
#4. 吸光度データの線形回帰:
#
#吸光度データに対して線形回帰を行い、回帰式を求めてください。実験データは以下のものを用いてください．
# ・'Concentration (mol/L)': [0.1, 0.2, 0.3, 0.4, 0.5],
# ・'Absorbance': [0.15, 0.30, 0.45, 0.60, 0.75]


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = np.array([0.1, 0.2, 0.3, 0.4, 0.5]).reshape(-1, 1)
y = np.array([0.15, 0.30, 0.45, 0.60, 0.75])

reg = LinearRegression().fit(X, y)
slope = reg.coef_[0]
intercept = reg.intercept_

print(f"Regression Equation: y = {slope:.3f}x + {intercept:.3f}")

plt.scatter(X, y, color='blue', label='Data points')
plt.plot(X, reg.predict(X), color='red', label='Regression Line')
plt.xlabel('Concentration (mol/L)')
plt.ylabel('Absorbance')
plt.title('Linear Regression for Absorbance vs Concentration')
plt.legend()
plt.grid(True)
plt.show()

