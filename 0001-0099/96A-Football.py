s = input()
count = 0
boolVar = False
for i in range(7, len(s) + 1):
    if s[i - 7:i] == "0000000" or s[i - 7:i] == "1111111":
        print("YES")
        boolVar = True
        break
if not boolVar:
    print("NO")
