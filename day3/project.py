# -*- coding: utf-8 -*-
# Team Project

from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
import cv2
import numpy as np

#------------------edge-detection------------------
names = ['paper1.jpg','paper2.jpg','rock1.jpg','rock2.jpg']
path = "data/" 
list_num = []

for name in names:
    file_path = path + name
    # grayScale
    img = cv2.imread(file_path,cv2.IMREAD_GRAYSCALE)
    list_num.append(img)

# Laplacian Edge 
edge_list = [cv2.Laplacian(list_num[i],-1) for i in range(len(list_num))]

# Horizontal Stacking & Labeling(0->paper, 1->rock)
paper1 = np.hstack((list_num[0],edge_list[0]))
cv2.imshow('Paper1',paper1)
# Flatten
paper1_data = np.ravel(edge_list[0],order = 'C')
#print(Bo_data.shape)
paper1_label = '0'

paper2 = np.hstack((list_num[1],edge_list[1]))
cv2.imshow('Paper2',paper2)
paper2_data = np.ravel(edge_list[1],order = 'C')
paper2_label = '0'

rock1 = np.hstack((list_num[2],edge_list[2]))
cv2.imshow('Rock1',rock1)
rock1_data = np.ravel(edge_list[2],order = 'C')
rock1_label = '1'

rock2 = np.hstack((list_num[3],edge_list[3]))
cv2.imshow('Rock2',rock2)
rock2_data = np.ravel(edge_list[3],order = 'C')
rock2_label = '1'

#------------------------Train DataSet------------------------
X_data= np.array([paper1_data,paper2_data,rock1_data,rock2_data])
Y_label = np.vstack([paper1_label,paper2_label,rock1_label,rock2_label]).reshape(-1,1)
print(X_data.shape) # (n_samples, n_features) e.g.(사진 수, 픽셀 수) (4, 307200)
print(Y_label.shape) # (n_samples,) e.g.(라벨 수,) (4, 1)

#--------------------------model-main-------------------------
kernel = 1.0 * RBF(1.0)
gpc = GaussianProcessClassifier(kernel=kernel,random_state=0)
# training
gpc.fit(X_data, Y_label)

# new data (=test data, unseen data)
img_new = cv2.imread('data/test.jpg',cv2.IMREAD_GRAYSCALE)
X_new = np.ravel(img_new,order = 'C').reshape(-1,1).T

print(X_new.shape) #(1, 307200) #(n_samples, n_features)
#------------------------prediction------------------------------
pred = gpc.predict(X_new) 
print(pred) # 원래는 rock이 들어갔기 때문에 '1'을 예측해야 하지만 현재는 '0'으로 잘못 예측

#-------------------Future Work---------------------------
# 1. interface를 이용하여 dataset 만들기(가능하면 sql로 database 구축까지)
# 2. image processing하고 labeling 자동화 함수 만들기
# 3. Gaussian Process이해해서 parameter 조정 or 다른 Classification 사용해보기
# 4. SVD 이용해서 dataset 압축해보기
# 5. Data Ploting
# 6. Test(prediction) interface를 이용하여 실시간 예측값 보여주기
# 7. 맞는 예측값 나올때까지 project developing 하
#-----------------------SVD----------------------------------
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

