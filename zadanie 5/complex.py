import math


class Complex(object):
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def convert_from_string(data):
        left, right = data.split(',')
        left = float(left)
        right = float(right)
        return Complex(left, right)


    def print(self):
        print(self.r, "+", self.i, "i")

    def coupling(self):
        self.i = self.i * (-1)

    def addition(self, c):
        return Complex(self.r + c.r, self.i + c.i)

    def subtraction(self, c):
        return Complex(self.r - c.r, self.i - c.i)

    def multiplication(self, c):
        return Complex(self.r * c.r - self.i * c.i,
                       self.r * c.i + self.i * c.r)

    def division(self, c):
        return Complex((self.r * c.r + self.i * c.i) / ((c.r ** 2) + (c.i ** 2)),
                       (self.i * c.r - self.r * c.i) / ((c.r ** 2) + (c.i ** 2)))

    def modulus(self):
        return math.sqrt(self.r ** 2 + self.i ** 2)
