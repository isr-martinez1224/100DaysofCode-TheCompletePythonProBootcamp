import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/":divide,
}


def calculate():
    print(art.logo)

    keep_going = True
    num1 = float(input("What's the first number?: "))
    while keep_going:

        for key in operations:
            print(key)

        compute = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        answer = operations[compute](num1, num2)
        print(f"{num1} {compute} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice.lower() == "y":
            num1 = answer
        else:
            keep_going = False
            print("\n" * 20)
            calculate()

calculate()
