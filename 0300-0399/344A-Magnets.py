n = int(input())
magnetComp = []
numGroups = 0

for i in range(n):
    magnetComp.append(input())
for i in range(1, n):
    if magnetComp[i] == "01" and magnetComp[i - 1] == "10":
        numGroups += 1
    if magnetComp[i] == "10" and magnetComp[i - 1] == "01":
        numGroups += 1

print(numGroups + 1)
