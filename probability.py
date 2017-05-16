import numpy as np
from scipy.stats import weibull_min
import  pickle
import matplotlib.pyplot as plt
s = 0.9*np.random.weibull(15526, 1000)
dist=weibull_min(100,0)
m = dist.rvs(size=10)
print(s)
print(m)
#pickle.dump(s, open("tmp.txt", "wb"))
count, bins, ignored = plt.hist(np.random.weibull(5.,1000))
plt.show()