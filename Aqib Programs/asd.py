import numpy as np
import matplotlib .pyplot as plt

U = 3
b = 1
p = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

xpoints = []
ypoints = []
for items in p:
    P = items 
    y = np.linspace(0, 1, 100)

    u = ((-P*U)/(b**2))*(y**2-b*y)-U*((y/b)-1)
    
    xpoints = u
    ypoints = y

plt.title("Graph For Coutte flow if top plane is stationary and bottom platter is moving in the positive direction")
plt.plot(xpoints, ypoints)
plt.xlabel("u")
plt.ylabel("y")
plt.show()