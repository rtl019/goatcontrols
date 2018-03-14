from depthdata import depthinfo
import numpy as np
csv = np.genfromtxt ('frame.csv', delimiter=",")
x = depthinfo.depth(0,0,0)
x.printpixel()
col = []

for i in range(0,480,1):
    for j in range(0,640,1):
        col.append(depthinfo.depth(csv[i,j],i,j))


res=np.append([],col)


