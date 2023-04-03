n = int(input())
vectorList = []
sum1 = 0
sum2 = 0
sum3 = 0
for i in range(n):
    vectors = list(map(int, input().split()))
    vectorList.append(vectors)

for i in range(n):
    sum1 += vectorList[i][0]
    sum2 += vectorList[i][1]
    sum3 += vectorList[i][2]

if sum1 == 0 and sum2 == 0 and sum3 == 0:
    print("YES")
else:
    print("NO")
