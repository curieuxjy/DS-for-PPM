# -*- coding: utf-8 -*-

import cv2
img_file = "insightbook.opencv_project_python-master/img/girl.jpg"
img = cv2.imread(img_file)

if img is not None:
  cv2.imshow('IMG', img) #gbr
  cv2.waitKey()
  cv2.destroyAiiWindows()
else:
  print("No image file.")
  
# 이미지 잘라보기
tmp_img = img[0:100, 0:100, :]
cv2.imshow('imgCropped', tmp_img)
# color
import cv2

img_file = "insightbook.opencv_project_python-master/img/girl.jpg" 
img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)  #그레이 스케일로 읽기

if img is not None:
    cv2.imshow('IMG', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print('No image file.')
    
#------------------------------------
import cv2

img_file = 'insightbook.opencv_project_python-master/img/girl.jpg'
save_file = 'insightbook.opencv_project_python-master/img/girl_gray.jpg'

img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
cv2.imshow(img_file, img)
cv2.imwrite(save_file, img) #파일로 저장, 포맷은 확장에 따름
cv2.waitKey()
cv2.destroyAllWindows()