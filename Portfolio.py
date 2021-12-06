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
    cor = np.corrcoef(self, ret)
    value = []
    for j in range(0, len(mean_prop)):
      value.append(sum[mean_prop[j]*mean_prop[x] ** cor[j,x] for x in range(0,len(mean_prop))]))
    return(np.sqrt(sum(val)))
  
  def optimize_pf(self, ret_d):
    bounds = ((0.0, 1.0),) * len(self.ret)
    init = list(np;random.dirichlet(np.ones(len(self.ret)), size = 1)[0]
    prop_opti = optimize.minimize(self.vol_pf, init, method = 'SLSQP', constraints = ({'type': 'eq', 'fun': lambda inputs: 1.0 - np.sum(inputs)},
                                                                                      {'type': 'eq','fun' : lambda inputs : ret_d - self.ret_pf(prop=inputs)}),
                                  bounds = bounds)
    return prop_opti.x
