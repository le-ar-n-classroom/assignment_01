  
""" 
3. Write a code that generates a nested list with 2D point coordinates to generate a XY point grid
Expected result: list_points = [[x1,y1], [x1,y2],...[xn,yn]]
"""
import matplotlib.pyplot as plt

x_size = 10
y_size = 6

list_points = []
### insert code here

def display_pt(list_points):
    for pt in list_points:
        plt.plot(pt[0],pt[1], 'bo')

plt.figure()
display_pt(list_points)
plt.axis('equal')
plt.show()
