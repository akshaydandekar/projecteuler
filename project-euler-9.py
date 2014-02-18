a = 1
while int(a) < 500:
    b = 0
    while int(b) < 500:
        if int(b) != int(a):
            c = 1000 - a - b
            lhs = a**2 + b**2
            rhs = c**2
            if lhs == rhs:
                print a
                print b
                print c
                print a*b*c
                exit()
        b += 1
    a += 1


