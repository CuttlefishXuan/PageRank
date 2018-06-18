# 输出 rOld.txt
import numpy as np

def initR(n, alpha):
    r = np.zeros((n), dtype=float)
    for i in range(n):
        r[i] = (float(1)-alpha)/n
    return r

if __name__=="__main__":
    N = 7115
    alpha = 0.85
    r_old = initR(N, alpha)
    for i in r_old:
        print(i)