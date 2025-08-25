# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 22:30:35 2024

@author: qwert
"""
import numpy as np
import glob
import matplotlib.pyplot as plt
import os

filedir = 'dataset\\uv-vis\\' #各自のパスを入力、必要なら絶対パスで表記

#spec1.csv をプロットしてください。
file = filedir + 'spec1.csv'
file = 'dataset\\uv-vis\\spec1.csv'

data = np.loadtxt(file,delimiter = ',', skiprows =1 )

x = data[:,0]
y = data[:,1]

plt.plot(x,y)
plt.xlabel('Wavelength / nm')
plt.ylabel('Abs.')
plt.show()

#Spec1.csv-spec7.csvを全て別々のプロットをしてください。
files = glob.glob(filedir + '*.csv')
for file in files:
    data = np.loadtxt(file,delimiter = ',', skiprows =1 )
    
    x = data[:,0]
    y = data[:,1]
    
    plt.plot(x,y)
    plt.title(os.path.basename(file) ) # ディレクトリを含まないファイル名
    plt.xlabel('Wavelength / nm')
    plt.ylabel('Abs.')
    plt.show()

#同一のプロットですべてのスペクトルを表示してください。
for file in files:
    data = np.loadtxt(file,delimiter = ',', skiprows =1 )
    
    x = data[:,0]
    y = data[:,1]
    
    plt.plot(x,y,label= os.path.basename(file).replace('.csv','') )
plt.title('All' ) # ディレクトリを含まないファイル名
plt.xlabel('Wavelength / nm')
plt.ylabel('Abs.')
plt.legend()
plt.show()

#各スペクトルの最大値が１になるように規格化してから、プロットしてください。
for file in files:
    data = np.loadtxt(file,delimiter = ',', skiprows =1 )
    
    x = data[:,0]
    y = data[:,1]
    
    y = y/ np.max(y)
    
    plt.plot(x,y,label= os.path.basename(file).replace('.csv','') )
plt.title('All' ) # ディレクトリを含まないファイル名
plt.xlabel('Wavelength / nm')
plt.ylabel('Abs.')
plt.legend()
plt.show()
#250-300nmの範囲のみプロットしてください。
for file in files:
    data = np.loadtxt(file,delimiter = ',', skiprows =1 )
    
    x = data[:,0]
    y = data[:,1]
    
    
    plt.plot(x,y,label= os.path.basename(file).replace('.csv','') )
plt.title('All' ) # ディレクトリを含まないファイル名
plt.xlabel('Wavelength / nm')
plt.ylabel('Abs.')
plt.legend()
plt.xlim(250,300)

plt.show()


#横軸にスペクトル番号、縦軸に300nm以下の最大値をプロットしてください。
#上のグラフに300nm以上の最大値を追加してください
max_abs_under_300 = []
max_abs_over_300 = []
spec_num = []

for i,file in enumerate(files):
    data = np.loadtxt(file,delimiter = ',', skiprows =1 )
    
    x = data[:,0]
    y = data[:,1]
    
    max_abs_under_300.append( np.max(y[x < 300] ) )
    max_abs_over_300.append( np.max(y[x > 300] ) )
    spec_num.append(i+1)
    
plt.plot(spec_num,max_abs_under_300,'r') #ｒは赤
plt.plot(spec_num,max_abs_over_300,'b') # bは青
plt.xlabel('num')
plt.ylabel('Abs.')
plt.show()

#300nm以下、以上それぞれの領域で最大値をとる波長を求めてください。
for file in files:
    data = np.loadtxt(file,delimiter = ',', skiprows =1 )
    
    x = data[:,0]
    y = data[:,1]
    
    print(file)
    peak_index_under_300 = np.argmax(y[x<300] )
    print("300以下で最大をとる波長は", x[x<300][peak_index_under_300] )
    peak_index_over_300 = np.argmax(y[x>300] )
    print("300以上で最大をとる波長は", x[x>300][peak_index_over_300] )
    
    