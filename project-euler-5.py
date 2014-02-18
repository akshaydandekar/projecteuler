import fractions

i = 2
product = 2
while int(i) < 21:
    if product%i != 0:
        gcd = fractions.gcd(product, i)
        product = product*i/gcd
        #print product
    i += 1
print product
