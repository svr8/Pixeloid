# from mpl_toolkits.mplot3d import axes3d
# import matplotlib.pyplot as plt
# import numpy as np

# fig = plt.figure()
# ax = fig.add_subplot(111,projection='3d')

# # Set up the grid in polar
# theta = np.linspace(0,2*np.pi,90)
# r = np.linspace(0,3,50)
# T, R = np.meshgrid(theta, r)

# # Then calculate X, Y, and Z
# X = R * np.cos(T)
# Y = R * np.sin(T)
# Z = np.sqrt(X**2 + Y**2) - 1

# ax.plot_wireframe(X, Y, Z)

# ax.set_zlim(0,2)

# plt.show()
##################################

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

X= np.arange(-2,3,.1)
Z=np.arange(-2,3,.1)
X,Z = np.meshgrid(X,Z)
Y=np.sqrt((Z+1)**2-X**2)
Y2=np.sqrt(4*Z-X**2)
ax.plot_wireframe(X, Y, Z, rstride = 1, cstride =1)
ax.plot_wireframe(X, -Y, Z, rstride = 1, cstride =1)
ax.plot_surface(X,Y2,Z,rstride=1,cstride=1,color='red')
ax.plot_surface(X,-Y2,Z,rstride=1,cstride=1,color='red')
ax.set_zlim(0,2)

plt.show()