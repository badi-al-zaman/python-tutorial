s = input()
lower_letters = "".join(sorted([l for l in s if l.islower()]))
upper_letters = "".join(sorted([l for l in s if l.isupper()]))
digits = [int(l) for l in s if l.isdigit()]
odd = "".join(sorted([str(d) for d in digits if d % 2 != 0]))
even = "".join(sorted([str(d) for d in digits if d % 2 == 0]))
print(lower_letters + upper_letters + odd + even)
