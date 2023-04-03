n, m, a = [int(x) for x in input().split()]
if n % a == 0:
  num1 = int(n/a)
else:
  num1 = int(n/a) + 1
if m % a == 0:
  num2 = int(m/a)
else:
  num2 = int(m/a) + 1
print(num1 * num2)
