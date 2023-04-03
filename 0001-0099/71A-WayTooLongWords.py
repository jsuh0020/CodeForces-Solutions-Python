numWords = int(input())
for i in range(numWords):
    n = input()
    if len(n) > 10:
        print(n[0] + str(len(n) - 2) + n[-1])
    else:
        print(n)
