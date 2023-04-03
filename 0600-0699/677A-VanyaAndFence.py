n, h = map(int, input().split())
heights = list(map(int, input().split()))

count = 0

for i in range(n):
    if heights[i] > h:
        count += 2
    else:
        count += 1

print(count)
