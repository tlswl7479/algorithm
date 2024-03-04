n = int(input())
f = True

while f:
    if n == 1:
        f = False
        break
    for i in range(2, n+1):
        if n % i == 0:
            print(i)
            n //= i
            break
