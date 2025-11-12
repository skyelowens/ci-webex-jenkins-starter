<<<<<<< HEAD
def add(a: float, b: float) -> float:
    return a + b

def sub(a: float, b: float) -> float:
    return a - b

def mul(a: float, b: float) -> float:
    return a * b

def div(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Division by zero")
=======
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("Division by zero")
>>>>>>> 0a06da347926d392404c22a6705d09e93790b92a
    return a / b
