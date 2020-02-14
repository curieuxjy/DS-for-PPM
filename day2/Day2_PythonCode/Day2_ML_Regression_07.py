# Polynomial Regression
# Source: https://towardsdatascience.com/polynomial-regression-bbe8b9d97491
import operator

import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures

np.random.seed(0)
nData = 50
x = 2 - 3 * np.random.normal(0, 1, nData)
y = 2 + x - 2 * (x ** 2) + 0.5 * (x ** 3) + np.random.normal(-3, 3, nData)
#y = 2 + x - 2 * (x ** 2) + np.random.normal(-3, 3, nData)

# transforming the data to include another axis
x = x[:, np.newaxis]
y = y[:, np.newaxis]

polynomial_features= PolynomialFeatures(degree=3)
x_poly = polynomial_features.fit_transform(x)

model = LinearRegression()
model.fit(x_poly, y)
y_poly_pred = model.predict(x_poly)

plt.cla()
plt.scatter(x, y, s=10)
# sort the values of x before line plot
sort_axis = operator.itemgetter(0)
sorted_zip = sorted(zip(x,y_poly_pred), key=sort_axis)
x, y_poly_pred = zip(*sorted_zip)
plt.plot(x, y_poly_pred, color='m')
plt.grid(True, alpha = 0.3, color='0.7', linestyle='-', linewidth=1)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('3rd Order Polynomial Regression')
plt.show()

#rmse = np.sqrt(mean_squared_error(y,y_poly_pred))
#r2 = r2_score(y,y_poly_pred)
#print(rmse)
#print(r2)




#import numpy as np
#import matplotlib.pyplot as plt
#
#from sklearn.linear_model import LinearRegression
#
#np.random.seed(0)
#x = 2 - 3 * np.random.normal(0, 1, 20)
#y = x - 2 * (x ** 2) + 0.5 * (x ** 3) + np.random.normal(-3, 3, 20)
#
## transforming the data to include another axis
#x = x[:, np.newaxis]
#y = y[:, np.newaxis]
#
#model = LinearRegression()
#model.fit(x, y)
#y_pred = model.predict(x)
#
#plt.scatter(x, y, s=10)
#plt.plot(x, y_pred, color='r')
#plt.show()


