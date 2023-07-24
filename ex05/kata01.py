import sys
import string

kata = {
    'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

if len(kata) > 0:
    for x in kata:
        print (f"{x} was creat by {kata[x]}")
