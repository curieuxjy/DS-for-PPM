# Regression #1

import numpy as np
import matplotlib.pyplot as plt

def getIdealY(x, theta):
    y = theta[0] + theta[1] * x
    
    return y
#-------------------------------------------------------------------

def getNoisyY(x, theta, mu, sigma):
    sigNoise = np.random.normal(mu, sigma, x.size).reshape(-1,1)    
    y = theta[0] + theta[1] * x + sigNoise

    return y
#-------------------------------------------------------------------

nData = 10
xSampled = np.linspace(0, 10, nData).reshape(-1,1)
        
a = 3
b = 2
theta = np.array([b, a])

#yIdeal = a * xSampled + b
yIdeal = getIdealY(xSampled, theta)

mu = 0
sigma = 8
#yNoisy = getNoisyY(xSampled, theta, mu, sigma)
yNoisy = np.array([[  2.28093446], [ 10.69146323], [  1.74930661],
                   [ 11.48563487], [ 20.30311448], [ 22.80010189],
                   [ 16.75367794], [ 17.6522528 ], [ 36.0261762 ],
                   [ 32.04787191]])
    
    
fig1 = plt.figure(1, figsize = (10, 5))
#plt.plot(xSampled, yIdeal, 
#         color='b', linestyle='-', label='Ideal y')
plt.plot(xSampled, yNoisy, 
         color='r', linestyle='', 
         marker = 'x', markersize = 10, label='Noisy y (Measurement)')
plt.legend(loc=0)
plt.grid(True, color='0.7', linestyle=':', linewidth=1)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression')
plt.show()

