import sys
input = sys.stdin.readline

lst = []

n = int(input())

for _ in range(n):
  str = input().rstrip()

  if str == "pop":
    if len(lst) == 0:
      print(-1)
    else:
      print(lst[0])
      del lst[0]
  elif str == "size":
    print(len(lst))
  elif str == "empty":
    if len(lst) == 0:
      print(1)
    else:
      print(0)
  elif str == "front":
    if len(lst) == 0:
      print(-1)
    else:
      print(lst[0])
  elif str == "back":
    if len(lst) == 0:
      print(-1)
    else:
      print(lst[-1])
  else:
    a, x = str.split()
    lst.append(int(x))
