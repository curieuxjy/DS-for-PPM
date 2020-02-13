# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 13:45:57 2020

@author: LG
"""

import numpy as np
import matplotlib.pyplot as plt

def getIdealY(x, theta):
  # x는 colunm vector
  y = theta[0] + theta[1] * x
  return y

def getNoisyY(x, theta, mu, sigma):
  sigNoise= np.random.normal(mu, sigma, x.size).reshape(-1, 1)
  y = theta[0] + theta[1] * xSampled + sigNoise
  return y
#-------------------------------------------------------------------
nData = 10
theta = np.array([2, 3])
xSampled = np.linspace(0, 10, nData).reshape(-1,1)#어쨌든 colunm은 1개로 맞춰라
yIdeal = getIdealY(xSampled, theta)

mu = 0
sigma =8
yNoisy = getNoisyY(xSampled, theta, mu, sigma)


fig1 = plt.figure(1, figsize = (10,5))
plt.cla() #axis 초기화
plt.clf() # figure 초기화
plt.plot(xSampled, yIdeal, 
         color='b', linestyle='-', label='Ideal y')
plt.plot(xSampled, yNoisy, 
         color='r', linestyle='', 
         marker = 'x', markersize = 10, label='Noisy y (Measurement)')
plt.legend(loc=0)
plt.grid(True, color='0.7', linestyle=':', linewidth=1)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression')
plt.show()
