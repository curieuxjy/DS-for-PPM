# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread('insightbook.opencv_project_python-master/img/gray_gradient.jpg', cv2.IMREAD_GRAYSCALE) #이미지를 그레이 스케일로 읽기

#NumPy API로 바이너리 이미지 만들기 Method1
thresh_np = np.zeros_like(img)   # 원본과 동일한 크기의 0으로 채워진 이미지
thresh_np[ img > 127] = 255      # 127 보다 큰 값만 255로 변경 #나머지는 0
# `img>127` -> index 반환

#OpenCV API로 바이너리 이미지 만들기 Method2
ret, thresh_cv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) 
print(ret)  # 127.0, 바이너리 이미지에 사용된 문턱 값 반환

#원본과 결과물을 matplotlib으로 출력
imgs = {'Original': img, 'NumPy API':thresh_np, 'cv2.threshold': thresh_cv}
# 딕셔너리로 저장(불러오기 쉬움)

# matplotlib 사용(steel image)
for i , (key, value) in enumerate(imgs.items()):
    plt.subplot(1, 3, i+1)
    plt.title(key)
    plt.imshow(value, cmap='gray')
    plt.xticks([]); plt.yticks([])

plt.show()



