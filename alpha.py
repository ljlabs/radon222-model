"""
kyle jordaan phy 312 alpha
3538638

this is the model of the alpha particle
"""
"""imports"""
import random # this lets us fire the alpha in a random direction
import operations # gives us access to those shared operations
from math import pi #uses the math constant pi (3.14...)


max_theta = pi    # 1 half revoloution either going up or down
max_phi = 2*pi      # 1 full revoloution going left right etc


"""
this class allows us to check if the alpha particle has moved outside the of the bounds
of the detector.
it does this by
-  checking its distance from the origin:
    if it is greater than r (the raduis of the L-chamber) it is said to
    be outside the detector
"""
class Alpha:
    # initilization
    def __init__(self, range_of_alpha):
        self.theta = random.random() * max_theta # the random direction of the alpha
        self.phi = random.random() * max_phi # the random direction of the alpha
        self.distance_traveled = 0  # keep track of the distance the alpha particle traveled
        self.max_range = range_of_alpha # keep track of the maximum distance the alpha can travel

    """this check if the alpha particle has moved outside the bounds of the detector"""
    def isInsideDetector(self, dr, n, initialPositionVector, max_r):
        deltaR = dr*n # keep track of how far the alpha particle has moved
        """we check the new position of the alpha particle after it has moved deltaR cm"""
        # its postion after being moved
        positionVectorAlphaHasTraveled =operations.sperical_to_cartesian(deltaR, self.theta, self.phi)
        """this is the specific case where the alpha particle moves below the base of the hemisphere of the L-chamber"""
        if(positionVectorAlphaHasTraveled[2] < 0): # if the particle moves below the base
            return False
        # its displacement vector equivelent to vector from origin to final position
        displacement_vector = operations.vectorAddition(initialPositionVector, positionVectorAlphaHasTraveled)
        if(operations.sizeOf(displacement_vector) < max_r): # check if the displacement vector
             #  is longer than the radius of the L-chamber
            self.distance_traveled = deltaR # keep track of the distance traveled when still inside L-chamber
            return True # says the alpha particle is inside the dome
        return False # says the alpha particle is outside the dome
