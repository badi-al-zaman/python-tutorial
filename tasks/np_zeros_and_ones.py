# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem?isFullScreen=true
import numpy as np

dim = tuple(map(int, input().split()))

print(np.zeros(shape=dim, dtype=int))
print(np.ones(shape=dim, dtype=int))

# [
#     [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
#     [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
#     [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
# ]
