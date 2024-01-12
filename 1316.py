N = int(input())
count = 0

for _ in range(N):
  str = input()
  check = True
  list = []
  for i in range(len(str)):
    if i == 0:
      list.append(str[0])
    elif list[i - 1] == str[i]:
      list.append(str[i])
    else:
      for j in list:
        if j == str[i]:
          check = False
          break
      if check == True:
        list.append(str[i])
    if check == False:
      break
  if check == True:
    count += 1
  
  
print(count)
        

# n = int(input())
# words = []

# for _ in range(n):
#     words.append(input())

# for word in words:
#     check = True
#     for j in range(len(word)-1):
#         if word[j] != word[j+1]:
#             if word[j] in word[:j]:
#                 check = False
#                 print(word)
#                 break
#     if not check:
#         n -= 1
# print(n)