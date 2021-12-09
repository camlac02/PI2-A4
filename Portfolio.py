from scipy import optimize
import numpy as np

class Portfolio():
  def __init__(self, ret):
    self.ret = ret
   
  def ret_pf(self, prop):
    ret_geo = []
    for i in range(0, len(self.ret)):
      ret_geo.append(np.prod([x+1 for x in self.ret[i]])**(1/len(self.ret[i])) - 1)
    return(sum([a*b for a,b in zip(prop, ret_geo)]))
  
  def vol_pf(self, prop):
    std = []
    for i in self.ret:
      mean = sum(i)/len(i)
      std.append(np.sqrt(sum([(x-mean)**2 for x in i])/len(i)))
    mean_prop = [a*b for a,b in zip(prop, std)]
    cor = np.corrcoef(self.ret)
    val = []
    for j in range(0, len(mean_prop)):
        val.append(sum([mean_prop[j]*mean_prop[x] ** cor[j,x] for x in range(0,len(mean_prop))]))
    return(np.sqrt(sum(val)))
  
