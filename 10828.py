import sys  

n = int(sys.stdin.readline())
lst = []

for _ in range(n):
  com = sys.stdin.readline().split()
  if com[0] == 'pop':
    if lst:
      print(lst[len(lst) - 1])
      del(lst[len(lst) - 1])
    else:
      print(-1)
  elif com[0] == 'size':
    print(len(lst))
  elif com[0] == 'empty':
    if lst:
      print(0)
    else:
      print(1)
  elif com[0] == 'top':
    if lst:
      print(lst[len(lst) - 1])
    else:
      print(-1)
  elif com[0] == 'push':
    lst.append(com[1])