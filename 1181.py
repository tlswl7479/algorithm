import sys

n = int(input())
str_list = []

for _ in range(n):
  str_list.append(sys.stdin.readline().strip()) 

str_list = set(str_list)
str_list = list(str_list)
str_list.sort()
str_list.sort(key = len)

print(*str_list)