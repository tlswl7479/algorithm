import sys
input = sys.stdin.readline

m = int(input())
oper = []
s = []

for _ in range(m):
  o = input().rstrip()
  if o == "empty":
    s = []
  elif o == "all":
    s = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
  else:
    a, b = o.split()
    if a == "add":
      if b not in s:
        s.append(b)
    elif a == "remove":
      if b in s:
        s.remove(b)
    elif a == "check":
      if b in s:
        print(1)
      else:
        print(0)
    elif a == "toggle":
      if b in s:
        s.remove(b)
      else:
        s.append(b)


