from datetime import date
from datetime import time
from datetime import datetime

def average(x):
	p = 0
	if(type(x) is list):
		for val in x:
			p += val
	p = p/len(x)
	return p
array = [23,24,25,29,30,10,5]
print average(array)

def dateTest():
	now = datetime.now()
	now = now.strftime("%A")
	return now
print dateTest()

#prints all datetime
import datetime
everything = dir(datetime)
print everything