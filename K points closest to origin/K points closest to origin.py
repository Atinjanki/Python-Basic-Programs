import matplotlib.pyplot as plt
from random import randint
from heapq import heappush, heappop, heapify, heappushpop
from math import sqrt
import numpy as np

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

#To calculate hypotenuse (distance from origin to the point)
def distance(pointA, pointB):
    return sqrt((pointB[0] - pointA[0]) ** 2 + (pointB[1] - pointA[1]) ** 2)

def closest(points, k, origin):
    heap = [(-distance(p, origin), p) for p in points[:k]]
    heapify(heap)

    for p in points[k:]:
        d = distance(p, origin)
        if d < -heap[0][0]:
            heappushpop(heap, (-d, p))
    return [p for nd, p in heap]

def naive(points, k, origin):
    sortedPoints = sorted(points, key=lambda p: distance(p, origin))
    return sortedPoints[:k]

points = coordinates

k = input('Enter number of k: ')
k = int(k)
resA = closest(points, k, (0, 0))
resB = naive(points, k, (0, 0))
plt.scatter(*zip(*points))
plt.scatter(*zip(*resA))
plt.scatter(*zip(*resB))
plt.show()