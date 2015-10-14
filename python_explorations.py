def average(x):
	p = 0
	if(type(x) is list):
		for val in x:
			p += val
	p = p/len(x)
	return p
array = [23,24,25,29,30,10,5]
print average(array)


