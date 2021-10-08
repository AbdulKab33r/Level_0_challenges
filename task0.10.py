#This program will print the common letters in two strings.
a = ("Solo") 
b = ("learning")

def extract_common(colist):
    comlist = []
    for x in colist:
        if x in a and b:
            comlist.append(x)
            return comlist

print ( "Common Letters:", extract_common(a and b))