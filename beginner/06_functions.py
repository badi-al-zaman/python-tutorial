def mysum(*numbers): # * Mean Passing many arguments
    count = 0
    for num in numbers:
        count += num
    return count

print(mysum(1,2,3,4,5)) # 15

def person(name="John", age=30): # Default values
    print(f"name: {name}, age: {age}")
