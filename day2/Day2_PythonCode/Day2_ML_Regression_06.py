# Regression #5 - cirrhosis death rate
from sklearn import linear_model
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm

dfData = pd.read_csv('population_drinking.csv')
dfData.column = ['Urban population (percentage)', 
                 'Late births (reciprocal * 100)',
                 'Wine consumption per capita',
                 'Liquor consumption per capita',
                 'Cirrhosis death rate']

rawData = dfData.values    # Pandas dataframe을 array로 변환
population = rawData[:,1].reshape(-1,1)
lateBirth = rawData[:,2].reshape(-1,1)
wine = rawData[:,3].reshape(-1,1)
liquor = rawData[:,4].reshape(-1,1)
deathRate = rawData[:,5].reshape(-1,1)

x = np.concatenate([population, lateBirth, wine, liquor], axis=1)
#x = np.concatenate([lateBirth, wine], axis=1)

fitFunc = linear_model.LinearRegression()
fitFunc.fit(x, deathRate)

print(fitFunc.intercept_)
print(fitFunc.coef_)

theta0 = fitFunc.intercept_
theta1 = fitFunc.coef_[0][0]
theta2 = fitFunc.coef_[0][1]

xp = np.linspace(min(lateBirth), max(lateBirth), 30).reshape(-1,1)
yp = np.linspace(min(wine), max(wine), 30).reshape(-1,1)

xMesh, yMesh = np.meshgrid(xp, yp)
zMesh = theta0 + theta1 * xMesh + theta2 * yMesh

fig = plt.figure(1, figsize = (10, 10))
plt.cla()
ax = plt.axes(projection='3d')
ax.plot_surface(xMesh, yMesh, zMesh, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False, alpha=0.5)
ax.scatter(lateBirth, wine, deathRate, marker='o')
 
 
ax.set_xlabel('Late Birth')
ax.set_ylabel('Wine')
ax.set_zlabel('Cirrhosis Death Rate')
plt.show()



