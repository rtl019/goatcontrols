import numpy as np
class depth(object):
	""" for ClassName"""
	minDistance = -10
	scaleFactor = .0021
	w = 640
	h = 480

	def __init__(self, rawdepth,row,col):
		super(depth, self).__init__()
		self.rawdepth = rawdepth
		self.row = row
		self.col = col



	def printpixel(self):
		print(self.row,self.col)


	def printdepth(self):
		print(self.rawdepth)
	
	def xdistance(self):
		x = (self.col - self.w/2)*(self.rawdepth +self.minDistance)*self.scaleFactor
		print(x)
		return(x)

	def ydistance(self):
		y = (self.row - self.h/2)*(self.rawdepth +self.minDistance)*self.scaleFactor
		print(y)
		return y

	def zdistance(self):
		z = self.rawdepth
		print(z)
		return (z)


"""an utility function to save a numpy array as a csv the default name is foo.csv """
def savearrayascsv(arr):
        try:
                np.savetxt("foo.csv", a, delimiter=",")
        except:
                print("Some Exception going on") 
