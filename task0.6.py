mainlist = (12,5,8)
def max_out(out):
    ilist = []
    for x in out:
        if x >= 0:
            ilist.append(x)
            return ilist
print(max_out(mainlist))