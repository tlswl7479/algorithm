def solution(height):
    need = 0
    unnecessary = 0

    for i in range(257):
        current_nums, diff = height_nums[i], i-height
        if current_nums == 0:
            continue
        if diff < 0:
            need += (-diff) * current_nums
        else:
            unnecessary += diff * current_nums
    
    if (unnecessary+ B) >= need:
        time = need + unnecessary * 2
        return time
    else:
        return sys.maxsize

import sys
N, M, B = map(int, sys.stdin.readline().split())
height_nums = [0]* 257
for i in range(N):
    for j in list(map(int,input().split())):
        height_nums[j] += 1 
min_times = sys.maxsize -1
answer_height = 0

for height in range(257):
    time_value = solution(height)
    if time_value <= min_times:
        min_times = time_value
        answer_height = height
print(min_times, answer_height)