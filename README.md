# Geometry
Checks if various points and 3D objects are strictly inside or intersecting another 3D object in the 3 dimensional planes.

This document compiles all the classes and functions that Geometry.py can do.

Classes:
  - Point
  
  - Sphere
    - is_inside_point: determines if a Point is strictly inside this Sphere
    - is_inside_sphere: determines if another Sphere is strictly inside this Sphere
    - is_inside_cube: determines if a Cube is strictly inside this Sphere
    - is_inside_cyl: determines if a Cylinder is strictly inside this Sphere
    - does_intersect_sphere: determines if another Sphere intersects this Sphere
    - does_intersect_cube: determines if a Cube intersects this Sphere
    - circumscribe_cube: returns the largest Cube that can fit inside this Sphere where all eight corners of the Cube are on the Sphere.
   
  - Cube
    is_inside_point: determines if a Point is strictly inside this Cube
    - is_inside_sphere: determines if a Sphere is strictly inside this Cube
    - is_inside_cube: determines if another Cube is strictly inside this Cube
    - is_inside_cyl: determines if a Cylinder is strictly inside this Cube
    - does_intersect_cube: determines if another Cube intersects this Cube
    - intersection_volume: determines the volume of intersection between two cubes
    - inscribe_sphere: returns the largest Sphere that fits inside this Cube
  
  - Cylinder
    - is_inside_point: determines if a Point is strictly inside this Cylinder
    - is_inside_sphere: determines if a Sphere is strictly inside this Cylinder
    - is_inside_cube: determines if a Cube is strictly inside this Cylinder
    - is_inside_cyl: determines if another Cylinder is strictly inside this Cylinder
    - does_intersect_cylinder: determines if another Cylinder intersects this Cylinder
