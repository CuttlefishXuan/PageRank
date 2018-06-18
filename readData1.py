# nodelist

import numpy as np

nodelist_all = np.zeros(8298, dtype=int)
with open('WikiData.txt') as f:
    for line in f:
        head, tail = [int(x) for x in line.split()]
        nodelist_all[head] = 1
        nodelist_all[tail] = 1

nodelist = np.zeros(7115, dtype=int)
count = 0
for i in range(8298):
    if(nodelist_all[i]==1):
        nodelist[count] = i
        count += 1
print(count)
np.save('nodelist', nodelist)