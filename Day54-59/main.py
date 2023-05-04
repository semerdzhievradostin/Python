# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        print(f"You called a function:{function.__name__}")
        print(f"It returned: {function(*args)}")
    return wrapper

# Use the decorator 👇
@logging_decorator
def summa(a, b, c):
    return a + b + c

summa(200, 300, 214)