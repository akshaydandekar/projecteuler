#takes out zero'd numbers from list
with_zero_list = range(10, 100)
num_list = []
for number in with_zero_list:
    if '0' not in str(number):
        num_list.append(number)

numproduct = 1
denproduct = 1

for one in num_list:
    for two in num_list:
        #we want fractions that are less than one
        if two > one:
            left_hand_side = float(one)/float(two)
            one_tuple = (int(one/10), int(one%10))
            two_tuple = (int(two/10), int(two%10))
            if one_tuple[1] == two_tuple[0]:
                right_hand_side = float(one_tuple[0])/float(two_tuple[1])
                if left_hand_side == right_hand_side:
                    #check to see that we get all four fractions
                    print one, two
                    #append the numerator and denominator to a product
                    numproduct *= one_tuple[0]
                    denproduct *= two_tuple[1]

#numproduct is smaller so we use that as a limit to reduce the fraction
for i in range(2, numproduct):
    if numproduct%i == 0 and denproduct%i == 0:
        numproduct /= i
        denproduct /= i

print denproduct
