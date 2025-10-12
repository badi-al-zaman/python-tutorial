# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == "__main__":
    n = int(input())  # number of students
    records = []
    for _ in range(n):  # iteration for enter each student: name, mark
        name = input()
        score = float(input())
        records.append([name, score])
    unique_records = list(set([rec[1] for rec in records]))  # get the unique marks
    unique_records.sort()  # sort marks
    result = [
        rec[0] for rec in records if rec[1] == unique_records[1]
    ]  # get students who has mark equal to the second lowest
    print("\n".join(sorted(result)))  # output results after sort them alphabetically
