a = ("Solo") 
b = ("learning")

def extract_common(colist):
    comlist = []
    for x in colist:
        if x in a and b:
            comlist.append(x)
            return comlist

print (extract_common(a and b))