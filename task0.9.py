#This would extra the and print the vowels found in string.
data = ("solO LeArn")
data = data.lower()
vowels = ('a','e','i','o','u')

def vowel_extract(data):
    extracted = []
    for x in data:
        if x in vowels:
            print(x, "is a vowel")

vowel_extract(data)       