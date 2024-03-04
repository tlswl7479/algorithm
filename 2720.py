t = int(input())

for _ in range(t):
  m = int(input())

  print(m // 25, end=" ")
  m = m % 25
  print(m // 10, end=" ")
  m = m % 10
  print(m // 5, end=" ")
  m = m % 5
  print(m // 1)