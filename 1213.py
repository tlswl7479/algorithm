from collections import Counter

def make_palindrome(s):
    # 문자열의 알파벳 개수를 세기
    counter = Counter(s)
    
    # 홀수 번 등장하는 알파벳 개수 확인
    odd_count = sum(1 for count in counter.values() if count % 2 != 0)

    # 홀수 번 등장하는 알파벳이 2개 이상이면 팰린드롬을 만들 수 없음
    if odd_count > 1:
        return "I'm Sorry Hansoo"
    
    # 팰린드롬의 절반을 구성
    half_palindrome = ""
    odd_char = ""
    for char, count in sorted(counter.items()):
        half_palindrome += char * (count // 2)
        if count % 2 != 0:
            odd_char = char
    
    # 홀수 번 등장하는 알파벳이 있으면 중앙에 배치
    palindrome = half_palindrome + odd_char + half_palindrome[::-1]
    
    return palindrome

# 입력 받기
name = input().strip()

# 결과 출력
result = make_palindrome(name)
print(result)
