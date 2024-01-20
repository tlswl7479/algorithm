n = int(input())
lst = []

for i in range(n):
  lst.append(int(input()))

num = lst[0]
lst = lst[1: len(lst)]
lst.sort(reverse=True)
count = 0

if n == 1:
  print(0)
else:
  while lst[0] >= num:
      lst[0] -= 1
      num += 1
      count += 1
      lst.sort(reverse=True)
  print(count)