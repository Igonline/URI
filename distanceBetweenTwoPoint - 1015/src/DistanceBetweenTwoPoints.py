__author__ = 'igor'

def distanceBetweenTwoPoints (point1, point2):
    partialResult = (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2
    finalResult = partialResult ** 0.5
    return finalResult

point1 = raw_input().split(' ')
point2 = raw_input().split(' ')

point1 = [float(x) for x in point1]
point2 = [float(x) for x in point2]

print("%.4f" % distanceBetweenTwoPoints(point1, point2))
