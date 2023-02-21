x0= int(input("input 2D x coordinate of first point:"));
y0= int(input("input 2D y coordinates of first point:"));
x1= int(input("input 2D x coordinates of second point:"));
y1= int(input("input 2D y coordinates of second point:"));
import math;
distance = math.sqrt( ((x0-x1)**2)+((y0-y1)**2) );
print(distance);