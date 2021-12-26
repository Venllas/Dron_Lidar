import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
lidar = pd.read_csv("DATOS 1.csv")

lidar = np.array(lidar)
x = lidar[:,0]/1000
y = lidar[:,1]/1000
z = lidar[:,2]

fig = plt.figure()
ax1 = plt.axes(projection='3d')
ax1.scatter(x,y,z,c=z, cmap='viridis',linewidth=5)
plt.show()
                                                    