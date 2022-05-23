import numpy as np
import math
def LeastSquareMethod(u, y, fi, precision = 2):
    a = []
    if(len(u) == len(fi) and len(u) == len(y)):
        Fi = []
        for f in fi:
            row = []
            for x in u:
                row.append(f(x))
            Fi.append(row)
        Fi = np.array(Fi)
        a = np.matmul(np.linalg.inv(np.matmul(Fi,Fi.transpose())),Fi)
        a = a.dot(np.array(y))
    for i in range(len(a)):
        a[i] = round(a[i],precision)
    return a