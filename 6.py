import sys , math

try:
  infilename = sys.argv[1]
	outfilename = sys.argv [2]
except:
	print "Usage:", sys.argv[0], "infile  outfile"
	sys.exit (1)
  
ifile = open(infilename, ’r’)
ofile = open(outfilename , 'w')

for line in ifile:
  args = line.split()
  sum=0
  for i in range(len(args)):
    sum+=float(args[i])
		ofile.write('%12.6f' % float(args[i]))
	avg = sum/len(args)
	ofile.write('%12.6f\n' % avg)

ifile.close()
ofile.close()
