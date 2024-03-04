def d(n):
    return n + sum(map(int, str(n)))

def self_numbers():
    limit = 10000
    numbers = set(range(1, limit+1))
    generated = set()

    for i in range(1, limit+1):
        generated.add(d(i))

    self_numbers = sorted(numbers - generated)
    for num in self_numbers:
        print(num)

self_numbers()
