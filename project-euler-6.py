i = 1
sum = 0
while (i < 101):
    j = 1
    while(j < 101):
        if(i != j):
            sum = sum + i * j
        j = j + 1
    i = i + 1
print sum

### project euler method
##n = 100
##print (((n * (n + 1) / 2) * (n * (n + 1) / 2)) - (((2 * n + 1) * (n + 1) * n) / 6))

