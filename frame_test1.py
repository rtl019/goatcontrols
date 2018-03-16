from depthdata import depthinfo
import numpy as np
import math
import timeit
csv = np.genfromtxt ('frame.csv', delimiter=",")
def func(csv):
    print(type(csv))
    print(csv.shape)
    a = np.mean(csv)
    distance = 0.1236*math.tan(a/2842.5+1.1863)
    print(distance)
    print(csv[0:2].shape)
    print(csv[2:0].shape)
    print(csv[0:40,0:40].shape)
    print("\n\n\n")
    print(np.mean(csv[440:480,40:80]))
    print(np.mean(csv[40:80,40:80]))
    print(np.mean(csv[40:80,600:640]))
    p=(np.mean(csv[40:80,40:80]))
    distance2 = 0.1236*math.tan(p/2842.5+1.1863)
    print(distance2)
    q=(np.mean(csv[2*120:360,240:360]))
    s=1070
    distance3 = 0.1236*math.tan(s/2842.5+1.1863)
    print(distance3)
    print(q)


func(csv) 
