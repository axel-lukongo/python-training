import sys
import string
kata = (123278,312,2332)

if type(kata) == int:
    print ("the value is {}".format(kata))
elif type(kata) == tuple:
    i = 1
    s = str(kata[0])
    while i < len(kata):
        s += ", " + str(kata[i])
        i = i + 1
    # print ("the {} numbers are: {}".format(len(kata), s)) methode 1
    print (f"the {len(kata)} numbers are: {s}") # methode 2
