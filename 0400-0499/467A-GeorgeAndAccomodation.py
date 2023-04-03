n = int(input())
count = 0

for i in range(n):
    people, capacity = map(int, input().split())
    if capacity - 1 > people:
        count += 1

print(count)
