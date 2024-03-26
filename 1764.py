import sys
input = sys.stdin.readline

n, m = map(int, input().split())

n_lst = []
m_lst = []

for _ in range(n):
  n_lst.append(input().rstrip())
for _ in range(m):
  m_lst.append(input().rstrip())

count = 0

nm_lst = list(set(n_lst) & set(m_lst))

nm_lst.sort()
print(len(nm_lst))
for i in nm_lst:
  print(i)
    