import sys
input = sys.stdin.readline

def calc(n, l):
  if n == 0:
    return 0
  
  l.sort()
  c = n * 0.15

  if c - int(c) >= 0.5:
    c = int(c) + 1
  else:
    c = int(c)
  
  count = 0
  total = 0
  
  for i in range(c, n - c):
    total += l[i]
    count += 1

  if (total * 10 // count) % 10 >= 5:
    return (total // count) + 1
  else:
    return total // count

# 입력값 받기
n = int(input())
lst = []

for _ in range(n):
  lst.append(int(input()))

# 난이도 계산 및 출력
print(calc(n, lst))
