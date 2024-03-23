m, n = map(int, input().split())

lst = [True for _ in range(n + 1)]
lst[0] = lst[1] = False

for i in range(2, int(n**0.5) + 1):
  if lst[i]:
    for j in range(i*i, n + 1, i):
      lst[j] = False 

for i in range(max(2, m),n + 1):
  if lst[i]:
    print(i)