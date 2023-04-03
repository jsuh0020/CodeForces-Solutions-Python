n = int(input())

count = 0
tramList = []

for i in range(n):
    a, b = map(int, input().split())
    tramList.append(count + b - a)
    count += b - a

print(max(tramList))
