# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 22:29:05 2023

@author: toshiro
"""
import numpy as np
from skimage import io, filters, measure, morphology, segmentation, color
from skimage.feature import peak_local_max
from scipy import ndimage as ndi
import matplotlib.pyplot as plt

def count_particles(image_path):
    # 画像の読み込み
    image = io.imread(image_path)
    
    # 画像がカラーならグレースケールに変換
    if image.ndim == 3:
        print("Converting color image to grayscale.")
        image = color.rgb2gray(image)
    
    print("Image shape after conversion:", image.shape)

    # Otsuの閾値を使用して二値化
    thresh = filters.threshold_otsu(image)
    binary = image > thresh
    
    print("Binary image shape:", binary.shape)

    # 小さなオブジェクトを除去
    binary_cleaned = morphology.remove_small_objects(binary, min_size=20)

    # 距離変換とウォーターシェッドアルゴリズムを使用して粒子を分離
    distance = ndi.distance_transform_edt(binary_cleaned)
    local_maxi = peak_local_max(distance, footprint=np.ones((3, 3)), labels=binary_cleaned)
    markers = measure.label(local_maxi)
    labels_ws = segmentation.watershed(-distance, markers, mask=binary_cleaned)
    
    # 粒子のカウント
    particle_count = np.max(measure.label(labels_ws))
    
    # 結果の表示
    fig, ax = plt.subplots(1, 3, figsize=(12, 4))
    ax[0].imshow(image, cmap='gray')
    ax[0].set_title('Original Image')
    ax[0].axis('off')
    ax[1].imshow(binary_cleaned, cmap='gray')
    ax[1].set_title('Binary Image')
    ax[1].axis('off')
    ax[2].imshow(labels_ws, cmap='nipy_spectral')
    ax[2].set_title('Labeled Image')
    ax[2].axis('off')
    
    plt.tight_layout()
    plt.show()
    
    return particle_count

# パスを設定
image_path = 'data/particle_image.png'

# 粒子をカウント
particle_count = count_particles(image_path)
print(f'Number of particles: {particle_count}')
