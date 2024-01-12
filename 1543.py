from collections import deque

# 두 문자열 입력 받기
str1 = input()
str2 = input()

# 중복 없이 최대 몇 번 등장하는지를 카운트할 변수 초기화
ans = 0

# 문자열을 deque로 변환
str1_deque = deque(str1)

# 검색하려는 단어(str2)가 문서(str1) 안에 중복 없이 몇 번 등장하는지 계산
while len(str1_deque) >= len(str2):
    # 현재 deque 내 문자열이 str2와 같은지 확인
    if ''.join(list(str1_deque)[:len(str2)]) == str2:
        ans += 1
        # str2의 길이만큼 deque에서 문자 제거
        for _ in range(len(str2)):
            str1_deque.popleft()
    else:
        # 일치하지 않는 경우 첫 번째 문자 제거
        str1_deque.popleft()

print(ans)



