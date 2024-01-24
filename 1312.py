a, b, n = map(int, input().split())

x = a / b
num = x - (a // b)
num = str(num)
print(num)
print(num[n + 1])