#This function will convert any number into hours and minutes 
def time_conv(x):
    return (x // 60) + (x % 60) 

x = 133
hours = (x // 60)
minutes = (x % 60)
print (hours , 'hours', minutes , 'minutes')