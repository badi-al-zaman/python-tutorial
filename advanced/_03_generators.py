def my_generator(n):
    """A simple generator that yields numbers from 0 to n-1."""
    for i in range(n):
        yield i**3


values = my_generator(1000)
print(next(values))  # Outputs: 0
print(next(values))
print(next(values))
print(next(values))

for value in my_generator(10):
    print(value)


def infinite_sequence():
    """A generator that yields an infinite sequence of natural numbers."""
    num = 1
    while True:
        yield num
        # Yield the current number and then multiply it by 5 for the next iteration and stop
        num *= 5


gen = infinite_sequence()
print(next(gen))  # Outputs: 0
print(next(gen))  # Outputs: 1

for i in range(10):
    print(next(gen))  # Outputs: 2, 3, ..., 11
