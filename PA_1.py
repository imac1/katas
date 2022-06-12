print("Welcome to my mystery program!")

a=float(input("P1x: "))
print("P1x is " + str(a))
b=float(input("P1y: "))
print("P1y is " + str(b))
c=float(input("P2x: "))
print("P2x is " + str(c))
d=float(input("P2y: "))
print("P2y is " + str(d))
import random
import math
points_coordinates = []

points_coordinates.append((a,b))
points_coordinates.append((c,d))
points_coordinates.append((random.random() * 10 - 5, random.random() * 10 - 5))
print("P3x is " + str(points_coordinates[2][0]))
print("P3y is " + str(points_coordinates[2][1]))

x = 0
a = points_coordinates[0]
b = points_coordinates[1]
for p in points_coordinates[::-1]:
    for q in points_coordinates[::-1]:
        if math.sqrt((p[0] - q[0]) * (p[0] - q[0]) + math.pow(p[1] - q[1], 2)) > x:
            x = math.sqrt(math.pow(p[1] - q[1], 2) + (p[0] - q[0]) * (p[0] - q[0]))
            a = p
            b = q

print("A " + str(a) + ", B" + str(b) + ", d:" + str(x))
''' coordonatele punctelor care se afla la ea mai mare distanta si afiseaza distanta'''