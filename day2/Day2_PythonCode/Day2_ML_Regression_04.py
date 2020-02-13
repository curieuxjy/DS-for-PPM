# Regression #3 - Scikit-Learn Module

from sklearn import linear_model
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
def getEstimatedY(x, thetaHat):
    yHat = thetaHat[0] + thetaHat[1] * x
    
    return yHat

#-------------------------------------------------------------------
def getError(y, yNoisy):
    tmpError = (y - yNoisy)**2
    rtnError = tmpError.sum()
    
    return rtnError
    
#-------------------------------------------------------------------
    
nData = 10
xSampled = np.linspace(0, 10, nData).reshape(-1,1)

yNoisy = np.array([[  2.28093446], [ 10.69146323], [  1.74930661],
                   [ 11.48563487], [ 20.30311448], [ 22.80010189],
                   [ 16.75367794], [ 17.6522528 ], [ 36.0261762 ],
                   [ 32.04787191]])

#nData = 50
#xSampled = np.linspace(0, 10, nData).reshape(-1,1)
#
#mu = 0
#sigma = 2
#yNoisy = getNoisyY(xSampled, [2,3], mu, sigma)
    
yIdeal = getIdealY(xSampled, [2,3])
    
fitFunc = linear_model.LinearRegression()
fitFunc.fit(xSampled, yNoisy)

print(fitFunc.coef_)
print(fitFunc.intercept_)

xEval = np.linspace(min(xSampled), max(xSampled), 50).reshape(-1,1)
yHat = fitFunc.predict(xEval)

fig1 = plt.figure(1, figsize = (10, 5))
plt.cla()
plt.plot(xSampled, yNoisy, 
         color='b', linestyle='', 
         marker = 'x', markersize = 10, label='Measured y')
plt.plot(xEval, yHat, 
         color='r', linestyle='-', label='Estimated y')
plt.plot(xSampled, yIdeal, 
         color='k', linestyle='-', label='Ideal y')

plt.legend(loc=0)
plt.grid(True, alpha = 0.3, color='0.7', linestyle='-', linewidth=1)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression w/ Scikit-Learn Module')
plt.show()















