def conv(c):
    return 9/5 * celsius +32
celsius = 36
fahrenheit = conv(celsius)
print(fahrenheit)

def conv(f):
    return (fahrenheit - 32) * 5/9
fahrenheit = 96.8
celsius = conv(fahrenheit)
print (celsius)