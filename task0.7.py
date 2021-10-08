#This will convert celcius to fahrenheit
def celcius_to_fahrenheit(c):
    return 9/5 * celsius +32
celsius = 36
fahrenheit = celcius_to_fahrenheit(celsius)
print("fahrenheit is:")
print(fahrenheit)

#This wil convert fahrenheit to celcius
def fahrenheit_to_celcius(f):
    return (fahrenheit - 32) * 5/9
fahrenheit = 96.8
celsius = fahrenheit_to_celcius(fahrenheit)
print("Celcius is:")
print (celsius)