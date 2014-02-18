from math import log

n = 1
total_product = 0
while int(n) < 1001:
    total_product = total_product + n**n
    n += 1
print str(total_product)[-10:]
