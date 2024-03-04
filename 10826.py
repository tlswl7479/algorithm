n = int(input())
lst = []

for i in range(n + 1):
  if i == 0:
    lst.append(0)
  elif i == 1:
    lst.append(1)
  else:
    lst.append(lst[i - 1] + lst[i - 2])

print(lst[-1])