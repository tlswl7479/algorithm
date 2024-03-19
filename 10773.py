import sys
input = sys.stdin.readline

k = int(input())
lst = []

for _ in range(k):
  num = int(input())
  if num == 0:
    del lst[len(lst) - 1]
  else:
    lst.append(num)

print(sum(lst))

