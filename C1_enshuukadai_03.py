# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 00:29:54 2023

@author: toshiro
"""
#3. 吸光度データの計算:
#    
#以下の吸光度の実験データより、吸光度と濃度の関係を計算してください。
#・'Concentration (mol/L)': [0.1, 0.2, 0.3, 0.4, 0.5],
#・'Absorbance': [0.15, 0.30, 0.45, 0.60, 0.75]

import numpy as np
import matplotlib.pyplot as plt

concentration = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
absorbance = np.array([0.15, 0.30, 0.45, 0.60, 0.75])

# Plotting the relationship
plt.plot(concentration, absorbance, 'o-', label="Experimental Data")
plt.xlabel('Concentration (mol/L)')
plt.ylabel('Absorbance')
plt.title('Absorbance vs. Concentration')
plt.legend()
plt.grid(True)
plt.show()
