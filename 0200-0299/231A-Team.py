numTrials = int(input())
count = 0
for i in range(numTrials):
    n = input()
    ans = n.replace(" ", "")
    if ans.count("1") > 1:
        count += 1

print(count)
