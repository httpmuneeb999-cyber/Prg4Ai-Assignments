

                                           #question no 4
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def modulus(a, b):
    return a % b

again = "yes"

while again == "yes":
    num1 = float(input("enter the first number : "))
    num2 = float(input("enter the second number : "))
    operation = input("enter the operation +, -, *, /, % : ")

    if operation == "+":
        result = addition(num1, num2)
    elif operation == "-":
        result = subtraction(num1, num2)
    elif operation == "*":
        result = multiplication(num1, num2)
    elif operation == "/":
        result = division(num1, num2)
    elif operation == "%":
        result = modulus(num1, num2)
    else:
        result = "invalid operation"

    print("result", result)

    again = input("Do you want to perform another calculation ? yes to continue and no to exit thanku buddy g : ")