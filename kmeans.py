# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 15:24:54 2024

@author: komoto_univ
"""

import numpy as np
import matplotlib.pyplot as plt

mean1 = np.array([0,0])
mean2 = np.array([100,0])
mean3 = np.array([50,5])

cov1 = np.array([[100,0],[0,5]])
cov2 = np.array([[100,0],[0,5]])
cov3 = np.array([[100,0],[0,5]])


mean1 = np.array([0,0])
mean2 = np.array([5,0])
mean3 = np.array([2.5,2.5])

cov1 = np.array([[1,0],[0,1]])
cov2 = np.array([[1,0],[0,1]])
cov3 = np.array([[1,0],[0,1]])

mean1 = np.array([0,0])
mean2 = np.array([10,10])
mean3 = np.array([1,100])

cov1 = np.array([[1,0],[0,100]])
cov2 = np.array([[1,0],[0,100]])
cov3 = np.array([[1,0],[00,100]])

gen = np.random.default_rng()
data1 = gen.multivariate_normal(mean1, cov1,size=100)
data2 = gen.multivariate_normal(mean2, cov2,size=100)
data3 = gen.multivariate_normal(mean3, cov3,size=100)

data= np.concatenate((data1,data2,data3) )



plt.plot(data1[:,0],data1[:,1] , '.' )
plt.plot(data2[:,0],data2[:,1] , '.' )
plt.plot(data3[:,0],data3[:,1] , '.' )
#plt.plot(data[:,0],data[:,1] , 'k.' )
plt.show() 


"""
k-means
1. クラスター数を設定
2.　ランダムに設定したクラスター数にクラスターを設定
3. 各クラスターの重心（平均）を求める
4. 最もクラスターの重心に近いクラスターに変更
5.　3,4を繰り返し、変化がなくなったら終了
"""

# 1. クラスター数を設定
n_clusters=3

#2.　ランダムに設定したクラスター数にクラスターを設定
clusters = np.random.randint(n_clusters,size= len(data), dtype=int )


while True: # 3,4の繰り返し
    #3. 各クラスターの重心（平均）を求める
    centers = np.array([ np.average(data[clusters == i] ,axis=0) for i in range(n_clusters)] )

    #クラスターの様子を確認
    for i in range(3):
        plt.plot(data[clusters == i][:,0], data[clusters == i][:,1] , '.' )
    plt.show()

    #4. 最もクラスターの重心に近いクラスターに変更
    new_clusters = []
    for d in data:
        min_norm = np.sum((centers[0] - d)**2 )
        cluster = 0
        for i in range(1,n_clusters):
            norm = np.sum((centers[i] - d)**2 )
            
            if norm < min_norm:
                min_norm = norm
                cluster = i
        new_clusters.append(cluster )
    new_clusters = np.array(new_clusters)
    
    #5. 割り当てたクラスターの変化がないかの判定
    if np.all(new_clusters==clusters) :                     
        break #もしなければ終了
        
    else:
        clusters = new_clusters #まだ変化がある場合、クラスターを更新





