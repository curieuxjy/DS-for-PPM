# -*- coding: utf-8 -*-

import cv2
import numpy as np

# 연산에 사용할 배열 생성
a = np.uint8([[200, 50]]) 
b = np.uint8([[100, 100]])

#NumPy 배열 직접 연산
add1 = a + b
sub1 = a - b
mult1 = a * 2
div1 = a / 3

# OpenCV API를 이용한 연산
add2 = cv2.add(a, b)
sub2 = cv2.subtract(a, b)
mult2 = cv2.multiply(a , 2)
div2 = cv2.divide(a, 3)

# 각 연산 결과 출력
# 이미지는 0-255사이의 값만 출력할 수 있어서 결과가 다르게 나옴
# 이미지 연산은 opencv module을 이용할 것
print(add1, add2)
print(sub1, sub2)
print(mult1, mult2)
print(div1, div2)
