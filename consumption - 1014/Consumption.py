__author__ = 'igor'

totalDistance = float( raw_input() )
spentFuel = float( raw_input() )

carConsumption = totalDistance / spentFuel

print("%.3f km/l" % carConsumption)