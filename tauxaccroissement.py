import numpy as np
import matplotlib.pyplot as plt

N=[20]
t=20
n = np.arange(0, 41, 1)
for i in range(1,41):
  N.append(N[i-1]*(1+t/100))
  
 plt.plot(n, N)

plot.show()
