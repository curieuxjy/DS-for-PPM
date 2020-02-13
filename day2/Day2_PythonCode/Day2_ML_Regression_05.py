# Regression #4 - brain weight vs body weight
from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dfData = pd.read_csv('BrainWeight_vs_BodyWeight.csv')
dfData.column = ['Brain_Weight', 'Body_Weight']

rawData = dfData.values    # Pandas dataframe을 array로 변환
brainWeight = rawData[:,1].reshape(-1,1)
bodyWeight = rawData[:,2].reshape(-1,1)

fig1 = plt.figure(1, figsize = (10, 8))
plt.cla()
plt.plot(bodyWeight, brainWeight, 
         color='b', linestyle='', 
         marker = 'o', markersize = 10, label='Measured brain weight')
#plt.legend(loc=0)
plt.grid(True, alpha = 0.3, color='0.7', linestyle='-', linewidth=1)
plt.xlabel('Body Weight')
plt.ylabel('Brain Weight')
plt.title('Brain Weight vs. Body Weight')
plt.show()

fitFunc = linear_model.LinearRegression()
fitFunc.fit(bodyWeight, brainWeight)

xEval = np.linspace(min(bodyWeight), max(bodyWeight), 50).reshape(-1,1)
yHat = fitFunc.predict(xEval)

plt.plot(xEval, yHat, 
         color='r', linestyle='-', 
         label='Estimated brain weight')
















## Regression #4 - brain weight vs body weightScikit-Learn Module
#
#from sklearn import linear_model
#import numpy as np
#import matplotlib.pyplot as plt
#import pandas as pd
#
#dfData = pd.read_csv('BrainWeight_vs_BodyWeight.csv')
#dfData.column = ['Brain_Weight', 'Body_Weight']
#
#rawData = dfData.values    # Pandas dataframe을 array로 변환
#brainWeight = rawData[:,1].reshape(-1,1)
#bodyWeight = rawData[:,2].reshape(-1,1)
#
#fig1 = plt.figure(1, figsize = (10, 8))
#plt.cla()
#plt.plot(bodyWeight, brainWeight, 
#         color='b', linestyle='', 
#         marker = 'o', markersize = 10, label='Measured brain weight')
##plt.legend(loc=0)
#plt.grid(True, alpha = 0.3, color='0.7', linestyle='-', linewidth=1)
#plt.xlabel('Body Weight')
#plt.ylabel('Brain Weight')
#plt.title('Brain Weight vs. Body Weight')
#plt.show()
#
#fitFunc = linear_model.LinearRegression()
#fitFunc.fit(bodyWeight, brainWeight)
#
#xEval = np.linspace(min(bodyWeight), max(bodyWeight), 50).reshape(-1,1)
#yHat = fitFunc.predict(xEval)
#
#plt.plot(xEval, yHat, 
#         color='r', linestyle='-', 
#         label='Estimated brain weight')

