n, k = map(int, input().split())

if (n % 2 == 0 and k < int(n / 2) + 1) or (n % 2 == 1 and k < int(n / 2) + 2):
    print((k * 2) - 1)
elif n % 2 == 0 and k > int(n / 2):
    print(2 * (k - int(n / 2)))
else:
    print(2 * (k - int(n / 2) - 1))
