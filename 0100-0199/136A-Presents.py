n = int(input())
indexes = list(map(int, input().split()))
str = ""
for i in range(1, n + 1):
    print(indexes.index(i) + 1, end=' ')
