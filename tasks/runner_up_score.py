# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    runner_up = arr[0]
    runner = arr[0]
    for e in arr:
        if e > runner:
            runner_up = runner
            runner = e

    print(runner_up)