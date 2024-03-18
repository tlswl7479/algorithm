n = int(input())

count = n
for _ in range(n):
  for _ in range(count):
    print("*", end='')
  print()
  count -= 1