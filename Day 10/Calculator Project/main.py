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
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

# result = operations["*"](n1 = 4, n2 = 8)
#
# print(result)

def calculator():
    print(art.logo)
    should_accumulate = True
    first_number = float(input("What's the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_type = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))
        result = operations[operation_type](n1 = first_number, n2 = second_number)
        print(f"{first_number} {operation_type} {second_number} = {result}")
        choice = input(f"Type 'y' to continue calculating with {result}, "
                              f"or type 'n' to start a new calculation: " ).lower()
        if choice == "y":
            first_number = result
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()





