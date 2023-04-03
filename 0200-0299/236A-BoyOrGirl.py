n = input()
count = 0
genderList = []
for i in range(len(n)):
    if n[i] not in genderList:
        genderList.append(n[i])
        count += 1

if count % 2 == 1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")
