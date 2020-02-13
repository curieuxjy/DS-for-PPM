# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 15:22:54 2020

@author: LG
"""

from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dfData = pd.read_csv('BrainWeight_vs_BodyWeight.csv')
dfData.column = ['Brain_Weight', 'Body_Weight']

rawData = dfData.values 
#print(rawData)
brainWeight = rawData[:,1].reshape(-1,1)
#print(brainWeight)
bodyWeight = rawData[:,2].reshape(-1,1)

#-----------again--------------------------
fig1 = plt.figure(1, figsize=(10, 8))
plt.cla()
plt.grid(True, alpha = 0.3, color='0.7', linestyle='-', linewidth=1)
plt.plot(brainWeight, bodyWeight, 
         color='b', linestyle='', 
         marker = 'o', markersize = 10, label='Measured brain weight')
plt.xlabel('Brain Weight')
plt.ylabel('Body Weight')
plt.title('Brain Weight vs. Body Weight')
plt.show()

fitFunc = linear_model.LinearRegression()
fitFunc.fit(brainWeight, bodyWeight)

xEval = np.linspace(min(brainWeight), max(brainWeight), 50).reshape(-1,1)
yHat = fitFunc.predict(xEval)

plt.plot(xEval, yHat, 
         color='r', linestyle='-', 
         label='Estimated brain weight')
