"""
kyle jordaan phy 312 radon
3538638

this creates a radon model. we can model the distance traveled and the energy
lost by the alpha particle due to that distance

this object will contain the alpha particle
when created it will create a radom x,y,z coordinate inside of a hemisphere
"""
import random   # this is used to position the randon in a random position
from math import pi, sin, cos, e # these are various maths funciton
import operations   # these are shared functions used by this and other classes
from alpha import Alpha # this is the model of the alpha particle produced in
                        #the decay of this radon

"""
constants about the enviroment in which the radon may spawn
"""
max_theta = pi/2    # 1 full revoloution
max_phi = 2*pi      # 1 upper hemisphere

"""
we also need to initilize the radon222  by creating objects and constants
    - energy_loss
    - max_range
    - theta
    - phi
    - r
    - alpha
    -initialPositionVector
this object will be able find the distance traveled of an alpha particle
    - this is done by spawning in a radom position
    - firing an alpha particle in a random direction
    - checking if it travels its full distance or is stopped by the dome of the L-chamber
    - and recording this distance

also we find the energy lost by the alpha particle
    -by use of the model of the bragg curve
"""
class Radon:
    # we initializer
    def __init__(self, radius_of_detector, range_of_alpha):
        self.energy_loss = 0 # to keep track of the energy lost by the alpha
        self.max_range = radius_of_detector # radius of dome of the L-chamber
        """generate a random position inside the dome in spherical coordinates"""
        theta = random.random() * max_theta # theta
        phi = random.random() * max_phi # phi
        r = random.random() * self.max_range# r
        """create an alpha particle object"""
        self.alpha = Alpha(range_of_alpha) # it needs to know how far the maximum
                                           # distance the alhpa particle may travel
        """ creates the position vecotor in cartesian coordinates using the spherial coordinates"""
        # it does this using the sperical_to_cartesian function found in the operations class
        self.initialPositionVector = operations.sperical_to_cartesian(r, theta, phi)
    """
    finds the total distance the alpha particle may travel after radon decay
        - it does this by moving the alpha particle dr (0.01) cm in the generated
        direction until the particle has moved the maximum range of the alpha particle
        - we create a loop n=0 while n*dr < max range of the alpha particle and
        the particle is inside the dome:
            - we check if the particle is inside the dome by checking its distance
            from the origin:
                if it is greater than r (the raduis of the L-chamber) it is said to
                be outside the detector
            - if its still inside N += 1
        - when the loop ends we check if the particle exited the chamebr
            if it did we return the dr * (n - 1)
            else we return dr * n

    N.B. self.alpha.distance_traveled is simply dr*n only it is computed inside the alpha object
    """
    def getDistanceTraveled(self):
        dr = 0.01 # the change in position of the alpha particle with each cycle of the loop
        n = 0 # the number of movements counted inside of the while loop
        """the loop takes into considiration if the alpha is still inside the Detector
        as well as if the alpha has not yet moved past its maximum range"""
        while(self.alpha.isInsideDetector(dr, n, self.initialPositionVector, self.max_range) and n*dr < self.alpha.max_range):
            n += 1 # we increment the counter with each loop
        return(self.alpha.distance_traveled) 

    """
    this computes the energy lost by the alpha particle by use of the bragg curve
    i have modeled the bragg curve using a mixture of piecewise and exponential functions
    """
    def get_energy_loss(self):
        x = self.alpha.distance_traveled # this is the distance that the alpha particle has traveled inside the dome
        """ this is the piece wise function resposnible for modeling the bragg curve"""
        if(x < 3.67):
            self.energy_loss = 0.85*x + 0.04*e**x - 0.04
        else:
            if(x < 4.12):
                self.energy_loss = 4.65 - 9.1643 - (8.176694909082223**-15) * 2002.72**x + 2.5*x
            else:
                self.energy_loss=5.49
        return self.energy_loss # this simply returns the value produced by the bragg curve model
