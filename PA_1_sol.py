import random
import math

def distance_between_2_points(p1, p2, p3, p4):

    points_coordinates = []

    points_coordinates.append((p1, p2))
    points_coordinates.append((p3, p4))
    
    p5 = random.random() * 10 - 5
    p6 = random.random() * 10 - 5
    points_coordinates.append((p5, p6))
    
    print("P3x is " + str(p5))
    print("P3y is " + str(p6))
    
    distance = 0
    a = points_coordinates[0]
    b = points_coordinates[1]
    for item in points_coordinates[::-1]:
        for col in points_coordinates[::-1]:
            if math.sqrt((item[0] - col[0]) * (item[0] - col[0]) + math.pow(item[1] - col[1], 2)) > distance:
                distance = math.sqrt(math.pow(item[1] - col[1], 2) + (item[0] - col[0]) * (item[0] - col[0]))
                a = item
                b = col

    print("A " + str(a) + ", B" + str(b) + ", d:" + str(distance))



def main():
    print("Please add points coordinates!")
    p1 = float(input("P1x: "))
    print("P1x is " + str(p1))
    p2 = float(input("P1y: "))
    print("P1y is " + str(p2))
    p3 = float(input("P2x: "))
    print("P2x is " + str(p3))
    p4 = float(input("P2y: "))
    print("P2y is " + str(p4))
    print(distance_between_2_points(p1, p2, p3, p4))


if __name__ == '__main__':
    main()