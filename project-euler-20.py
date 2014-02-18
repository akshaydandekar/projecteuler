from math import factorial

n = factorial(100)
print n
total = 0
for c in str(n):
    total += int(c)
print total
