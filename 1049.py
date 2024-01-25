n, m = map(int, input().split())
lst1 = []
lst2 = []

for _ in range(m):
  a, b = map(int, input().split())
  lst1.append(a)
  lst2.append(b)

lst1.sort()
lst2.sort()
  
if n // 6 != 0:
    count = (n // 6) * lst1[0]
    x = n
    n = n % 6
    if n != 0:
      if count + lst1[0] < count + (n * lst2[0]):
        print(count + lst1[0])
      elif count > x * lst2[0]:
        print(x * lst2[0])
      else:  
        print(count + (n * lst2[0]))
    else:
      if count > x * lst2[0]:
        print(x * lst2[0])
      else:
        print(count)
else:
    if lst1[0] <= lst2[0] * n:
       print(lst1[0])
    else:
      count = n * lst2[0]
      print(count)