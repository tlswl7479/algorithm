def recur(h, count):
  global r
  visit[h] = True

  if h == p2:
    r = count
    return
  
  for i in lis[h]:
    if not visit[i]:
      recur(i ,count+1)



n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
lis = [[] for _ in range(n + 1)]
count = 0
r = -1
visit = [False] * (n + 1)

for i in range(m):
  a, b = map(int, input().split())
  lis[a].append(b)
  lis[b].append(a)

recur(p1, 0)
print(r)
