#brute force - will make it better some day

mega_list = []
for a in range(2,101):
	for b in range(2,101):
		if a**b not in mega_list:
			mega_list.append(a**b)
		#x = raw_input("")
print len(mega_list)
