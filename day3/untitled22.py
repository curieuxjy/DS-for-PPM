# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

nData = 50
x1 = 8*np.random.rand(nData, 1)
x2 = 7*np.random.rand(nData, 1) - 3

g = 1.5 * x1 + x2 - 2

C1 = np.where(g >= 1)
C0 = np.where(g < -1)
print(C1)

C1 = np.where(g >= 1)[0]
C0 = np.where(g < -1)[0]
print(C1.shape)
print(C0.shape)

plt.figure(1, figsize=(10, 8))
plt.plot(x1[C1], x2[C1], 'ro', alpha = 0.4, label = 'C1')
plt.plot(x1[C0], x2[C0], 'bo', alpha = 0.4, label = 'C0')
plt.title('Perceptron Algorithm', fontsize = 15)
plt.legend(loc = 1, fontsize = 15)
plt.xlabel(r'$x_1$', fontsize = 15)
plt.ylabel(r'$x_2$', fontsize = 15)
plt.show()


X1 = np.hstack([x1[C1], x2[C1]])
X0 = np.hstack([x1[C0], x2[C0]])
X = np.vstack([X1, X0])

y = np.vstack([np.ones([C1.shape[0],1]), -np.ones([C0.shape[0],1])])

clf = linear_model.Perceptron(tol=1e-3)
clf.fit(X, np.ravel(y))

testPoint = [4, 0]
isOne = clf.predict([[4,0]])[0]

print(isOne)
#
#if isOne > 0:
#    plt.figure(1, figsize=(10, 8))
#    plt.plot(testPoint[0], testPoint[1], 'ro', markersize=10)
#else:
#    plt.figure(1, figsize=(10, 8))
#    plt.plot(testPoint[0], testPoint[1], 'bo', markersize=10)
    
    
    
w0 = clf.intercept_[0]
w1 = clf.coef_[0,0]
w2 = clf.coef_[0,1]

x1p = np.linspace(0,8,100).reshape(-1,1)
x2p = - w1/w2*x1p - w0/w2

plt.figure(1, figsize=(10, 8))
plt.plot(x1[C1], x2[C1], 'ro', alpha = 0.4, label = 'C1')
plt.plot(x1[C0], x2[C0], 'bo', alpha = 0.4, label = 'C0')
plt.plot(x1p, x2p, c = 'k', linewidth = 4, label = 'perceptron')
plt.xlim([0, 8])
plt.ylim([-7, 5])
plt.xlabel('$x_1$', fontsize = 15)
plt.ylabel('$x_2$', fontsize = 15)
plt.legend(loc = 1, fontsize = 15)
plt.show()


    