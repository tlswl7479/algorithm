lst = []

for _ in range(5):
  lst.append(input())

for i in range(15):
  for j in range(5):
    if i > len(lst[j]) - 1:
      continue
    else:
      print(lst[j][i], end='')