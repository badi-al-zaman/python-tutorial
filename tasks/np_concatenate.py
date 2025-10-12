import numpy

n, m, p = list(map(int, input().split()))
arr1 = []
arr2 = []
for row in range(n):
    arr1.append(list(map(int, input().split())))

for row in range(m):
    arr2.append(list(map(int, input().split())))

print(numpy.concatenate((arr1, arr2), axis=0))
