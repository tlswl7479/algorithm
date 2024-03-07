def find_special_seat(arr):
    if len(arr) == 1:
        return min(arr[0])

    n = len(arr)
    half = n // 2
    quarters = [
        [row[:half] for row in arr[:half]],
        [row[half:] for row in arr[:half]],
        [row[:half] for row in arr[half:]],
        [row[half:] for row in arr[half:]]
    ]

    candidates = []
    for quarter in quarters:
        candidates.append(find_special_seat(quarter))

    second_min = min(candidate for candidate in candidates if candidate != min(candidates))
    return second_min


N = int(input())
chairs = [list(map(int, input().split())) for _ in range(N)]
result = find_special_seat(chairs)
print(result)
