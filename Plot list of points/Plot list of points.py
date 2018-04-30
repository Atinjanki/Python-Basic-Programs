#Take as input points from user and plot those points on graph

import numpy as np
import matplotlib.pyplot as plt

coordinates=[]
temp=[]
points = int(input("Enter number of points: "))

#Take input the co-ordinates of points and store it in array
for i in range(0,points):
    print('Enter X co-ordinate of point', i+1)
    x_coordinate = int(input())
    print('Enter Y co-ordinate of point', i+1)
    y_coordinate = int(input())
    temp=[]
    temp.append(x_coordinate)
    temp.append(y_coordinate)
    coordinates.append(temp)

print('All co-ordinates are: ',coordinates)

#Ploting on graph
splitting_coordinates = np.array(coordinates)
x,y = splitting_coordinates.T
plt.scatter(x,y)
plt.show()