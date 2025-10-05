x1 = int(input("Enter first number: "))
x2 = int(input("Enter second number: "))

if x1 > x2:
    print(f"{x1} is greater than {x2}")
    if x1 == 100:
        print(f"{x1} is equal to 100")
elif x1 < x2:
    print(f"{x1} is less than {x2}")
else:
    print(f"{x1} is equal to {x2}")