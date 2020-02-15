# -*- coding: utf-8 -*-
#Small Project

from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
import cv2
import numpy as np

#------------------------edge-------------------
names = ['bo.jpg','bo2.jpg','rock.jpg','rock2.jpg']
path = "../data/" 
list_num = []
for name in names:
    file_path = path + name
    img = cv2.imread(file_path,cv2.IMREAD_GRAYSCALE)
    list_num.append(img)
    
edge_list = [cv2.Laplacian(list_num[i],-1) for i in range(len(list_num))]

Bo = np.hstack((list_num[0],edge_list[0]))
cv2.imshow('B',Bo)
Bo_data = np.ravel(edge_list[0],order = 'C')
#print(Bo_data.shape)
Bo_label = '0'


Bo2 = np.hstack((list_num[1],edge_list[1]))
cv2.imshow('B',Bo2)
Bo2_data = np.ravel(edge_list[1],order = 'C')
Bo2_label = '0'
#--------------------------------------------------------


Ro = np.hstack((list_num[2],edge_list[2]))
cv2.imshow('R',Ro)
Ro_data = np.ravel(edge_list[2],order = 'C')
Ro_label = '1'


Ro2 = np.hstack((list_num[3],edge_list[3]))
cv2.imshow('R',Ro2)
Ro2_data = np.ravel(edge_list[3],order = 'C')
Ro2_label = '1'

X_data= np.array([Bo_data,Bo2_data,Ro_data,Ro2_data])
Y_label = np.vstack([Bo_label,Bo2_label,Ro_label,Ro2_label]).reshape(-1,1)
  

print(X_data.shape)

#------------------------------model-----main-------------------------
kernel = 1.0 * RBF(1.0)
X = X_data  #(150, 4)
y = Y_label # (150,)
gpc = GaussianProcessClassifier(kernel=kernel,random_state=0)
gpc.fit(X, y)


# new
img_new = cv2.imread('C:/Users/LG\Desktop/Intro for Data Science/data/test.jpg',cv2.IMREAD_GRAYSCALE)
X_new = np.ravel(img_new,order = 'C').reshape(-1,1).T

print(X_new.shape)
#--------------------------------------------------------------------

pred = gpc.predict(X_new) #(n_samples, n_features) #(1,118958 )
print(pred)


#
##-------------------TEST--------------------------------------------
#x_new = # 교수님의 손
#pred = gpc.predict(x_new) #(n_samples, n_features) #(1,118958 )
#print(pred)


#-------------SVD
# import numpy as np
## 행렬 A는 이전 포스트에 있는 예제에서 사용된 것이다.
# def SVDImage(input_image):
#   #input_image -> numpy array, shape
#  
#   # svd함수를 사용하여 3개의 반환값(U,s,V)를 저장한다.
#   U, s, V = np.linalg.svd(input_image, full_matrices = True)
#  
#   # s는 matA의 고유값(eigenvalue) 리스트이다.
#   # svd를 이용하여 근사한(approximated) 결과를 원본과 비교하기 위해
#   # s를 유사대각행렬로 변환한다.
#   S = np.zeros(matA.shape)
#   for i in range(len(s)):
#       S[i][i] = s[i]
#  
#   # 근사한 결과를 계산한다.
#   appA = np.dot(U, np.dot(S, V))
#  
#   # 원래 행렬인 matA와 근사한 행렬인 appA가 서로 비슷하다면
#   # 두 행렬의 차이는 영행렬(zero matrix)에 가까울 것이다.
#   # 즉, 다음의 결과가 대부분 0으로 채워져있다면 성공적인 svd가 이루어진 것이다.
#   print(matA - appA)

