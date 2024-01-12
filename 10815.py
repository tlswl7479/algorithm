n = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
result = []

m = int(input())
num_list2 = list(map(int, input().split()))

for i in num_list2:
    left = 0
    right = len(num_list) - 1
    found = False

    while left <= right:
        mid = (left + right) // 2

        if num_list[mid] == i:
            found = True
            break
        elif num_list[mid] < i:
            left = mid + 1
        else:
            right = mid - 1

    if found:
        result.append(1)
    else:
        result.append(0)
print(result)
print(*result)
