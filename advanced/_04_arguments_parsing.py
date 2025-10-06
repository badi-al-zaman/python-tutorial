def test(*args, **kwargs):
    print("Positional arguments:", args)  # Print positional arguments. args is a tuple
    print(
        "Keyword arguments:", kwargs
    )  # Print keyword arguments kwargs is a dictionary
    print(args[0])
    print(args[1])
    print(args[2])
    print(kwargs["name"])
    print(kwargs["age"])


test(1, 2, 3, name="Alice", age=30)


import sys

print(sys.argv)  # List of command-line arguments passed to the script

import getopt

filename = "test.txt"
message = "Hello, World!"

options, arguments = getopt.getopt(
    sys.argv[1:], "f:m:", ["filename", "message"]
)  # Parse command-line options and arguments

for opt, arg in options:
    if opt in ("-f", "--filename"):
        filename = arg
    elif opt in ("-m", "--message"):
        message = arg

with open(filename, "w", encoding="utf-8") as file:
    file.write(message)
