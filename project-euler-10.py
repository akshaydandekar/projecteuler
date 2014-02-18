def isprime(n):
    n *= 1.0 #makes it a float number
    if n < 2:
        return False
    if n == 2:
        return True
    if n !=2 and n%2 == 0:
        return False
    for d in range(3, int(n**0.5)+1, 2):
        if n%d == 0:
            return False
    return True

a = 2
total = 0
for a in range(2, 2000000):
    if isprime(a):
        total += a
print total
