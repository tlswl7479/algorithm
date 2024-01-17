n, k = map(int, input().split())
num = 1

for i in range(n, -1, -1):
  if n > k:
    num *= i
  else:
    break

print(num)