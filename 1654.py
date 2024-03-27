k, n = map(int, input().split())
lst = []

for _ in range(k):
  lst.append(int(input()))

s = 1
e = max(lst)
res = 0

while s <= e:
  m = (s + e) // 2
  count = 0

  for i in lst:
    count += i // m
  if count >= n:
    res = m
    s = m + 1
  else:
     e = m - 1

print(res)
