n = int(input())
num = 1
count = 0

for i in range(1, n + 1):
  num *= i

num = str(num)

for i in range(len(num) - 1, -1, -1):
  if num[i] == '0':
    count += 1
  else:
    break
print(count)