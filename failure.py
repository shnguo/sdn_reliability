import matplotlib.pyplot as plt
import numpy as np
import math
x = np.arange(23)
print(x)
y = 0.2565*np.power(np.e,(-0.2256)*x)
d1 = np.random.random_integers(-1, 1, 23)/500
y=y+d1
y.sort()
y[:] = y[::-1]
print(y)
fig, ax = plt.subplots()
line=ax.plot(x,y,'bo-')
plt.xlabel('Link(i), in decreasing order of link failure rate')
plt.ylabel('Link failure rate')
ax.legend((line[0],),('Link failure rate',),) 
#plt.savefig('../IEEEtran5/Link-failure-rate')
plt.savefig('../IEEEtran5/Link-failure-rate.eps', format='eps') 
plt.show()