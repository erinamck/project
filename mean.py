#calculate mean for input (list of numbers)
import sys

if len(sys.argv) == 1:
	print 'Error: no arguments given.'
	sys.exit()
else:
	sum =0
	for sum in sys.argv[1:]:
		sum += float(num)

	print sum / (len(sys.argv)-1)
