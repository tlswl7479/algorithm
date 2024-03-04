c = int(input())

for _ in range(c):
  lst = list(map(float, input().split()))
  res = sum(lst[1:]) / lst[0]
  count = 0
  for i in range(1, len(lst)):
    if lst[i] > res:
      count += 1
  ans = (count / (len(lst) - 1)) * 100
  print('%0.3f' % ans + '%')
