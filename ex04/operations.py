import sys

if len(sys.argv) != 3:
    print("wrong number of argument")
    sys.exit(0)
a = sys.argv[1]
b = sys.argv[2]
sum = 0
if a.isdigit() and b.isdigit():
    print("sum: ", (int(a) + int(b)))
    print("diff: ", (int(a) - int(b)))
    print("product: ", (int(a) * int(b)))
    if int(a) != 0 and int(b) != 0:
      print("quotient: ", (int(a) / int(b)))
      print("remainder: ", (int(a) % int(b)))
    else:
        print("ERROR")
else:
	print("i accept only the digit")