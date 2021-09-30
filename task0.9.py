vow_ex = ("Umuzi welcomes us")
vowels =['a','e','i','o','u','A','E','I','O','U']
list1=[]
for x in vow_ex:
    if (x in vowels and x not in list1):
        list1.append(x)  
print("Vowels present in given statement : ",list1)