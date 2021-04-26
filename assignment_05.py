"""Write a Polyline class that uses the Point3d class and can return the length of the polyline
"""
import random
import math
import matplotlib.pyplot as plt

def display_pl(polyline):
    xs, ys = [], []
    for pt in polyline.points:
        xs.append(pt.x)
        ys.append(pt.y)
    plt.plot(xs,ys)

class Point3d():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    @property
    def data(self):
        return (x,y,z)

# Create class here



polyline = # Create object based on class Polyline here
polyline_length = # Polyline length class method function here
print(polyline_length)
plt.figure()
display_pl(polyline)
plt.show()