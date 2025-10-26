# https://www.hackerrank.com/challenges/any-or-all/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
numbers = input().split()
print(
    all([(lambda x: int(x) > 0)(num) for num in numbers])
    and any([(lambda x: x == x[::-1])(x) for x in numbers])
)
