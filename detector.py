"""
kyle leon jordaan Phy 312 Detector
3538638

this is the detector class that measures the energy lost due to decaying Radon222
"""
# this is the radon class (radon.py)
from radon import Radon

"""
this detector is designed to record the energies lost by the decay of radon 222
this proces is doen using the radon model in radon.py class

the init function initilizes the function creating the variables
    chagre -
    distances -
    energies -
    radius_of_detector -
    range_of_alpha -
 this simply sets the values used by the radon_decay function

 the radon decay function decays a radon222 particle and records the energy lost by it
"""
class Detector:
    # initilizes default values and data types
    def __init__(self, radius_of_detector, range_of_alpha):
        self.charge = 0 #the charge in the Detector
        self.distances = [] # the distance traveled by the various alpha particles
        self.energies = [] # the energy lost by the alpha based on its distance
        self.radius_of_detector = radius_of_detector# constant based on the real
                                                    # world L-chamber
        self.range_of_alpha = range_of_alpha # distance that the subsequent alpha
                                             # particle travels based on the enviroment

    # radon_decay
    # this uses the radon 222 model to create 1 decay and measures the enrgy lost
    # we create a radon object in a random location
    # then fire an alpha particle in a random direction.
    # then measure the distance the alpha particle travels
    # then we measure energy lost due to that distnace by the bragg curve
    # and we record this energy
    def radon_decay(self):
        # create the radon object it want to know:
            # the total space it can be placed into
            # and the distance the create dalpha particle may travel
        rd = Radon(self.radius_of_detector, self.range_of_alpha)
        # we then find the distance the radon may travel while staying inside the detector
        distance = rd.getDistanceTraveled()
        # we then use this disctance to find the enrgy lost using the bragg curve
        energyLoss = rd.get_energy_loss()
        # we then store the distance traveled of the individual alpha particle
        self.distances.append(distance)
        # we store the energy lost of the individual alpha particle
        self.energies.append(energyLoss)
        # and we keep track of the net energy loss of all the alpha particles
        self.charge += energyLoss
