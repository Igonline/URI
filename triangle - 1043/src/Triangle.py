__author__ = 'igor'

def isTriangle(sides):
    if sides[0] > abs(sides[1] - sides[2]) and sides[0] < sides[1] + sides[2]:
        return True
    else:
        return False

sides = raw_input().split()
sides = [float(i) for i in sides]
perimeter = sides[0] + sides[1] + sides[2]

if isTriangle(sides):
    print("Perimetro = %.1f" % perimeter)
else:
    area = (sides[0] + sides[1]) * sides[2]
    area /= 2.0

    print("Area = %.1f" % area)
