n, m = map(int ,input().split())
list1 = []
list2 = []
list3 = []

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

i = 0
j = 0

while 1:
  if i == n:
    list3 += list2[j:]
    break
  elif j == m :
    list3 += list1[i:]
    break
  else:
    if list1[i] <= list2[j]:
      list3.append(list1[i])
      i += 1
    else:
      list3.append(list2[j])
      j += 1

# for i in list3:
#   print(i, end=' ')

print(*list3)



