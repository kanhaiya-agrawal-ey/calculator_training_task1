def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if( b != 0):
        return a / b
    return "Division by zero."

def power(a, b):
    return a ** b;


if __name__ == "__main__":
    print("Add:", add(5, 3))
    print("Subtract:", subtract(5, 3))
    print("Multiply:", mul(5, 3))
    print("Division:", div(5, 3))