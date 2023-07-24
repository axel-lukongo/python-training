import sys
nbr = len(sys.argv)

try:
	if nbr > 2:
		print ("bad number of arg")
	else:
		my_str = sys.argv[1]
		if my_str.isdigit():
			my_nbr = int(my_str)
			if my_nbr <= 0:
				print("i'm zero")
			elif (my_nbr % 2) > 0:
				print ("i'm odd")
			else:
				print("i'm even")
		else:
			print("it not a digit")
except:
	print ("wrong arg")