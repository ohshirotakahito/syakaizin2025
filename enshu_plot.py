# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 18:35:33 2024

@author: komoto_univ
"""
import numpy as np
import matplotlib.pyplot as plt
import glob

files = glob.glob('dataset/uv-vis/*.csv')

for file in files:
    data = np.loadtxt(file,delimiter=',',skiprows=1)
    
    x = data[:,0]
    y = data[:,1]
    
    plt.plot(x,y)
plt.show()

