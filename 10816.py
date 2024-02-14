import sys
from collections import defaultdict

n = int(sys.stdin.readline())
n_lst = list(map(int, sys.stdin.readline().split()))

# 숫자 카드의 개수를 세는 딕셔너리 생성
card_count = defaultdict(int)
for num in n_lst:
    card_count[num] += 1

m = int(sys.stdin.readline())
m_lst = list(map(int, sys.stdin.readline().split()))

result = []
for num in m_lst:
    result.append(card_count[num])

print(' '.join(map(str, result)))
