from depthdata import depthinfo
import numpy as np
csv = np.genfromtxt ('frame.csv', delimiter=",")

col = []

for i in range(0,480,1):
    for j in range(0,640,1):
        col.append(depthinfo.depth(csv[i,j],i,j))


res=np.append([],col)
q = res[0:640]
r=res[640:2*640]
np.vstack((q,r))
