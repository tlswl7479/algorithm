# n = input()
# n_list = []
# n_str = []
# count = 1
# check = False

# for i in range(len(n)):
#   n_list.append(n[i])

# n_list.sort()

# if len(n_list) % 2 == 0:
#   for i in range(len(n_list) - 1):
#     if i == len(n_list) - 2 and n_list[i] == n_list[i + 1]:
#       n_str.append(n_list[i])
#       break
#     elif n_list[i] == n_list[i + 1]:
#       count += 1
#     else:
#       for j in range(count // 2):
#         n_str.append(n_list[i])
#       count = 1
#   for i in range(len(n_str) - 1, -1, -1):
#     n_str.append(n_str[i])

# else:
#   for i in range(len(n_list) - 1):
#     if i == len(n_list) - 2 and n_list[i] == n_list[i + 1]:
#       n_str.append(n_list[i])
#       break
#     elif i == len(n_list) - 2 and n_list[i] != n_list[i + 1]:
#       n_str.append(n_list[i])
#       n_str.append(n_list[i + 1])
#       break
#     elif n_list[i] == n_list[i + 1]:
#       count += 1
#     else:
#       if count % 2 == 0:
#         for j in range(count // 2):
#           n_str.append(n_list[i])
#       else:
#         for j in range(count // 2):
#           n_str.append(n_list[i])
#           check = True
#           a = n_list[i]
#       count = 1
#   if check == True:
#     n_str.append(a)
#   for i in range(len(n_str) - 2, -1, -1):
#     n_str.append(n_str[i])

# if n_str:
#   result = ''.join(n_str)
#   print(result)
# else:
#   print('I\'m Sorry Hansoo')


# gpt

# n = input()
# n_list = []
# n_str = []
# count = 1
# check = False

# for i in range(len(n)):
#     n_list.append(n[i])

# n_list.sort()

# if len(n_list) % 2 == 0:
#     for i in range(len(n_list) - 1):
#         if i == len(n_list) - 2 and n_list[i] == n_list[i + 1]:
#             n_str.append(n_list[i])
#             break
#         elif n_list[i] == n_list[i + 1]:
#             count += 1
#         else:
#             for j in range(count // 2):
#                 n_str.append(n_list[i])
#             count = 1
#     for i in range(len(n_str) - 1, -1, -1):
#         n_str.append(n_str[i])
# else:
#     for i in range(len(n_list) - 1):
#         if i == len(n_list) - 2 and n_list[i] == n_list[i + 1]:
#             n_str.append(n_list[i])
#             break
#         elif i == len(n_list) - 2 and n_list[i] != n_list[i + 1]:
#             n_str.append(n_list[i])
#             n_str.append(n_list[i + 1])
#             break
#         elif n_list[i] == n_list[i + 1]:
#             count += 1
#         else:
#             if count % 2 == 0:
#                 for j in range(count // 2):
#                     n_str.append(n_list[i])
#             else:
#                 for j in range(count // 2):
#                     n_str.append(n_list[i])
#                     check = True
#                     a = n_list[i]
#             count = 1
#     if check:
#         n_str.append(a)
#     for i in range(len(n_str) - 2, -1, -1):
#         n_str.append(n_str[i])

# result = ''.join(n_str)

# if result == result[::-1]:
#     print(result)
# else:
#     print('I\'m Sorry Hansoo')


from collections import Counter

def make_palindrome(name):
    # 각 알파벳의 개수를 세기
    char_count = Counter(name)
    
    # 홀수 개의 알파벳의 개수를 세기
    odd_count = 0
    odd_char = ''
    for char, count in char_count.items():
        if count % 2 == 1:
            odd_count += 1
            odd_char = char

    # 팰린드롬을 만들 수 없는 경우
    if odd_count > 1:
        return "I'm Sorry Hansoo"

    # 팰린드롬을 만들기
    palindrome = []
    for char, count in sorted(char_count.items()):
        half_count = count // 2
        palindrome.extend([char] * half_count)

    # 가운데에 홀수 개의 알파벳이 있다면 추가
    if odd_count == 1:
        palindrome.append(odd_char)

    # 오른쪽에 추가된 알파벳들을 뒤집어서 왼쪽에 추가
    palindrome += palindrome[::-1]

    return ''.join(palindrome)

# 입력 받기
name = input().strip()

# 결과 출력
result = make_palindrome(name)
print(result)
