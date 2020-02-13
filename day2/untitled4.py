# -*- coding: utf-8 -*-
# 움직이는 예측값에 따른 애러 구하기
import numpy as np
import matplotlib.pyplot as plt

def getIdealY(x, theta):
    y = theta[0] + theta[1] * x
    
    return y

def getEstimatedY(x, theta):
    y = theta[0] + theta[1] * x
    
    return y
#-------------------------------------------------------------------

def getNoisyY(x, theta, mu, sigma):
    sigNoise = np.random.normal(mu, sigma, x.size).reshape(-1,1)    
    y = theta[0] + theta[1] * x + sigNoise

    return y
  
def getError(y, yNoisy):
  tmpError = (y-yNoisy)**2
  rtnError = tmpError.sum()
  
  return rtnError
#-------------------------------------------------------------------

nData = 10
xSampled = np.linspace(0, 10, nData).reshape(-1,1)

yIdeal = getIdealY(xSampled, theta)
yNoisy = getNoisyY(xSampled, theta, mu, sigma)
a = np.array([1, 2, 3, 4, 5])
b = np.array([2])

yHats = np.empty([len(xSampled), 0])
estErr = np.empty([0])

for i in range(5):
  print(a[i])
  
  thetaHat = np.array([b[0], a[i]])

  mu = 0
  sigma = 8
  yNoisy = getNoisyY(xSampled, theta, mu, sigma)
  
  yHat = getEstimatedY(xSampled, thetaHat)
  yHats = np.append(yHats, yHat, axis =1)
  
  tmpErr = getError(yNoisy, yHat)
  est
      
      
fig1 = plt.figure(1, figsize = (10, 5))
ax1 = fig1.add
######-------------------------------------------------------
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


