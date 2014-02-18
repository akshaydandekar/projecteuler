def fibb_r(n):
	# recursive method - time consuming
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return fibb(n-1) + fibb(n-2)

def fibb_n(n):
	# normal method
	i = 0
	j = 1
	ans = 0
	count = 0
	while count < n:
		ans += (i + j)
		i, j = j, i+j
		count += 1
	return j
	

i = 0
sumofterms = 0
while True:
	i += 1
	if fibb_n(i)%2 == 0:
		sumofterms += fibb_n(i)
	if fibb_n(i) > 4000000:
		break

print sumofterms
