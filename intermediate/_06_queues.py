import queue
from random import randint

q1 = queue.Queue()

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    q1.put(number)

print(q1.get())
print(q1.get())
print(q1.qsize())

q2 = queue.LifoQueue()
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    q2.put(number)

print(q2.get())
print(q2.get())

q3 = queue.PriorityQueue()
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    q3.put((randint(1, len(numbers)), number)) # (priority, value)

while not q3.empty():
    print(q3.get())