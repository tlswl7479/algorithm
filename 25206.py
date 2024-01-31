lst = []

for _ in range(0, 20):
  a, b, c = input().split(' ')
  lst.append([b, c])

count = 0
sum = 0

for i in range(0, 20):
  if lst[i][1] == "P":
    continue
  elif lst[i][1] == "A+":
    count += float(lst[i][0]) * 4.5
    sum += float(lst[i][0])
  elif lst[i][1] == "A0":
    count += float(lst[i][0]) * 4.0
    sum += float(lst[i][0])
  elif lst[i][1] == "B+":
    count += float(lst[i][0]) * 3.5
    sum += float(lst[i][0])
  elif lst[i][1] == "B0":
    count += float(lst[i][0]) * 3.0
    sum += float(lst[i][0])
  elif lst[i][1] == "C+":
    count += float(lst[i][0]) * 2.5
    sum += float(lst[i][0])
  elif lst[i][1] == "C0":
    count += float(lst[i][0]) * 2.0
    sum += float(lst[i][0])
  elif lst[i][1] == "D+":
    count += float(lst[i][0]) * 1.5
    sum += float(lst[i][0])
  elif lst[i][1] == "D0":
    count += float(lst[i][0]) * 1.0
    sum += float(lst[i][0])
  elif lst[i][1] == "F":
    count += float(lst[i][0]) * 0.0
    sum += float(lst[i][0])

print(count / sum)
