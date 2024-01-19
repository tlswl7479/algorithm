t = int(input())
lst = []

for _ in range(t):
  k = int(input())
  n = int(input())
  count = 0
  lst = [i for i in range(1, n + 1)] 
  for i in range(k):
    for j in range(1, n):
      lst[j] += lst[j - 1]
  print(lst[n - 1])
      


