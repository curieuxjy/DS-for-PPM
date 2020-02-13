# numpy exercise

import numpy as np

a1 = np.empty((0,3), float)

print(a1)

a1 = np.append(a1, np.array([[10,20,30]]), axis=0)
a1 = np.append(a1, np.array([[40,50,60]]), axis=0)
print(a1)

print(a1[1,2])




