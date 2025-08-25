# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 00:22:33 2024

@author: qwert
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 18:56:49 2024

@author: komoto_univ
"""

import numpy as np
import matplotlib.pyplot as plt
import glob
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans,DBSCAN

#spectraに100個のスペクトルを読み込む
files = glob.glob('dataset/PCA_Cluster/*.csv')

spectra = []
for file in files:
    data = np.loadtxt(file,delimiter=',',skiprows=1)
    
    x = data[:,0]
    y = data[:,1]
    
    spectra.append(y)
    
spectra = np.array(spectra)

#PCAを使って2次元に削減
n = 2
pca = PCA(n_components=n)

rec_X = pca.fit_transform(spectra)

#寄与度を確認
plt.plot(pca.explained_variance_)
plt.xlabel('ith components')
plt.ylabel('explained_variance_')
plt.show()

#主成分ベクトルを確認
for i in range(n):
    plt.plot(x,pca.components_[i])
    plt.xlabel('wavelength / nm')
    
    plt.title('PC'+str(i) )
    plt.show()

#i番目のスペクトルを主成分から再構成
i=5
spectrum = spectra[i]
rec = rec_X[i]

#for spectrum,rec in zip(spectra,rec_X) :
plt.plot(x,spectrum,'k',label='raw')

rec_spec = pca.mean_ + rec@pca.components_

plt.plot(x,rec_spec,'r',label='reconstructed')

plt.legend()
plt.xlabel('wavelength / nm')
plt.ylabel('Absorbance')
plt.show()

#2次元の散布図を作成
plt.scatter(rec_X[:,0],rec_X[:,1])
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.show()

#k-meansを使ってクラスタリング、（クラスタ数３）
n_clusters = 3
alg = KMeans(n_clusters = n_clusters)
#alg = DBSCAN(eps = 2)
clusters = alg.fit_predict(rec_X)

#クラスターごとに色分けして散布図をプロット
for i in range(n_clusters):
    plt.scatter(rec_X[:,0][clusters==i],rec_X[:,1][clusters==i])
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.show()



