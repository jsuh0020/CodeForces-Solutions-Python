n = input()
holder = []
finalStr = ""

for i in range(0, len(n), 2):
    holder.append(n[i])

holder.sort()

for num in holder:
    finalStr += num + "+"

print(finalStr[0:-1])
