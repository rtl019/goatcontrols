from depthdata import depthinfo
import numpy as np
import math
import timeit
import cv2
csv = np.genfromtxt ('frame.csv', delimiter=",")

def func1(csv):
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

def func(csv):
    #print(type(csv))
    #print(csv.shape)
    a = np.mean(csv)
    distance = 0.1236*math.tan(a/2842.5+1.1863)
    return distance

def frame_grid(csv):
    """This function returns a  3x4 array of distance from the camera. It is basically the average of depth distance of 480x640 grid."""
    a1=(csv[0:160,0:160])
    a2=(csv[0:160,160:320])
    a3=(csv[0:160,320:480])
    a4=(csv[0:160,480:640])

    b1=(csv[160:320,0:160])
    b2=(csv[160:320,160:320])
    b3=(csv[160:320,320:480])
    b4=(csv[160:320,480:640])
    
    c1=(csv[320:480,0:160])
    c2=(csv[320:480,160:320])
    c3=(csv[320:480,320:480])
    c4=(csv[320:480,480:640])

    a_1=func(a1)
    a_2=func(a2)
    a_3=func(a3)
    a_4=func(a4)

    b_1=func(b1)
    b_2=func(b2)
    b_3=func(b3)
    b_4=func(b4)

    c_1=func(c1)
    c_2=func(c2)
    c_3=func(c3)
    c_4=func(c4)
    a = np.array([[a_1,a_2,a_3,a_4],[b_1,b_2,b_3,b_4],[c_1,c_2,c_3,c_4]])
    return a





a2=(csv[320:330,160:170])

answer=(frame_grid(csv))
print(answer)
print(type(answer))
print(answer.shape)
print(a2)
while 1:
    array = csv.astype(np.uint8)
    #cv2.rectangle(array,(0,0),(120,480),(0,0,0),1)
    cv2.rectangle(array,(0,0),(0,160),(0,0,0),1)
    cv2.imshow('Depth image',array)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        print("ESC Key pressed quiting")
        break
cv2.destroyAllWindows()
    




