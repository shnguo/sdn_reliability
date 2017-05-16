import  pickle
import numpy as np
from scipy.stats import dweibull
x = np.arange(1,43)/26
def weib(x,n,a):
     return (a / n) * (x / n)**(a - 1) * np.exp(-(x / n)**a)
y=weib(x,0.99,5)
max=np.amax(y)
y=y/max
print(y)

#pickle.dump(y, open("tmp.txt", "wb"))
#print(obj2)