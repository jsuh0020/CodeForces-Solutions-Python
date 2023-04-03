n, k = [int(x) for x in input().split()]
scores = list(map(int, input().split()))

count = 0

threshold = scores[k - 1]

for num in scores:
    if num >= threshold and num > 0:
        count += 1
    else:
        break
print(count)
