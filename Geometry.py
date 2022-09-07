#  File: Geometry.py

#  Description: Checks is various 3D shapes are inside one another.

#  Student Name: Austin Kwa

#  Student UT EID: ak38754

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51125

#  Date Created: 2/6/2022

#  Date Last Modified: 2/7/2022

import math
from pickle import FALSE
import sys

class Point (object):
    # constructor with default values
    def __init__ (self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    # create a string representation of a Point
    # returns a string of the form (x, y, z)
    
    def __str__ (self):
        return '(' + format(self.x, '.1f') + ', ' + format(self.y, '.1f') + ', ' + format(self.z, '.1f') + ')'
    
    # get distance to another Point object
    # other is a Point object
    # returns the distance as a floating point number
    def distance (self, other):
        return math.hypot(self.x - other.x, self.y - other.y, self.z - other.z)

    # test for equality between two points
    # other is a Point object
    # returns a Boolean
    def __eq__ (self, other):
        tol = 1.0e-6
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol) and (abs(self.z - other.z) < tol))

class Sphere (object):
    # constructor with default values
    def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
        self.center = Point(x, y, z)
        self.radius = radius
    # returns string representation of a Sphere of the form:
    # Center: (x, y, z), Radius: value
    def __str__ (self):
        return 'Center: (' + format(self.center.x, '.1f') + ', ' + format(self.center.y, '.1f') + ', ' + format(self.center.z, '.1f') + '), Radius: ' + format(self.radius, '.1f')

    # compute surface area of Sphere
    # returns a floating point number
    def area (self):
        return 4 * math.pi * math.pow(self.radius, 2)

    # compute volume of a Sphere
    # returns a floating point number
    def volume (self):
        return 4 * math.pi * math.pow(self.radius, 3) / 3

    # determines if a Point is strictly inside the Sphere
    # p is Point object
    # returns a Boolean
    def is_inside_point (self, p):
        d = self.center.distance(p)
        if d < self.radius:
            return True
        else:
            return False

    # determine if another Sphere is strictly inside this Sphere
    # other is a Sphere object
    # returns a Boolean
    def is_inside_sphere (self, other):
        d = self.center.distance(other.center) + other.radius
        if d < self.radius:
            return True
        else:
            return False

    # determine if a Cube is strictly inside this Sphere
    # determine if the eight corners of the Cube are strictly 
    # inside the Sphere
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube (self, a_cube):
        tally = 0
        half = a_cube.side / 2 
        cornerA = Point(a_cube.center.x - half, a_cube.center.y + half, a_cube.center.z + half)
        cornerB = Point(a_cube.center.x + half, a_cube.center.y + half, a_cube.center.z + half)
        cornerC = Point(a_cube.center.x - half, a_cube.center.y - half, a_cube.center.z + half)
        cornerD = Point(a_cube.center.x + half, a_cube.center.y - half, a_cube.center.z + half)
        cornerE = Point(a_cube.center.x - half, a_cube.center.y + half, a_cube.center.z - half)
        cornerF = Point(a_cube.center.x + half, a_cube.center.y + half, a_cube.center.z - half)
        cornerG = Point(a_cube.center.x - half, a_cube.center.y - half, a_cube.center.z - half)
        cornerH = Point(a_cube.center.x + half, a_cube.center.y - half, a_cube.center.z - half)
        cube_corners = [cornerA, cornerB, cornerC, cornerD, cornerE, cornerF, cornerG, cornerH]
        for i in range(len(cube_corners)):
            if self.center.distance(cube_corners[i]) >= self.radius:
                return False
        return True

    # determine if a Cylinder is strictly inside this Sphere
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cyl (self, a_cyl):
        d_x_y_plane = math.hypot(self.center.x - a_cyl.center.x, self.center.y - a_cyl.center.y)

        if d_x_y_plane != 0:
            vectorX = math.fabs(a_cyl.center.x - self.center.x) / d_x_y_plane
            vectorY = math.fabs(a_cyl.center.y - self.center.y) / d_x_y_plane
            x = math.fabs(a_cyl.center.x - self.center.x) + (a_cyl.radius * vectorX)
            y = math.fabs(a_cyl.center.y - self.center.y) + (a_cyl.radius * vectorY)
        else:
            x = math.fabs(a_cyl.center.x - self.center.x) + a_cyl.radius
            y = math.fabs(a_cyl.center.y - self.center.y)

        z = math.fabs(a_cyl.center.z - self.center.z + (a_cyl.height / 2))
        d = math.sqrt(math.pow(x, 2) + math.pow(y, 2) + math.pow(z, 2))

        if d < self.radius:
            return True
        else:
            return False

    # determine if another Sphere intersects this Sphere
    # other is a Sphere object
    # two spheres intersect if they are not strictly inside
    # or not strictly outside each other
    # returns a Boolean
    def does_intersect_sphere (self, other):
        if self.center.distance(other.center) - other.radius < self.radius < self.center.distance(other.center) + other.radius:
            return True
        else:
            return False
    # determine if a Cube intersects this Sphere
    # the Cube and Sphere intersect if they are not
    # strictly inside or not strictly outside the other
    # a_cube is a Cube object
    # returns a Boolean
    def does_intersect_cube (self, a_cube):
        inside = 0
        outside = 0
        half = a_cube.side / 2 
        cornerA = Point(a_cube.center.x - half, a_cube.center.y + half, a_cube.center.z + half)
        cornerB = Point(a_cube.center.x + half, a_cube.center.y + half, a_cube.center.z + half)
        cornerC = Point(a_cube.center.x - half, a_cube.center.y - half, a_cube.center.z + half)
        cornerD = Point(a_cube.center.x + half, a_cube.center.y - half, a_cube.center.z + half)
        cornerE = Point(a_cube.center.x - half, a_cube.center.y + half, a_cube.center.z - half)
        cornerF = Point(a_cube.center.x + half, a_cube.center.y + half, a_cube.center.z - half)
        cornerG = Point(a_cube.center.x - half, a_cube.center.y - half, a_cube.center.z - half)
        cornerH = Point(a_cube.center.x + half, a_cube.center.y - half, a_cube.center.z - half)
        cube_corners = [cornerA, cornerB, cornerC, cornerD, cornerE, cornerF, cornerG, cornerH]
        for i in range(len(cube_corners)):
            if self.center.distance(cube_corners[i]) < self.radius:
                inside += 1
            else:
                outside += 1

        if inside > 0 and outside > 0:
            return True
        else:
            return False

    # return the largest Cube object that is circumscribed
    # by this Sphere
    # all eight corners of the Cube are on the Sphere
    # returns a Cube object
    def circumscribe_cube (self):
        s = self.radius * 2 / math.sqrt(3)
        return Cube(self.center.x, self.center.y, self.center.z, s)

