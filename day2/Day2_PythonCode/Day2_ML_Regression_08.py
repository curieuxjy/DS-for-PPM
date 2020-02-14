# Ridge Regression
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
#    yHat = thetaHat[0] + thetaHat[1] * x
    
    # 9th order polynomial
    yHat = thetaHat[0] + thetaHat[1] * x + thetaHat[2] * x**2 \
         + thetaHat[3] * x**3 + thetaHat[4] * x**4 + thetaHat[5] * x**5 \
         + thetaHat[6] * x**6 + thetaHat[7] * x**7  + thetaHat[8] * x**8 \
         + thetaHat[9] * x**9
         
    return yHat

#-------------------------------------------------------------------
def getError(y, yNoisy):
    tmpError = (y - yNoisy)**2
    rtnError = tmpError.sum()
    
    return rtnError
    
#-------------------------------------------------------------------

nData = 10
xSampled = np.linspace(0, 10, nData).reshape(-1,1)
yIdeal = getIdealY(xSampled, [2,3])

yNoisy = np.array([[  1.86351679],
       [  8.76001878],
       [  7.17715702],
       [ 10.34712292],
       [ 15.13642828],
       [ 17.33971009],
       [ 24.25327184],
       [ 23.17347032],
       [ 26.37172936],
       [ 31.12435991]])
    
#mu = 0
#sigma = 2
#yNoisy = getNoisyY(xSampled, [2,3], mu, sigma)

Phi = np.concatenate([np.ones([nData,1]), 
                      xSampled, xSampled**2, xSampled**3,
                      xSampled**4, xSampled**5, xSampled**6,
                      xSampled**7, xSampled**8, xSampled**9], axis=1)
    
Phi = np.asmatrix(Phi)

lamda_ = 1
theta = (Phi.T*Phi + lamda_*np.identity(10)).I  * Phi.T  * yNoisy

print(theta)

xEval = np.linspace(min(xSampled), max(xSampled), 200)
yHat = getEstimatedY(xEval, theta ).reshape(-1,1)

fig1 = plt.figure(1, figsize = (10, 5))
#plt.cla()
plt.plot(xSampled, yNoisy, 
         color='b', linestyle='', 
         marker = 'x', markersize = 10, label='Measured y')
plt.plot(xEval, yHat, 
         color='k', linestyle='-', label='Estimated y')
#plt.plot(xSampled, yIdeal, 
#         color='k', linestyle='-', label='Ideal y')

#plt.legend(loc=0)
plt.grid(True, color='0.7', linestyle=':', linewidth=1)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Ridge Regression w/ Least Square Method')
plt.show()
