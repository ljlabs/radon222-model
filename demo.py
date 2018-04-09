"""
kyle jordaan phy 312 radon detector Demo
3538638


this is the demo application that will be using the radon Detector
(detector.py) class to measure the energy lost by radon 222 during its radon_decay
process in side of an EPERM L-chamber. this data is then graphed using matplotlib
and displayed in a web browser
"""

# this is used to create measue the energy lost due to decay
from detector import Detector
# this is used to plot the energy lost vs the total energy possible to loose
from matplotlib import pyplot as plt

"""
these specify the constant properties of the detector and the particles being
detected
"""
# this is the radius of the L-chamber in cm
radius_of_detector = 3.75
# the distance an alpha particle at 5.49Mev will travel at the specified
# tempreture and pressure
"""There does exist a formula to find the specific range will update this when
I find  it"""
range_of_alpha = 4.49

# this creates a detector object giving it the constants specified above as arguments
radonDetetor = Detector(radius_of_detector, range_of_alpha)
# this is part of the demo it will track the charge on the electret as the radon decays
chargeArray = []
# this will keep track of the total energy that the particle could possibly loose
# in the Detector this is variable as when the particle doesnt travel the
# particle may not be able to travel the entire distance of 4.12cm beacuse of the
# tempreture and preassure of the enviroment
eTotal = []
# this is just to keep track of the counts taken for the purpose of displaying
# it in the graph
count  = []
# this specifies the number of particles that will be let loose in the detector
# to find the number of energy lost by the radon during decay
for i in range(100):
    # this is the first test case just to help us not to work with empty arrays
    # and get errors in the first append
    if(eTotal == []):
        eTotal.append(5.49)
    # this is the subsequent appends and keeps track of the net energies that could have been lost
    else:
        eTotal.append(eTotal[-1] + 5.49)
    # here we tell the detector that a decay has occured
    radonDetetor.radon_decay()
    # here we track the energy lost by the alpha particle in the detector
    chargeArray.append(radonDetetor.charge)
    # here we keep track of the number of counts made for the graph
    count.append(i)

"""show the results in the terminal"""
# show the net energy loss
print("energy collected ", chargeArray[-1])
# show energy total possible loss
print("total energy", eTotal[-1])
# show the ratio of the energy loss and the total energy
print("energy recorded / total energy : ", chargeArray[-1] / eTotal[-1])

"""display graph"""
# show the total energy
plt.scatter(count, eTotal)
# show the energy loss
plt.scatter(count, chargeArray, marker='.')
# dsiplay the graph
plt.show()