class Cube (object):
    # Cube is defined by its center (which is a Point object)
    # and side. The faces of the Cube are parallel to x-y, y-z,
    # and x-z planes.
    def __init__ (self, x = 0, y = 0, z = 0, side = 1):
        self.center = Point(x, y, z)
        self.side = side

    # string representation of a Cube of the form: 
    # Center: (x, y, z), Side: value
    def __str__ (self):
        return 'Center: (' + format(self.center.x, '.1f') + ', ' + format(self.center.y, '.1f') + ', ' + format(self.center.z, '.1f') + '), Side: ' + format(self.side, '.1f')

    # compute the total surface area of Cube (all 6 sides)
    # returns a floating point number
    def area (self):
        return 6 * math.pow(self.side, 2)

    # compute volume of a Cube
    # returns a floating point number
    def volume (self):
        return math.pow(self.side, 3)

    # determines if a Point is strictly inside this Cube
    # p is a point object
    # returns a Boolean
    def is_inside_point (self, p):
        d_x = math.fabs(p.x - self.center.x)
        d_y = math.fabs(p.y - self.center.y)
        d_z = math.fabs(p.z - self.center.z)

        if (d_x < self.side / 2) and (d_y < self.side / 2) and (d_z < self.side / 2):
            return True
        else:
            return False

    # determine if a Sphere is strictly inside this Cube 
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere (self, a_sphere):
        neg_x = self.center.x - self.side / 2
        pos_x = self.center.x + self.side / 2
        neg_y = self.center.y - self.side / 2
        pos_y = self.center.y + self.side / 2
        neg_z = self.center.z - self.side / 2
        pos_z = self.center.z + self.side / 2
        
        sphere_neg_x = a_sphere.center.x - a_sphere.radius
        sphere_pos_x = a_sphere.center.x + a_sphere.radius
        sphere_neg_y = a_sphere.center.y - a_sphere.radius
        sphere_pos_y = a_sphere.center.y + a_sphere.radius
        sphere_neg_z = a_sphere.center.z - a_sphere.radius
        sphere_pos_z = a_sphere.center.z + a_sphere.radius

        if (neg_x < sphere_neg_x) and (pos_x > sphere_pos_x) and (neg_y < sphere_neg_y) and (pos_y > sphere_pos_y) and (neg_z < sphere_neg_z) and (pos_z > sphere_pos_z):
            return True
        else:
            return False

    # determine if another Cube is strictly inside this Cube
    # other is a Cube object
    # returns a Boolean
    def is_inside_cube (self, other):
        half = other.side / 2
        d_x = math.fabs(other.center.x - self.center.x) + half
        d_y = math.fabs(other.center.y - self.center.y) + half
        d_z = math.fabs(other.center.z - self.center.z) + half

        if (d_x < self.side / 2) and (d_y < self.side / 2) and (d_z < self.side / 2):
            return True
        else:
            return False

    # determine if a Cylinder is strictly inside this Cube
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cylinder (self, a_cyl):
        d_x = math.fabs(a_cyl.center.x - self.center.x) + a_cyl.radius
        d_y = math.fabs(a_cyl.center.y - self.center.y) + a_cyl.radius
        d_z = math.fabs(a_cyl.center.z - self.center.z) + a_cyl.height / 2
        if (d_x < self.side / 2) and (d_y < self.side / 2) and (d_z < self.side / 2):
            return True
        else:
            return False

    # determine if another Cube intersects this Cube
    # two Cube objects intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cube object
    # returns a Boolean
    def does_intersect_cube (self, other):
        half = other.side / 2
        d_x = math.fabs(other.center.x - self.center.x)
        d_y = math.fabs(other.center.y - self.center.y)
        d_z = math.fabs(other.center.z - self.center.z)

        if (d_x - half < self.side/2 < d_x + half) and (d_y - half < self.side/2 < d_y + half) and (d_z - half < self.side/2 < d_z + half):
            return True
        else:
            return False

    # determine the volume of intersection if this Cube 
    # intersects with another Cube
    # other is a Cube object
    # returns a floating point number
    def intersection_volume (self, other):
        l = math.fabs(other.center.x - self.center.x) - ((other.center.x + other.side / 2) - (self.center.x + self.side / 2))
        w = math.fabs(other.center.y - self.center.y) - ((other.center.y + other.side / 2) - (self.center.y + self.side / 2))
        h = math.fabs(other.center.z - self.center.z) - ((other.center.z + other.side / 2) - (self.center.z + self.side / 2))

        return l * w * h

    # return the largest Sphere object that is inscribed
    # by this Cube
    # Sphere object is inside the Cube and the faces of the
    # Cube are tangential planes of the Sphere
    # returns a Sphere object
    def inscribe_sphere (self):
        return Sphere(self.center.x, self.center.y, self.center.z, self.side / 2)

