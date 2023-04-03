n = int(input())
usedNums = []
bool = True
i = 0
while (bool):
    n = n + 1
    if len(set(str(n))) == len(str(n)):
        bool = False
print(n)
