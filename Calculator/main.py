import art

print(art.logo)

def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
}


def calculator():
    num1 = int(input("Enter First number :: "))
    for sym in operations:
        print(sym)

    flag = True

    while flag:
        operator = input("Pick an operator below :: ")
        num2 = int(input("Enter Next number :: "))
        calculator_function = operations[operator]
        result = calculator_function(num1, num2)

        print(f"{num1} {operator} {num2} = {result}")

        if input(f"type 'y' to continue calculating with {result}, or type 'n' to restart.") == 'y':
            num1 = result
        else:
            flag = False
            calculator()


calculator()
