# M.txt
# 节点编号，入度，出度，desination
# M大小有7115行，都映射成0~7114来表示
# dead end 数量 1005

import numpy as np

N = 7115
nodelist = np.load('nodelist.npy')[()]
destination = [[] for row in range(N)]
in_degree = np.zeros(N, dtype=int)
out_degree = np.zeros(N, dtype=int)


with open('WikiData.txt') as f:
    for line in f:
        head, tail = [int(x) for x in line.split()]
        head_index = np.where(nodelist==head)[0][0]
        tail_index = np.where(nodelist==tail)[0][0]
        destination[head_index].append(tail_index)
        out_degree[head_index] += 1
        in_degree[tail_index] += 1


for i in range(N):
    if(in_degree[i]==0 and out_degree[i]==0):
        print("\nError!", i, "in_degree[i]==0 and out_degree[i]==0")
    if(out_degree[i]==0):
        destination[i] = [int(x) for x in range(N)]
        out_degree[i] = 7115
    
    print("{};{};{};{}".format(i, in_degree[i], out_degree[i], destination[i]))