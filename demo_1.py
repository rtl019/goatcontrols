#import the necessary modules
import freenect
import cv2
import numpy as np
import math

#function to get RGB image from kinect
def get_video():
    array,_ = freenect.sync_get_video()
    array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
    return array

#get raw depth data from kinect
def get_depth():
    array,_ = freenect.sync_get_depth()
    array = array.astype(np.uint16)
    return array

#function to get depth image from kinect
def get_depth_image():
    array,_ = freenect.sync_get_depth()
    array = array.astype(np.uint8)
    return array

def func(csv):
    #print(type(csv))
    #print(csv.shape)
    a = np.mean(csv)
    distance = 0.1236*math.tan(a/2842.5+1.1863)
    return distance



if __name__ == "__main__":
    print("Please press ESC key to quit:")
    while 1:
        #get a frame from RGB camera
        frame = get_video()
        #get a frame from depth sensor
        depth = get_depth()
        depth_image = get_depth_image()
        #display RGB image
        cv2.imshow('RGB image',frame)
        #display depth image
        cv2.imshow('Depth image',depth_image)
        if(func(depth)<1.5):
            print("BOOOM")
        else:
            print("\n")
            pass

        # quit program when 'esc' key is pressed
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            print("ESC Key pressed quiting")
            break
    cv2.destroyAllWindows()
