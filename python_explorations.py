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

import calendar
calendarOptions = dir(calendar)
webCal = calendar.TextCalendar(calendar.SUNDAY)
webCalOut = webCal.formatmonth(2015,1)
print webCalOut

statement = "Here are all of the calendar Classes"
print statement
print calendarOptions

for m in range(1,13):
	cal = calendar.monthcalendar(2015, m)
	weekone = cal[0]
	weektwo = cal[1]

	if weekone[calendar.FRIDAY] != 0:
		meetday = weekone[calendar.FRIDAY]
	else:
		meetday = weektwo[calendar.FRIDAY]
	print "%15s %2d" % (calendar.month_name[m], meetday)