import sys
import math

def read_args(argument):
	num = float(argument)
	if num < 0:
		print("ln(%n) is illegal" % num)
  elif num>0
 		print("ln(%n) = %n" % (num, math.log(num)))
	else:
    print("ln(%n) = -infinity" % num)


'''for r in sys.argv[1:]:
  read_args(r)

arguments = sys.argv[1:]
for i in range(1, len(arguments)+1):
  read_args(sys.argv[i])

i = 1
while i <= len(arguments):
  read_args(sys.argv[i])
  i += 1'''

i = 1
while 1:
	try:
		read_args(sys.argv[i])
		i += 1
	except IndexError:
		break
