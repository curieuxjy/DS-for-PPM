# -*- coding: utf-8 -*-

# Singular Value Decomposition
# np.linalg.svd
# sigma 값은 내림차순으로 나와있음


# Singular-value decomposition
from numpy import array
from scipy.linalg import svd
# define a matrix
A = array([[1, 2], [3, 4], [5, 6]])
print(A)
# SVD
U, s, VT = svd(A)
print(U)
print(s)
print(VT)


# Reconstruct SVD
from numpy import array
from numpy import diag
#from numpy import dot
from numpy import zeros
from scipy.linalg import svd
# define a matrix
A = array([[1, 2], [3, 4], [5, 6]])
print(A)
# Singular-value decomposition
U, s, VT = svd(A)
# create m x n Sigma matrix
Sigma = zeros((A.shape[0], A.shape[1]))
# populate Sigma with n x n diagonal matrix
Sigma[:A.shape[1], :A.shape[1]] = diag(s)
# reconstruct matrix
B = U.dot(Sigma.dot(VT))
print(B)



#
## Reconstruct SVD
#from numpy import array
#from numpy import diag
#from numpy import dot
#from numpy import zeros
#from scipy.linalg import svd
## define a matrix
#A = array([[1, 2], [3, 4], [5, 6]])
#print(A)
## Singular-value decomposition
#U, s, VT = svd(A)
## create m x n Sigma matrix
#Sigma = zeros((A.shape[0], A.shape[1]))
## populate Sigma with n x n diagonal matrix
#Sigma[:A.shape[1], :A.shape[1]] = diag(s)
## reconstruct matrix
#B = U.dot(Sigma.dot(VT))
#print(B)