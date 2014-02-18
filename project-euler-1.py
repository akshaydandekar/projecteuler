n=0
total=0
while n < 1000:
    i = n%3
    j = n%5
    if ((i == 0 or j == 0) and (n != 0)):
        total = total + n
    n += 1
print total

