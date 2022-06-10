import matplotlib.pyplot as plt
import noise
import random
import math
from PIL import Image
from random import random as rand



""" ---------- generate a 2D grid made of points ---------- """

# N = 25
# x, y = [], []
# distance = 0.1

# for i in range(N):
#     for j in range(N):
#         x.append(i* distance)
#         y.append(j* distance)

# # create an empty figure
# plt.figure(figsize = (10,10))
# # plt.axis('equal')
# plt.axis('off')

# plt.scatter(x, y, s=5, c='red')
# plt.show()



""" ---------- diagonals version ---------- """

# plt.figure(figsize = (15,15))
# # plt.axis('equal')
# plt.axis('off')

# N=12
# x,y = [],[]
# d = 1.0

# for i in range(N):
#     x.append(i*d)
#     y.append(i*d)
# plt.scatter(x, y, s=900, c='green')

# for i in range(N):
#     x[i] += 1.0
# plt.scatter(x, y, s=600, c='red')

# for i in range(N):
#     y[i] += 2.0
# plt.scatter(x, y, s=100, color='blue')
# plt.show()



""" ---------- circle version ---------- """

# def draw_circle(N, radius, center_x, center_y):
#     x,y,c = [],[],[]
    
#     for i in range(N):
#         theta = math.pi * 2 * i/N
#         x.append(radius * math.cos(theta) + center_x)
#         y.append(radius * math.sin(theta) + center_y)
#         c.append([random.random()*abs(math.cos(theta)), random.random(),  random.random()*abs(math.sin(theta)), random.random()])
    
#     plt.scatter(x,y,s=50*radius, c=c)

# plt.figure(figsize = (15,15))
# plt.axis('off')

# draw_circle(N=30, radius=50, center_x=0, center_y=0)
# plt.show()



""" ---------- circles version ---------- """

# plt.figure(figsize = (15,15))
# plt.axis('equal')
# plt.axis('off')

# for i in range(30):
#     draw_circle(N=20, 
#                 radius=rand()*18, 
#                 center_x=rand()*100, 
#                 center_y=rand()*100)
# plt.show()

