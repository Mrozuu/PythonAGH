set_code = input("Enter the code: ")
while not set_code.isdigit():
    set_code = input("Wrong code. The code can only contain numbers. Enter again: ")
print("Code set successfully")

is_correct = False
given_code = input("Lock closed. Enter the code to open: ")
while not is_correct:
    while not given_code.isdigit():
        given_code = input("Wrong code. The code can only contain numbers. Enter again: ")
    if given_code == set_code:
        is_correct = True
    else:
        given_code = input("Wrong code. Enter again: ")
print("Lock opened!")
