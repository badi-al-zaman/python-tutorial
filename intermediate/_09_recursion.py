import time
start = time.time()

n = 7
fact = 1
while n > 0:
    fact *= n
    n -= 1

print(fact)
end = time.time()     # Record end time
print("Execution Time for while loop:", end - start, "seconds")


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

start = time.time()
print(factorial(7))
end = time.time()     # Record end time
print("Execution Time for recursion function:", end - start, "seconds") # it takes more time than while loop because of function call overhead