def divide():
    try:
        x = int(input("First Number: "))
        y = int(input("Second Number: "))
        print(x / y)
    except ValueError:
        print("Please Enter A Valid Number.")
        print("starting over...")
        divide()
    except ZeroDivisionError:
        print("Can't Divide By Zero")
        print("starting over...")
        divide()
    finally:
        print("Done.")

divide()

def test():
    if True:
        raise Exception("Test")
        # raise ValueError("Test")

# test()

x = 100
y = 20

# Return Error & Finish The Script If The Assertion Is Not True
# assert (x < y)
