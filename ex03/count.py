import sys
import string

def my_count(s):
	try:
		if s.isdigit() or len(s) == 0:
			print("wrong argument")
			return
		lower_case = 0
		uppercase = 0
		space = s.count(' ')
		ponctuation = 0
		for c in s:
			if c.islower():
				lower_case += 1
			elif c.isupper():
				uppercase += 1
			elif c in string.punctuation:
				ponctuation += 1
		print("this text containe: ",len(s))
		print("upper: ", uppercase, "\nlower: ",lower_case, "\nspace: ", space, "\nponctuation: ", ponctuation)
	except:
		print ("ERROR")
my_count("je suis la RER bloquer !!!")