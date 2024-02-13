import sys

# 이분 탐색 함수 정의
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

n_lst = []
m_lst = []

n = int(sys.stdin.readline())
n_cards = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
m_cards = list(map(int, sys.stdin.readline().split()))

n_cards.sort()  # 상근이가 가지고 있는 숫자 카드를 정렬합니다.

# 결과 계산
result = []
for card in m_cards:
    if binary_search(n_cards, card):  # 이분 탐색을 사용하여 해당하는 숫자가 있는지 확인합니다.
        count = n_cards.count(card)  # 상근이가 가지고 있는 카드에 해당 숫자가 있을 경우 개수를 세어 결과에 추가
        result.append(str(count))
    else:
        result.append('0')  # 상근이가 가지고 있는 카드에 해당 숫자가 없을 경우 0을 결과에 추가합니다.

# 결과 출력
print(' '.join(result))
