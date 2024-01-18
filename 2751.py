import sys

n = int(input())
lst = []

for _ in range(n):
  lst.append(int(sys.stdin.readline().strip()))

lst.sort()

for i in range(len(lst)):
  print(lst[i])