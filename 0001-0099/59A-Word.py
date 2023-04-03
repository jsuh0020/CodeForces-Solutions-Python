s = input()

sumUpper = sum(1 for c in s if c.isupper())
sumLower = sum(1 for c in s if c.islower())

if sumUpper > sumLower:
    print(s.upper())
else:
    print(s.lower())
