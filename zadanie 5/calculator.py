from complex import Complex

input_data = input("Calculator, format: real,img'operator'real,img - example: 1,1+2,2\n")

if '+' in input_data:
    left, right = input_data.split("+")
    left = Complex.convert_from_string(left)
    right = Complex.convert_from_string(right)
    Complex.print(Complex.addition(left, right))
elif '-' in input_data:
    left, right = input_data.split("-")
    left = Complex.convert_from_string(left)
    right = Complex.convert_from_string(right)
    Complex.print(Complex.subtraction(left, right))
elif '*' in input_data:
    left, right = input_data.split("*")
    left = Complex.convert_from_string(left)
    right = Complex.convert_from_string(right)
    Complex.print(Complex.multiplication(left, right))
elif '/' in input_data:
    left, right = input_data.split("/")
    left = Complex.convert_from_string(left)
    right = Complex.convert_from_string(right)
    Complex.print(Complex.division(left, right))
else:
    print("Wrong input format")




