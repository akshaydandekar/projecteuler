a = 999
largest_palindrome = 0
while a > 0:
    b = a # instead of b = 999, because that reduces the number of calculations
    while b > 0:
        product = a * b
        first_half = str(product)[:3]
        second_half = str(product)[3:]
        reverse_second_half = second_half[::-1]
        if first_half == reverse_second_half:
            if int(product) > int(largest_palindrome):
                largest_palindrome = product
        b -= 1
    a -= 1
print largest_palindrome

# if the programmer knows that a or b must be a factor of 11, this is even simpler