class Cylinder (object):
    # Cylinder is defined by its center (which is a Point object),
    # radius and height. The main axis of the Cylinder is along the
    # z-axis and height is measured along this axis
    def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
        self.center = Point(x, y, z)
        self.radius = radius
        self.height = height

    # returns a string representation of a Cylinder of the form: 
    # Center: (x, y, z), Radius: value, Height: value
    def __str__ (self):
        return 'Center: (' + format(self.center.x, '.1f') + ', ' + format(self.center.y, '.1f') + ', ' + format(self.center.z, '.1f') + '), Radius: ' + format(self.radius, '.1f') + ', Height: ' + format(self.height, '.1f')

    # compute surface area of Cylinder
    # returns a floating point number
    def area (self):
        return 2 * math.pi * self.radius * self.height + 2 * math.pi * math.pow(self.radius, 2)

    # compute volume of a Cylinder
    # returns a floating point number
    def volume (self):
        return math.pi * math.pow(self.radius, 2) * self.height

    # determine if a Point is strictly inside this Cylinder
    # p is a Point object
    # returns a Boolean
    def is_inside_point (self, p):
        d_x_y = math.hypot(math.fabs(p.x - self.center.x), math.fabs(p.y - self.center.y))
        z = math.fabs(p.z - self.center.z)
        if (d_x_y < self.radius) and (z < self.height / 2):
            return True
        else:
            return False

    # determine if a Sphere is strictly inside this Cylinder
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere (self, a_sphere):
        d_x_y = math.hypot(math.fabs(a_sphere.center.x - self.center.x), math.fabs(a_sphere.center.y - self.center.y))
        z = math.fabs(a_sphere.center.z - self.center.z) + a_sphere.radius
        if (d_x_y + a_sphere.radius < self.radius) and (z < self.height / 2):
            return True
        else:
            return False

    # determine if a Cube is strictly inside this Cylinder
    # determine if all eight corners of the Cube are inside
    # the Cylinder
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube (self, a_cube):
        center_to_edge = a_cube.side * math.sqrt(2) / 2
        d_x_y = math.hypot(math.fabs(a_cube.center.x - self.center.x), math.fabs(a_cube.center.y - self.center.y))
        z = math.fabs(a_cube.center.z - self.center.z) + (a_cube.side / 2)
        if (d_x_y + center_to_edge < self.radius) and (z < self.height / 2):
            return True
        else:
            return False

    # determine if another Cylinder is strictly inside this Cylinder
    # other is Cylinder object
    # returns a Boolean
    def is_inside_cylinder (self, other):
        d_x_y = math.hypot(math.fabs(other.center.x - self.center.x), math.fabs(other.center.y - self.center.y))
        z = math.fabs(other.center.z - self.center.z) + (other.height / 2)
        if (d_x_y + other.radius < self.radius) and (z < self.height / 2):
            return True
        else:
            return False

    # determine if another Cylinder intersects this Cylinder
    # two Cylinder object intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cylinder object
    # returns a Boolean
    def does_intersect_cylinder (self, other):
        d_x_y = math.hypot(math.fabs(other.center.x - self.center.x), math.fabs(other.center.y - self.center.y))
        z = other.center.z - self.center.z
        if(d_x_y - other.radius < self.radius < d_x_y + other.radius) and (z - other.height / 2 < self.height / 2 < z + other.height / 2):
            return True
        else:
            return False

