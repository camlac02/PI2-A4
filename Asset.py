import numpy as np
from scipy import optimize

class Asset():
	def __init__(self,price):
		self.pt = price
	
	def annual_return(self):
		ret = []
		for i in range(0, len(self.pt) - 1):
			ret.append((self.pt[i+1] - self.pt[i])/self.pt[i])
		return(ret)
	def ret_geo(self, ret):
		return(np.prod([x+1 for x in ret])**(1/len(retours))-1)
	
	def std_dev(self, ret):
		mean = sum(ret)/len(ret)
		return(np.sqrt(sum([(x - mean)**2 for x in ret])/len(ret))]
	
