a = [1, 2, 12, 4]
b = [2, 4, 2, 8]

dot_product = 0
if len(a) == len(b):
    for i in range(len(a)):
        dot_product += a[i] * b[i]
    print(dot_product)
else:
    print("Vectors are of different length!")
