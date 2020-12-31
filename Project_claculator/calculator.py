def add(n1, n2):
    a = n1 + n2
    return a


def subtract(n1, n2):
    s = n1 - n2
    return s


def multiply(n1, n2):
    m = n1 * n2
    return m


def divide(n1, n2):
    d = n1 / n2
    return d


operations = {'-': subtract,
              '+': add,
              '*': multiply,
              '/': divide
              }

def calculator():
    n1 = float(input("Enter the first number : "))

    for keys in operations:
      print(keys)

    letsgo = True
    while letsgo:
        symbols = input("pick one of the operator :")
        n2 = float(input("What is the next number : "))

        if symbols == '-':
           answer = subtract(n1, n2)

        elif symbols == '+':
           answer = add(n1, n2)
        elif symbols == '*':
           answer = multiply(n1, n2)
        elif symbols == '/':
           answer = divide(n1, n2)
        print(f"{n1} {symbols} {n2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            n1 = answer
        else:
            letsgo = False

            calculator()
calculator()