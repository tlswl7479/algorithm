x = int(input())

n = 64
count = 0

while x > 0:
  if n > x:
    n = n // 2
  else:
    count += 1
    x -= n

print(count)