def main():
    # read data from standard input

    # read the coordinates of the first Point p
    p_coords_in = sys.stdin.readline()
    p_coords_in = p_coords_in.split()
    p_coords = p_coords_in[0:3]
    for i in range(len(p_coords)):
        p_coords[i] = float(p_coords[i])

    # create a Point object 
    point_p = Point(p_coords[0], p_coords[1], p_coords[2])

    # read the coordinates of the second Point q
    q_coords_in = sys.stdin.readline()
    q_coords_in = q_coords_in.split()
    q_coords = q_coords_in[0:3]
    for i in range(len(q_coords)):
        q_coords[i] = float(q_coords[i])

    # create a Point object 
    point_q = Point(q_coords[0], q_coords[1], q_coords[2])

    # read the coordinates of the center and radius of sphereA
    sphereA_coords_in = sys.stdin.readline()
    sphereA_coords_in = sphereA_coords_in.split()
    sphereA_coords = sphereA_coords_in[0:4]
    for i in range(len(sphereA_coords)):
        sphereA_coords[i] = float(sphereA_coords[i])

    # create a Sphere object 
    sphereA = Sphere(sphereA_coords[0], sphereA_coords[1], sphereA_coords[2], sphereA_coords[3])

    # read the coordinates of the center and radius of sphereB
    sphereB_coords_in = sys.stdin.readline()
    sphereB_coords_in = sphereB_coords_in.split()
    sphereB_coords = sphereB_coords_in[0:4]
    for i in range(len(sphereB_coords)):
        sphereB_coords[i] = float(sphereB_coords[i])

    # create a Sphere object
    sphereB = Sphere(sphereB_coords[0], sphereB_coords[1], sphereB_coords[2], sphereB_coords[3])

    # read the coordinates of the center and side of cubeA
    cubeA_coords_in = sys.stdin.readline()
    cubeA_coords_in = cubeA_coords_in.split()
    cubeA_coords = cubeA_coords_in[0:4]
    for i in range(len(cubeA_coords)):
        cubeA_coords[i] = float(cubeA_coords[i])

    # create a Cube object 
    cubeA = Cube(cubeA_coords[0], cubeA_coords[1], cubeA_coords[2], cubeA_coords[3])

    # read the coordinates of the center and side of cubeB
    cubeB_coords_in = sys.stdin.readline()
    cubeB_coords_in = cubeB_coords_in.split()
    cubeB_coords = cubeB_coords_in[0:4]
    for i in range(len(cubeB_coords)):
        cubeB_coords[i] = float(cubeB_coords[i])

    # create a Cube object 
    cubeB = Cube(cubeB_coords[0], cubeB_coords[1], cubeB_coords[2], cubeB_coords[3])

    # read the coordinates of the center, radius and height of cylA
    cylA_coords_in = sys.stdin.readline()
    cylA_coords_in = cylA_coords_in.split()
    cylA_coords = cylA_coords_in[0:5]
    for i in range(len(cylA_coords)):
        cylA_coords[i] = float(cylA_coords[i])

    # create a Cylinder object 
    cylA = Cylinder(cylA_coords[0], cylA_coords[1], cylA_coords[2], cylA_coords[3], cylA_coords[4])

    # read the coordinates of the center, radius and height of cylB
    cylB_coords_in = sys.stdin.readline()
    cylB_coords_in = cylB_coords_in.split()
    cylB_coords = cylB_coords_in[0:5]
    for i in range(len(cylB_coords)):
        cylB_coords[i] = float(cylB_coords[i])

    # create a Cylinder object
    cylB = Cylinder(cylB_coords[0], cylB_coords[1], cylB_coords[2], cylB_coords[3], cylB_coords[4])

    # print if the distance of p from the origin is greater
    # than the distance of q from the origin
    if point_p.distance(Point(0, 0, 0)) > point_q.distance(Point(0, 0, 0)):
        print('Distance of Point p from the origin is greater than the distance of Point q from the origin')
    else:
        print('Distance of Point p from the origin is not greater than the distance of Point q from the origin')

    # print if Point p is inside sphereA
    if sphereA.is_inside_point(point_p):
        print('Point p is inside sphereA')
    else:
        print('Point p is not inside sphereA')

    # print if sphereB is inside sphereA
    if sphereA.is_inside_sphere(sphereB):
        print('sphereB is inside sphereA')
    else:
        print('sphereB is not inside sphereA')

    # print if cubeA is inside sphereA
    if sphereA.is_inside_cube(cubeA):
        print('cubeA is inside sphereA')
    else:
        print('cubeA is not inside sphereA')

    # print if cylA is inside sphereA
    if sphereA.is_inside_cyl(cylA):
        print('cylA is inside sphereA')
    else:
        print('cylA is not inside sphereA')

    # print if sphereA intersects with sphereB
    if sphereB.does_intersect_sphere(sphereA):
        print('sphereA does intersect sphereB')
    else:
        print('sphereA does not intersect sphereB')

    # print if cubeB intersects with sphereB
    if sphereB.does_intersect_cube(cubeB):
        print('cubeB does intersect sphereB')
    else:
        print('cubeB does not intersect sphereB')

    # print if the volume of the largest Cube that is circumscribed 
    # by sphereA is greater than the volume of cylA
    if sphereA.circumscribe_cube().volume() > cylA.volume():
        print('Volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA')
    else:
        print('Volume of the largest Cube that is circumscribed by sphereA is not greater than the volume of cylA')

    # print if Point p is inside cubeA
    if cubeA.is_inside_point(point_p):
        print('Point p is inside cubeA')
    else:
        print('Point p is not inside cubeA')

    # print if sphereA is inside cubeA
    if cubeA.is_inside_sphere(sphereA):
        print('sphereA is inside cubeA')
    else:
        print('sphereA is not inside cubeA')

    # print if cubeB is inside cubeA
    if cubeA.is_inside_cube(cubeB):
        print('cubeB is inside cubeA')
    else:
        print('cubeB is not inside cubeA')

    # print if cylA is inside cubeA
    if cubeA.is_inside_cylinder(cylA):
        print('cylA is inside cubeA')
    else:
        print('cylA is not inside cubeA')

    # print if cubeA intersects with cubeB
    if cubeB.does_intersect_cube(cubeA):
        print('cubeA does intersect cubeB')
    else:
        print('cubeA does not intersect cubeB')

    # print if the intersection volume of cubeA and cubeB
    # is greater than the volume of sphereA
    if cubeA.intersection_volume(cubeB) > sphereA.volume():
        print('Intersection volume of cubeA and cubeB is greater than the volume of sphereA')
    else:
        print('Intersection volume of cubeA and cubeB is not greater than the volume of sphereA')

    # print if the surface area of the largest Sphere object inscribed 
    # by cubeA is greater than the surface area of cylA
    if cubeA.inscribe_sphere().area() > cylA.area():
        print('Surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA')
    else:
        print('Surface area of the largest Sphere object inscribed by cubeA is not greater than the surface area of cylA')

    # print if Point p is inside cylA
    if cylA.is_inside_point(point_p):
        print('Point p is inside cylA')
    else:
        print('Point p is not inside cylA')

    # print if sphereA is inside cylA
    if cylA.is_inside_sphere(sphereA):
        print('sphereA is inside cylA')
    else:
        print('sphereA is not inside cylA')

    # print if cubeA is inside cylA
    if cylA.is_inside_cube(cubeA):
        print('cubeA is inside cylA')
    else:
        print('cubeA is not inside cylA')

    # print if cylB is inside cylA
    if cylA.is_inside_cylinder(cylB):
        print('cylB is inside cylA')
    else:
        print('cylB is not inside cylA')

    # print if cylB intersects with cylA
    if cylA.does_intersect_cylinder(cylB):
        print('cylB does intersect cylA')
    else:
        print('cylB does not intersect cylA')
    
    print(point_p)

if __name__ == "__main__":
    main()
