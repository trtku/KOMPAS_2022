import matplotlib.pyplot as plt
import math
import random
import noise



""" ---------- random noise ---------- """

fig1, ax = plt.subplots()
height = 100
width = 100
grid = []

for x in range(0, width):
    row = []
    for y in range(0, height):
        
        r = random.random()
        color = [r, r, r]
        row.append(color)
    grid.append(row)

ax.imshow(grid, cmap='viridis')
plt.show()



""" ---------- perlin noise ---------- """

# fig1, ax = plt.subplots()
# height = 100
# width = 100
# grid = []

# shape = (1024,1024)
# scale = 0.1
# octaves = 6
# persistence = 0.5
# lacunarity = 2.0

# for x in range(0, width):
#     row = []
#     for y in range(0, height):
        
#         r = noise.pnoise2(x*scale, 
#                         y*scale, 
#                         octaves=octaves, 
#                         persistence=persistence, 
#                         lacunarity=lacunarity, 
#                         repeatx=1024, 
#                         repeaty=1024, 
#                         base=0)
        
#         r_remapped = 0.5*(r+1)
#         color = [r_remapped, r_remapped, r_remapped]
#         row.append(color)
#     grid.append(row)

# ax.imshow(grid, cmap='viridis')
# plt.show()



""" ---------- voronoi ---------- """

def map(value, low1, high1, low2, high2):
    return low2 + (value - low1) * (high2 - low2) / (high1 - low1)

def dist(x1,y1,x2,y2):
    return (x2 - x1)**2 + (y2 - y1)**2

# grid = []
# num_points = 25
# points = []
# height = 400
# width = 400

# fig1, ax2 = plt.subplots()


# for i in range(num_points):
#     points.append( (random.randint(0,width), random.randint(0,height)) )
   

# for x in range(0, width):
#     row = []
#     for y in range(0, height):
#         distances = []
        
#         for i in range(num_points):
            
#             v = points[i]
#             d = dist(x, y, v[0], v[1])
            
#             distances.append(d)
        
#         #sort distances
#         distances.sort()
#         color = map(distances[0], 0, 5000, 0.2, 0.9)
#         col = [ color, color, color ]
#         row.append(col)
#     grid.append(row)

# ax2.imshow(grid, cmap='viridis')

# x_coordinates = [p[1] for p in points]
# y_coordinates = [p[0] for p in points]

# ax2.plot(x_coordinates, y_coordinates, 'r+')
# plt.show()



""" ---------- vector field ---------- """

# fig1, ax = plt.subplots(1,1,figsize=(15,15))

# grid = []

# shape = (1024,1024)
# pscale = 100
# octaves = 6
# persistence = 0.5
# lacunarity = 2.0
# height = 400
# width = 400
# X = []
# Y = []
# angles = []

# for x in range(0, width, 8):
#     #row = []
#     for y in range(0, height, 8):
        
        
#         X.append(x)
#         Y.append(y)
#         angle = noise.pnoise2(x/pscale, 
#                         y/pscale, 
#                         octaves=octaves, 
#                         persistence=persistence, 
#                         lacunarity=lacunarity, 
#                         repeatx=1024, 
#                         repeaty=1024, 
#                         base=0)

#         angles.append(map(angle,-0.5,0.5,-math.pi,math.pi))

# U = []
# V = []

    
# for a in angles:
    
#     u =  math.cos(a)
#     v =  math.sin(a)

#     U.append(u)
#     V.append(v)

# plt.quiver(X,Y,U,V,scale = 50)
# plt.show()



""" ---------- class example ---------- """

class Rect(object):
    
    """A 'Rect' is defined by two opposite corners with x,y coordinates.
    Attributes
    ----------
    x1, y1 : float
        The coordinates of the bottom left front corner.
    x2, y2 : float
        The coordinates of the top right back corner.
    """
    def __init__(self, x1, y1, x2, y2):
        
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        
        self.cx = 0.5 * ( x1 + x2 )
        self.cy = 0.5 * ( y1 + y2 )

        #list of x and list of y coordinates
        self.x = [self.x1, self.x1, self.x2, self.x2]
        self.y = [self.y1, self.y2, self.y2, self.y1]
    
    def move(self, _x, _y):
        
        newX = []
        newY = []
        
        for x,y in zip(self.x,self.y):
            
            x += _x
            y += _y
            
            newX.append(x)
            newY.append(y)
        
        self.x = newX
        self.y = newY
    
    def rotate(self, angle):
        
        s = math.sin(angle)
        c = math.cos(angle)
        
        newX = []
        newY = []
        
        for x,y in zip(self.x,self.y):
            #move point to origin
            x -= self.cx
            y -= self.cy
            
            #rotate point
            
            xnew = x * c - y * s
            ynew = x * s + y * c

            #move point back
            x = xnew + self.cx
            y = ynew + self.cy
            
            newX.append(x)
            newY.append(y)
        
        self.x = newX
        self.y = newY    
    
    def display(self, colorv):
        plt.axis("equal")
        plt.fill(self.x, self.y, c=colorv, linewidth=1)


""" example 1 """
# #figure size
# plt.figure(figsize=(5,5))
# #set limits of axis
# plt.xlim(-50, 250)
# plt.ylim(-50, 250)

# r = Rect(0,0,200,200)
# r.display("pink")

# plt.show()

""" example 2 """
# #figure size
# plt.figure(figsize=(10,10))
# #set limits of axis
# plt.xlim(-50, 250)
# plt.ylim(-50, 250)

# rects = []
# gap = 20

# for x in range(5):
#     for y in range(5):
#         r = Rect(x*100 + x*gap, y*100+ y*gap, (x+1)*100+ x*gap, (y+1)*100+ y*gap )
#         rects.append(r)
# for rs in rects:
#     rs.display("pink")

# plt.show()

""" example 3 """
#figure size
# plt.figure(figsize=(10,10))
# #set limits of axis
# plt.xlim(-50, 250)
# plt.ylim(-50, 250)

# rects = []
# gap = 20

# for x in range(5):
#     for y in range(5):
#         r = Rect(x*100 + x*gap, y*100+ y*gap, (x+1)*100+ x*gap, (y+1)*100+ y*gap )
#         r.rotate(math.radians(30))
#         rects.append(r)
# for rs in rects:
#     rs.display("pink")
# plt.show()

""" exampel 4 """
# fig = plt.figure(figsize=(7, 7))

# rects = []
# gap = 3

# for x in range(7):
#     for y in range(20):
        
#         r = Rect(x*10 + x*gap, y*10+ y*gap, (x+1)*10+ x*gap, (y+1)*10+ y*gap )
        
#         degree = random.randint(-r.cy,r.cy) * 0.3 
#         distance = random.randint(0,r.cy) * 0.05
        
#         r.rotate( math.radians(0.75+degree))
#         r.move(distance , -distance)
#         rects.append(r)
        
# for r in rects:
#     ct = [random.random(), 0.5, 0.6, 0.4]
#     r.display(ct)
# plt.show()

