import sys
input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n):
  str = input().rstrip()
  if str == "pop_front":
    if len(lst) == 0:
      print(-1)
    else:
      print(lst[0])
      del(lst[0])
  elif str == "pop_back":
    if len(lst) == 0:
      print(-1)
    else:
      print(lst[-1])
      del(lst[-1])
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
    if a == "push_front":
      lst.insert(0, x)
    elif a == "push_back":
      lst.append(x)