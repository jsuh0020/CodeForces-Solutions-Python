n, t = map(int, input().split())
genderList = list(input())
indexList = []
for i in range(t):
    for j in range(1, n):
        if genderList[j-1] == "B" and genderList[j] == "G" and j-1 not in indexList:
            genderList[j-1] = "G"
            genderList[j] = "B"
            indexList.append(j)
    indexList.clear()
print("".join(genderList))
