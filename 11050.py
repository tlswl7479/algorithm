n, k = map(int, input().split())
n_p = 1
k_p = 1
nk_p = 1

for i in range(1, n+1):
  n_p *= i

for j in range(1, k+1):
  k_p *= j

num = n-k

for k in range(1, num+1):
  nk_p *= k

print(n_p // (nk_p * k_p))