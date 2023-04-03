n = int(input())
coinValues = list(map(int, input().split()))
coinValues.sort(reverse=True)
count = 0
total = 0
totalLeft = 0
for i in range(len(coinValues)):
    total += coinValues[i]
    totalLeft = 0
    for j in range(i + 1, len(coinValues)):
        totalLeft += coinValues[j]
    if total > totalLeft:
        count += 1
        break
    else:
        count += 1
print(count)
