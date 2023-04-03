n = int(input())
peopleDecide = list(map(int, input().split()))
if peopleDecide.count(1) > 0:
    print("HARD")
else:
    print("EASY")
