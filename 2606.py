
def recur(n, num, visit):
  global count
  visit[n] = True

  for i in num[n]:
    if not visit[i]:
      recur(i, num, visit)
      count += 1


t = int(input())
c_n = int(input())
count = 0
num = [[] for _ in range(t + 1)]
visit = [False] * (t + 1)

for i in range(c_n):
  a,b=map(int,input().split())
  num[a].append(b)
  num[b].append(a)

recur(1, num, visit)

print(count)           

      
  