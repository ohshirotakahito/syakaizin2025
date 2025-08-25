# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 18:56:49 2024

@author: komoto_univ
"""

import numpy as np
import matplotlib.pyplot as plt
import glob
from sklearn.decomposition import PCA

files = glob.glob('dataset/uv-vis/*.csv')

spectra = []
for file in files:
    data = np.loadtxt(file,delimiter=',',skiprows=1)
    
    x = data[:,0]
    y = data[:,1]
    
    spectra.append(y)
    
spectra = np.array(spectra)

n = 2
pca = PCA(n_components=n)

rec_X = pca.fit_transform(spectra)

plt.plot(pca.explained_variance_)
plt.xlabel('ith components')
plt.ylabel('explained_variance_')
plt.show()

for i in range(n):
    plt.plot(x,pca.components_[i])
    plt.xlabel('wavelength / nm')
    
    plt.title('PC'+str(i) )
    plt.show()

for spectrum,rec in zip(spectra,rec_X) :
    plt.plot(x,spectrum,'k',label='raw')
    
    rec_spec = pca.mean_ + rec@pca.components_
    
    plt.plot(x,rec_spec,'r',label='reconstructed')

    plt.legend()
    plt.xlabel('wavelength / nm')
    plt.ylabel('Absorbance')
    plt.show()
    
plt.scatter(rec_X[:,0],rec_X[:,1])
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.show()

