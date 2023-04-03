arr = []
for i in range(0, 5):
    temp = list(map(int, input().split()))
    if 1 in temp:
        print(abs(2-i) + abs(3 - (temp.index(1) + 1)))
        break
