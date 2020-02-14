# -*- coding: utf-8 -*-

import cv2

img_file = 'insightbook.opencv_project_python-master/img/girl.jpg'
save_file = 'insightbook.opencv_project_python-master/img/girl_gray.jpg'

img = cv2.imread(img_file)
#cv2.imshow(img_file, img)
#cv2.imwrite(save_file, img) #파일로 저장, 포맷은 확장에 따름
#cv2.waitKey()

tmpImg = img[:,199,0] #numpy array여서 연산처리 간편
# tmpImg.where : 특정값의 인덱스를 추출하는 함수(numpy array의 기능임)
#print(sum(tmpImg)) #23600
cv2.imshow('test', tmpImg)
cv2.waitKey()
cv2.destroyAllWindows()
