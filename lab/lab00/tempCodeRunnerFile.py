import numpy as np

a = [[1,2,3],[2,2,2],[1,1,1]]
b = np.sum(a,axis = 1)
c = np.sum(a,axis = 1,keepdims = True)
print(b)
print(c)