# Write the functions for arithmatic operations here
# These functions should cover Task 2

# -------------------------------------
# Write the select_op(choice) function here
# This function should cover Task 1 (Section 2) and Task 3
def Sum(a, b):
    print(f"{a} + {b} = {a + b}")


def sub(a, b):
    print(f"{a} - {b} = {a - b}")


def multi(a, b):
    print(f"{a} * {b} = {a * b}")


def div(a, b):
    if b != 0:
        print(f"{a} / {b} = {a / b}")
    else:
        print(f"{a} / {b} = None")


def power(a, b):
    print(f"{a} ^ {b} = {a ** b}")


def mod(a, b):
    print(f"{a} % {b} = {a / b}")


def select_op(Choice):
    if Choice == "+":
        a = 0
        b = 0
        num1 = input("Enter first number : ")
        try:
            a = int(num1)
            print(a)
        except:
            print("Not a valid number,please enter again")
        num2 = input("Enter second number : ")
        try:
            b = int(num2)
            print(b)
        except:
            print("Not a valid number,please enter again")
        Sum(a, b)
    elif Choice == "-":
        a = 0
        b = 0
        num1 = input("Enter first number : ")
        try:
            a = int(num1)
            print(a)
        except:
            print("Not a valid number,please enter again")
        num2 = input("Enter second number : ")
        try:
            b = int(num2)
            print(b)
        except:
            print("Not a valid number,please enter again")
        sub(a, b)
    elif Choice == "*":
        a = 0
        b = 0
        num1 = input("Enter first number : ")
        try:
            a = int(num1)
            print(a)
        except:
            print("Not a valid number,please enter again")
        num2 = input("Enter second number : ")
        try:
            b = int(num2)
            print(b)
        except:
            print("Not a valid number,please enter again")
        multi(a, b)
    elif Choice == "/":
        a = 0
        b = 0
        num1 = input("Enter first number : ")
        try:
            a = int(num1)
            print(a)
        except:
            print("Not a valid number,please enter again")
        num2 = input("Enter second number : ")
        try:
            b = int(num2)
            print(b)
        except:
            print("Not a valid number,please enter again")
        div(a, b)
    elif Choice == "^":
        a = 0
        b = 0
        num1 = input("Enter first number : ")
        try:
            a = int(num1)
            print(a)
        except:
            print("Not a valid number,please enter again")
        num2 = input("Enter second number : ")
        try:
            b = int(num2)
            print(b)
        except:
            print("Not a valid number,please enter again")
        power(a, b)
    elif Choice == "%":
        a = 0
        b = 0
        num1 = input("Enter first number : ")
        try:
            a = int(num1)
            print(a)
        except:
            print("Not a valid number,please enter again")
        num2 = input("Enter second number : ")
        try:
            b = int(num2)
            print(b)
        except:
            print("Not a valid number,please enter again")
        mod(a, b)
    elif Choice == "#":
        return -1
    elif Choice == "$":
        return ""
    else:
        return "Unrecognized operation"


# End the select_op(choice) function here
# -------------------------------------
# This is the main loop. It covers Task 1 (Section 1)
# YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")

    # take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice)
    if select_op(choice) == -1:
        # program ends here
        print("Done. Terminating")
        exit()
