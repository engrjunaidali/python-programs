import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp

for p in np.array([np.arange(- 5,5+1)]).reshape(-1):
    b = 2
    c = 3
    y = np.array([np.arange(0,2+0.01,0.01)])
    U = 3
    u = np.multiply(((np.multiply(-p,U))/(b**2)), (y**2 - np.multiply(b,y))) - np.multiply(U,((y / b) - 1))
    plt.plot(u,y, color='green', marker='o', linestyle='dashed', linewidth=1, markersize=1)
    
plt.show()