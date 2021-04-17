  
""" 
3. Write a code that generates a nested list with 2D point coordinates to generate a XY point grid
Expected result: list_points = [[x1,y1], [x1,y2],...[xn,yn]]
"""
import matplotlib.pyplot as plt

def display_pt(list_points):
    for l in list_points:
        for p in l:
            plt.plot(p[0],p[1],'bo')

x_size = 10
y_size = 6

list_points = []
### insert code here

plt.figure()
display_pt(list_points)
plt.axis('equal')
plt.show()
