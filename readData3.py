# 输出M_stripe.txt
# k, 节点编号，出度，desination
# K取9    0~999, 1000~1999, ... , 8000～8298

import numpy as np


N = 7115
K = 8
nodelist = np.load('nodelist.npy')[()]
degree = np.zeros(N, dtype=int)


with open('WikiData.txt') as f:
    for line in f:
        head, tail = [int(x) for x in line.split()]
        head_index = np.where(nodelist==head)[0][0]
        tail_index = np.where(nodelist==tail)[0][0]
        degree[head_index] += 1


for k  in range(K):
    destination = [[] for row in range(N)]
    with open('WikiData.txt') as f:
        for line in f:
            head, tail = [int(x) for x in line.split()]
            head_index = np.where(nodelist==head)[0][0]
            tail_index = np.where(nodelist==tail)[0][0]
            if(tail_index > (1000*(k+1)-1)):
                continue
            if(tail_index >= 1000*k and tail_index < (1000*(k+1))):
                destination[head_index].append(tail_index)
    
    for i in range(N):
        if(degree[i]==0 or degree[i]==7115):
            degree[i] = 7115
            if(k==7):
                destination[i] = [int(x) for x in range(7000, 7115)]
            else:
                destination[i] = [int(x) for x in range(1000*k, 1000*(k+1))]
        print("{};{};{};{}".format(k, i, degree[i], destination[i]))