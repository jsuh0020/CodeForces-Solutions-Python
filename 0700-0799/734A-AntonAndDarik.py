n = int(input())
s = input()

aCount = 0
dCount = 0

for i in range(n):
    if s[i] == "A":
        aCount += 1
    else:
        dCount += 1

if aCount > dCount:
    print("Anton")
elif dCount > aCount:
    print("Danik")
else:
    print("Friendship")

