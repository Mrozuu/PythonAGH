import math


def quadratic_equation(a, b, c):
    delta = b * b - 4 * a * c
    if delta > 0:
        x1 = round((-1 * b - math.sqrt(delta)) / (2 * a), 2)
        x2 = round((-1 * b + math.sqrt(delta)) / (2 * a), 2)
        print("Roots: " + str(x1) + ", " + str(x2))
    elif delta == 0:
        x1 = round((-1 * b) / (2 * a), 2)
        print("Root: " + str(x1))
    else:
        print("No roots")


a1 = float(input("a: "))
b1 = float(input("b: "))
c1 = float(input("c: "))
quadratic_equation(a1, b1, c1)
