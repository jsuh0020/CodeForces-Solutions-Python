n = input().lower()
finalStr = ""
for i in range(len(n)):
    if n[i] not in ('a', 'e', 'i', 'o', 'u', 'y'):
        finalStr += "." + n[i]
print(finalStr)


