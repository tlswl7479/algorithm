m, n = map(int, input().split())
p = []
c = []

for _ in range(m):
    p.append(input())

for a in range(m-7):
  for b in range(n-7):
      W = 0
      B = 0
      for i in range(a, a+8):
        for j in range(b, b+8):
            if (i+j) % 2 == 0:
              if p[i][j] != 'W':
                  W += 1
              if p[i][j] != 'B':
                  B += 1
            else:
              if p[i][j] != 'B':
                  W += 1
              if p[i][j] != 'W':
                  B += 1
      c.append(min(W, B))
print(min(c))