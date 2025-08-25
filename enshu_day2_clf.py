# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 08:16:41 2024

@author: qwert
"""

import numpy as np
import matplotlib.pyplot as plt
import glob
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans,DBSCAN
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix

#spectraに全てのスペクトルを読み込む
filedir = 'dataset\\classification1\\'
train_files = glob.glob(filedir + 'train\\*.csv')
test_files = glob.glob(filedir + 'test\\*.csv')


spectra = []
for i in range(len(train_files) ):
    file = filedir + 'train\\spec' + str(i) + '.csv'
    data = np.loadtxt(file,delimiter=',',skiprows=1)
    
    wavelength = data[:,0]
    absorbance = data[:,1]
    
    spectra.append(absorbance)
    
x_train = np.array(spectra)

y_train = np.loadtxt(filedir + 'train\\label.txt',dtype = "unicode_")

print('Train data loaded')
spectra = []
for i in range(len(test_files)):
    file = filedir + 'test\\spec' + str(i) + '.csv'
    data = np.loadtxt(file,delimiter=',',skiprows=1)
    
    wavelength = data[:,0]
    absorbance = data[:,1]
    
    spectra.append(absorbance)

x_test = np.array(spectra)
y_test = np.loadtxt(filedir + 'test\\label.txt',dtype = "unicode_")
print('Test data loaded')

#Random Forestを呼び出し
clf = RandomForestClassifier()

#Random Forestを学習
clf.fit(x_train,y_train)

#学習した分類機で識別
y_pred = clf.predict(x_test)

#Confusion matrixを作成
CM = confusion_matrix(y_test,y_pred)
print(CM)





