import math

print ("Enter the coordinates of the first point:\n")
x1 = int(input("x1: "))
y1 = int(input("y1: "))
print ("Enter the coordinates of the second point:\n")
x2 = int(input("x2: "))
y2 = int(input("y2: "))

print ("The distance between the two points is: " + str(math.sqrt((x2 - x1)**2 + (y2 - y1)**2)))