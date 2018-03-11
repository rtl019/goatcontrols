class depth(object):
	""" for ClassName"""
	minDistance = -10
	scaleFactor = .0021
	w = 640
	h = 480

	def __init__(self, rawdepth,pixel):
		super(depth, self).__init__()
		self.rawdepth = rawdepth+1
		self.pixel = pixel


	def printpixel(self):
		print(self.pixel)


	def printdepth(self):
		print(self.rawdepth)
	
	def xdistance(self):
		x = (self.pixel - self.w/2)*(self.rawdepth +self.minDistance)*self.scaleFactor
		print(x)
		return(x)

	def ydistance(self):
		y = (self.pixel - self.h/2)*(self.rawdepth +self.minDistance)*self.scaleFactor
		print(y)
		return y

	def zdistance(self):
		z = self.rawdepth
		print(z)
		return (z)
