data = ("solO")
vowels = ('a','e','i','o','u','A','E','I','O','U')

def vowel_extract(vox):
    extracted = []
    for x in vox:
        if x in vowels:
            extracted.append(x)
            return (extracted)

print (vowel_extract(data))          