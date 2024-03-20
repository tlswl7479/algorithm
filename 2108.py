from collections import Counter
import sys
input = sys.stdin.readline

# 반올림 함수 - 사사오입 방식
def round_half_up(number):
    return int(number + 0.5) if number > 0 else int(number - 0.5)

# 입력 받기
N = int(input())
numbers = [int(input()) for _ in range(N)]

# 1. 산술평균 계산
mean = round_half_up(sum(numbers) / N)

# 2. 중앙값 계산
numbers.sort()
median = numbers[N // 2]

# 3. 최빈값 계산
freq = Counter(numbers)
max_freq = max(freq.values())
modes = [num for num, count in freq.items() if count == max_freq]
mode = min(modes) if len(modes) == 1 else sorted(modes)[1]

# 4. 범위 계산
range_value = max(numbers) - min(numbers)

# 5. 결과 출력
print(mean)
print(median)
print(mode)
print(range_value)