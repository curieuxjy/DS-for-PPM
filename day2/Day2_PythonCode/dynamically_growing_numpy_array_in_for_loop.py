import numpy as np
import matplotlib.pyplot as plt

#nData = 10
#xSampled = np.linspace(0, 10, nData).reshape(-1,1)
#yArray = np.array([[  2.28093446], [ 10.69146323], [  1.74930661],
#                   [ 11.48563487], [ 20.30311448], [ 22.80010189],
#                   [ 16.75367794], [ 17.6522528 ], [ 36.0261762 ],
#                   [ 32.04787191]])
#
#accArray = np.empty([len(yArray), 0])
#accArray = np.concatenate([accArray, yArray], axis=1)


a = np.empty([0])

for k in range(1,5):
    a = np.append(a, k)
    
    print(a)
    
    

