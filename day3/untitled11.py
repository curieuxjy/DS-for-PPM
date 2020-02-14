# -*- coding: utf-8 -*-


import cv2
import numpy as np

img = cv2.imread('insightbook.opencv_project_python-master/img/girl.jpg')

img2 = img.astype(np.uint16)                # dtype 변경 integer로
b,g,r = cv2.split(img2)                     # 채널 별로 분리 
#b,g,r = img2[:,:,0], img2[:,:,1], img2[:,:,2]
gray1 = ((b + g + r)/3).astype(np.uint8)    # 평균 값 연산후 dtype 변경 
# 수동으로 gray값으로 변형

gray2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # BGR을 그레이 스케일로 변경 
# opencv module이용
cv2.imshow('original', img)
cv2.imshow('gray1', gray1)
cv2.imshow('gray2', gray2)

cv2.waitKey(0)
cv2.destroyAllWindows()

# 수동과 모듈의 차이를 출력해보기 됨
# (차이를 구하는 순서에 따라 결과가 음수면 의도한 대로 안나올 수 있음)
# 모션 캡쳐는 앞, 뒤 프레임의 차이를 인지하면 됨
differ = gray2-gray1
cv2.imshow('difference', differ)
sum_differ = sum(sum(differ))
print(sum_differ)
cv2.waitKey(0)
cv2.destroyAllWindows()