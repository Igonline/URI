__author__ = 'igor'

EFFICIENCY = 12

timeSpentInTheTrip = input()
averageVelocity = input()

distance = timeSpentInTheTrip * averageVelocity

fuelSpent = distance / 12.0

print("%.3f" % fuelSpent)
