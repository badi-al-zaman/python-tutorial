# https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true


def get_marks_avg(marks):
    """_summary_
    Args:
        marks (lits): students' marks

    Returns:
        float: the marks' avg
    """
    marks_sum = 0
    for mark in marks:
        marks_sum += mark
    return marks_sum / len(marks)


if __name__ == "__main__":
    n = int(input())  # number of students
    student_marks = {}  # dictionary to save students as name: [marks]
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()  # student name to calculate his marks avg
    print(f"{get_marks_avg(student_marks[query_name]):.2f}")
