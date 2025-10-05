x = [1, 2, 3, "Hello", [0], 3]

x.insert(1, 10) # insert element by index and shift the other elements
x.append(2) # Add element to the end of the list
x.remove(3) # Remove first element matches the value (raises ValueError if not found)
x.pop(0) # Remove first element by the index
x.index("Hello") # Get The index Of The first matches element
x.pop(x.index(3))

print(x[1:4]) # Slicing the list from index 1 to index 4 (not including index 4)
print(x[-2:])  # Slicing the list to get the last two elements
for ele in x:
    print(type(ele))

x2 = [1, 22, 31, 4, 5, 61]
x2.sort() # Sort the list (only if all elements are of the same type)
x3 = x2 * 2 # Repeat the list
x4 = list(range(1, 11)) # Create a list from range

y = 2 in x # Check if element exists in the list
z = type(x[0]) is int # Check if the type of the first element is int

len(x)
max(x2)
min(x2)
sorted(x2)

# to concat two lists just type x + y and this will merge elements in one list

################################################
###################  Tuples  ###################
################################################
x5 = (1, 2, 3, "Hello", (0,),) # Tuple is a immutable list
# x3[0] = 10 # This will raise an error because tuple is immutable
temp = list(x5)
temp[0] = 10
x5 = tuple(temp) # Convert back to tuple
print(x5[1:4]) # Slicing the tuple from index 1 to index

################################################
################  dictionaries  ################
################################################
person = {"name": "Mahmoud", "age": "24", "gender": "male", True: 88}
person.items() # return a tuple of a list of tuples of key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")

person["nickname"] = "mmmm"
person.keys() # return a list of keys
person.values() # return a list of values
person.get("name") # return the value of the key (or None if the key does