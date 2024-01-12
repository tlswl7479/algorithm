import sys

stack = []
N = int(input())

for _ in range(N):
  n = sys.stdin.readline()
  if n[0] == '1':
    stack.append(int(n[2:]))
  elif n[0] == '2':
    if stack == []:
      print(-1)
    else:
      print(stack.pop())
  elif n[0] == '3':
    print(len(stack))
  elif n[0] == '4':
    if stack == []:
      print(1)
    else:
      print(0)
  elif n[0] == '5':
    if stack == []:
      print(-1)
    else:
      print(stack[-1])



