count = 0
n = int(input())
for i in range(n):
    temp = input()
    if temp[-2:] == "++" or temp[0:2] == "++":
        count += 1
    else:
        count -= 1

print(count)
