x = 0
print("while loop example:")
while x < 10:
    if x % 2 == 0:
        print(f"{x} is even")
        continue
    if x == 7:
        print("x is 7, breaking the loop")
        break
    x+=1
    print(x)

print("for loop example:")
for i in range(1, 11):
    print(i)
    pass



