"""
kyle jordaan phy 312 operations
3538638

this is a set of commanly used simple math functions
"""

# we use the trig function for conversion between spherical and cartesian
from math import sin, cos, sqrt

# this is a basic 2 vector in 3d space addition function
def vectorAddition(A, B):
    return([A[0]+B[0], A[1]+B[1], A[2]+B[2]])

# this converts spherical coordinates to cartesian coordinates
def sperical_to_cartesian(r, theta, phi):
    # this uses the generic spherical to cartesian formula and returns it as a 3D vector
    return([r*sin(theta)*cos(phi),
        r*sin(theta)*sin(phi),
        r*cos(theta)])
# this finds the length of the vector as the distance from the origin to that 3d position
def sizeOf(vect):
    return(sqrt((vect[0]**2) + (vect[1]**2) + (vect[2]**2)))
