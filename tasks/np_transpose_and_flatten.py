import numpy


n, m = list(map(int, input().split()))
arr = []

for row in range(n):
    arr.append(list(map(int, input().split())))

arr = numpy.array(arr)
print(numpy.transpose(arr))
print(arr.flatten())
