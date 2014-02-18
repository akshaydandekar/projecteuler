def prime(number):
    if int(number) < 1:
        return "only positive numbers"
    elif int(number) == 1:
        return "1"
    elif int(number) > 1:
        i = 1
        j = 3
        while int(i) < int(number):
            if str(isprime(j)) in "prime":
                i += 1
            else:
                pass
            j += 1
        return j - 1

def isprime(number):
    number *= 1.0 #makes it a float number
    for divisor in range(2, int((number**0.5)+1)):
        if number/divisor == int(number/divisor):
            return "not prime"
        else:
            pass
    return "prime"

print prime(10001)
