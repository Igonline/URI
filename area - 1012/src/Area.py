__author__ = 'igor'

values = raw_input().split(' ')
a = float(values[0])
b = float(values[1])
c = float(values[2])

triaArea = (a * c) / 2.0
circArea =  3.14159 * c * c
trapArea = ((a + b) * c) / 2.0
squareArea = b * b
recArea = a * b

print ("TRIANGULO: %.3f\n" \
      "CIRCULO: %.3f\n" \
      "TRAPEZIO: %.3f\n" \
      "QUADRADO: %.3f\n" \
      "RETANGULO: %.3f" % (triaArea, circArea, trapArea, squareArea, recArea)
    )
