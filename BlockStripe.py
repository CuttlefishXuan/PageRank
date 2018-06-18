'''
    Block-Stripe Update Algorithm
'''

import numpy as np
import time


def initR(n, alpha):
    r = np.zeros((n), dtype = float)
    for i in range(n):
        r[i] = (float(1)-alpha)/7115
    return r


def loadROld(n, fileName='rOld.txt'):
    r = np.zeros((n), dtype=float)
    with open(fileName) as f:
        i = 0
        for line in f:
            r[i] = float(line.strip('\n'))
            i += 1
    return r


def writeIntoFile(r_new, k, n, fileName='rOld.txt'):
    r_old_tmp = np.zeros(n, dtype=float)
    count = 0
    with open(fileName, 'r') as f:
        for line in f:
            line = line.strip('\n').strip('{}')
            score = float(line)
            r_old_tmp[count] = score
            count += 1
    start = 1000* k
    if(k==7):
        end = 7115
    else:
        end = 1000 * (k+1)
    r_old_tmp[start:end] = r_new
    with open(fileName, 'w') as f:
        for item in r_old_tmp:
            f.write(str(item) + '\n')


def loadDegree(n, fileName='M.txt'):
    degree_array = np.zeros(n, dtype=int)
    with open(fileName) as f:
        for line in f:
            source, indeg, degree, destination = [x for x in line.split(';')]
            source = int(source)
            degree = int(degree)
            degree_array[source] = degree
    return degree_array


def loadMatrix(n, k, fileName='M_stripe.txt'):
    destination_list = [[] for row in range(n)]
    with open(fileName) as f:
        for line in f:
            group, source, degree, destination = [x for x in line.split(';')]
            group = int(group)
            if(group == k):
                source = int(source)
                destination = destination.strip('\n').strip('[]')
                if(len(destination)==0):
                    continue
                destination_str_list = destination.split(',')
                destination_list[source] = [int(x) for x in destination_str_list]
    return destination_list


def pageRank(N, K=8, alpha=0.85, max_inter=100, tol=1.0e-10):
    degree_array = loadDegree(N)

    for iter in range(max_inter):
        print("\n第", iter+1, "次迭代")
        r_old = loadROld(N)
        print("r_old[0]", r_old[0], "r_old[1]", r_old[1])
        convergence = np.array([False, False, False, False, False, False, False, False])
        err = 0
        for k in range(K):
            start = k * 1000
            end = (k + 1) * 1000
            r_new = np.zeros(1)
            if(k==7):
                r_new = initR(115, alpha)
            else:
                r_new = initR(1000, alpha)
            
            destination_list = loadMatrix(N, k)# 读取k对应的7115条M记录,得到destination_list[i]


            for i in range(N):
                for j in range(len(destination_list[i])):
                    r_new[ destination_list[i][j] - k*1000 ] += alpha * r_old[i] / degree_array[i]
            # 把更新的r_new存进文件
            if(k==7):
                err += np.fabs(r_new - r_old[7000:len(r_old)]).sum()
                if((r_old[7000:len(r_old)] == r_new).all()):
                    convergence[k] = True
            else:
                err += np.fabs(r_new - r_old[start:end]).sum()
                if((r_old[start:end] == r_new).all()):
                    convergence[k] = True
            writeIntoFile(r_new, k, N)
        # 怎么判断收敛？
        print("err", err)
        if(err < tol):
            print("err < N*tol, Convergence")
            break
        if(np.sum(convergence==True) == 8):
            print("Concergence is true")
            break


if __name__=="__main__":
    N = 7115
    pageRank(N)