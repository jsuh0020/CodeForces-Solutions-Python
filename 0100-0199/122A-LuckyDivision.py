def isAlmostLucky(n):
    list = [47, 74, 447, 474, 774, 477, 747]
    for i in range(len(list)):
        if n % list[i] == 0:
            return "YES"
    if n % 4 == 0 or n % 7 == 0:
        return "YES"
    else:
        return "NO"


print(isAlmostLucky(n))
