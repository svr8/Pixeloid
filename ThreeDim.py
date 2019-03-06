#!/usr/bin/python3
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import time
import sys, termios, tty, os
from random import uniform

# import sys, termios, tty, os, time

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

pointCount = 1000

x = np.random.rand(pointCount)
y = np.random.rand(pointCount)
z = np.random.rand(pointCount)

colorList = ["#0000FF", "#00FF00", "#FF0000"]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

scatterList = []
for index in range(0, pointCount):
  scatterList.append( ax.scatter(x[index], y[index], z[index], color=colorList[index%3]) )

fig.canvas.draw()
plt.show()

# last_scatter = 24

# while True:
#   char = getch()
#   print(char)
#   if(char == 'e'): break
#   elif(char == 'd'): fig.canvas.draw()
#   elif(char == 'u'): 
#     scatterList[last_scatter].remove()
#     fig.canvas.draw()
#     last_scatter = last_scatter - 1
