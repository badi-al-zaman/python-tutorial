import time


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        print("Before the function call.")
        returned_value = func(*args, **kwargs)
        print("After the function call.")
        return returned_value

    return wrapper


def hello_world():
    print("Hello, world!")


@my_decorator
def hello_world_2():
    print("Hello, world!")


@my_decorator
def hello_world_3(person):
    return f"Hello, {person}!"


my_decorator(hello_world)()  # Manually applying the decorator
hello_world_2()  # Using the @ syntax

print(hello_world_3("mike"))  # Using the @ syntax with arguments


# Example of a decorator that logs function calls to a file
def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open("log_file.txt", "a+", encoding="utf-8") as f:
            fname = function.__name__
            result = f"{fname} returned value: {value}\n"
            print(result)
            f.write(result)
        return result

    return wrapper


@logged
def add(x, y):
    return x + y


print(add(10, 20))


# Example of a decorator that measures execution time
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(
            f"Function {func.__name__} took {end_time - start_time:.4f} seconds to execute."
        )
        return result

    return wrapper


@timer
def factorial(x):
    """Return x!"""
    result = 1
    for i in range(1, x):
        result *= i
    return result


print(factorial(1000))
