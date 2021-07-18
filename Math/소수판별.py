# logN
import math
res = False

N = 3423
if N == 1:
    res = False
else:
    for i in range(2, int(math.sqrt(N)) + 1): # key point
        if N % i == 0:
            break
    else:
        res = True