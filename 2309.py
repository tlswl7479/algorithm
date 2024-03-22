lst = []
n1 = 0
n2 = 0
flag = False

for _ in range(9):
  num = int(input())
  lst.append(num)

lst.sort()

for i in range(8):
  if flag == True:
    break
  else:
    lst2 = lst
    for j in range(9):
      if j == i:
        continue
      else:
        if sum(lst) - lst[i] - lst[j] == 100:
          n1 = i
          n2 = j
          flag = True
          break


for i in range(9):
  if i == n1 or i == n2:
    continue
  else:
    print(lst[i])

