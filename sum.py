import sys
number = sys.argv[-1]
if sys.argv[-1] == sys.argv[0]:
	print "Please enter a number to find its sum"
else:
	try:
		int(number)
		number= sum(map(int, str(number)))
		print number
	except ValueError:
		print "Integer has to be entered"



