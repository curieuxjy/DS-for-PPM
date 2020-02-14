# Regression #2

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

#nData = 10
#xSampled = np.linspace(0, 10, nData).reshape(-1,1)
#yIdeal = getIdealY(xSampled, [2,3])
#yNoisy = np.array([[  2.28093446], [ 10.69146323], [  1.74930661],
#                   [ 11.48563487], [ 20.30311448], [ 22.80010189],
#                   [ 16.75367794], [ 17.6522528 ], [ 36.0261762 ],
#                   [ 32.04787191]])
nData = 50
xSampled = np.linspace(0, 10, nData).reshape(-1,1)
yIdeal = getIdealY(xSampled, [2,3])

mu = 0
sigma = 2
yNoisy = getNoisyY(xSampled, [2,3], mu, sigma)


#a = 3
#b = 2
#thetaHat = np.array([b, a]) 
#yHat = getEstimatedY(xSampled, thetaHat)
#errL2 = getError(yNoisy, yHat)
#    
#fig1 = plt.figure(1, figsize = (10, 5))
#plt.plot(xSampled, yNoisy, 
#         color='r', linestyle='', 
#         marker = 'x', markersize = 10, label='Measured y')
#plt.plot(xSampled, yHat, 
#         color='b', linestyle='-', label='Estimated y')
##plt.legend(loc=0)
#plt.grid(True, color='0.7', linestyle=':', linewidth=1)
#plt.xlabel('X')
#plt.ylabel('Y')
#plt.title('Linear Regression')
#plt.show()

#result_array = np.empty(data_array.size) # the default dtype is float, so set dtype if it isn't float
#
#for idx, line in enumerate(data_array):
#result_array[idx] = do_stuff(line)



as_ = np.array([1, 2, 3, 4, 5])
bs_ = np.array([2])

thetaHat = []
yHats = np.empty([len(xSampled), 0])
estErr = np.empty([0])

#accArray = np.empty([len(yArray), 0])
#accArray = np.concatenate([accArray, yArray], axis=1)

for i in range(0, len(as_)):
    
    print(as_[i])
    thetaHat = np.array([bs_[0], as_[i]]) 
    
    yHat = getEstimatedY(xSampled, thetaHat)
#    yHats = np.concatenate([yHats, yHat], axis=1)
    yHats = np.append(yHats, yHat, axis=1)
    
    tmpErr = getError(yNoisy, yHat)
#    estErr = np.concatenate([estErr, tmpErr], axis=0)     
    estErr = np.append(estErr, tmpErr)


# Two separate figures
#fig1 = plt.figure(1, figsize = (10, 5))
#for i in range(0, len(as_)):
#    plt.plot(xSampled, yHats[:,i], 
#             color='r', linestyle='-', label='Estimated y_%s' % str(i))
#
#plt.plot(xSampled, yNoisy, 
#         color='b', linestyle='', marker='x', markersize=8,
#         label='Measured y')
#plt.plot(xSampled, yIdeal, 
#         color='k', linestyle='-',
#         label='Ideal y')
#
#plt.legend(loc=0)
#plt.grid(True, color='0.7', linestyle=':', linewidth=1)
#plt.xlabel('X')
#plt.ylabel('Y')
#plt.title('Linear Regression')
#plt.show()
#
#
#fig2 = plt.figure(2, figsize = (10, 5))
#plt.plot(as_, estErr, 
#         color='b', linestyle='-', marker='x', markersize = 8)
#         
#plt.legend(loc=0)
#plt.grid(True, color='0.7', linestyle=':', linewidth=1)
#plt.xlabel('a (slope)')
#plt.ylabel('error')
#plt.title('Error')
#plt.show()


# Two subplots in one figure
fig1 = plt.figure(1, figsize = (10, 5))
ax1 = fig1.add_subplot(1,2,1)
for i in range(0, len(as_)):
    ax1.plot(xSampled, yHats[:,i], 
             color='r', linestyle='-', label='Estimated y_%s' % str(i))
    
ax1.plot(xSampled, yNoisy, 
         color='b', linestyle='', marker='x', markersize=8,
         label='Measured y')
ax1.plot(xSampled, yIdeal, 
         color='k', linestyle='-',
         label='Ideal y')

ax1.legend(loc=0)
ax1.grid(True, color='0.7', linestyle=':', linewidth=1)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_title('Linear Regression')

ax2 = fig1.add_subplot(1,2,2)
ax2.plot(as_, estErr, 
         color='b', linestyle='-', marker='x', markersize = 8)
         
ax2.legend(loc=0)
ax2.grid(True, color='0.7', linestyle=':', linewidth=1)
ax2.set_xlabel('a (slope)')
ax2.set_ylabel('error')
ax2.set_title('Error')

plt.show()



