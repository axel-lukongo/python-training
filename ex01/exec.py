import sys


nbr_arg = len(sys.argv)
sep = " "
print (sep.join(sys.argv[1:])[::-1].swapcase())
