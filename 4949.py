s = []

while True:
  line = input()
  if line == ".":
    break
  else:
    s.append(line)

for string in s:
  stack = []
  is_balanced = True
  for char in string:
    if char in "([":  # 왼쪽 괄호인 경우 스택에 추가
      stack.append(char)
    elif char == ")":  # 오른쪽 소괄호인 경우
      if not stack or stack[-1] != "(":  # 스택이 비어있거나 짝이 맞지 않는 경우
        is_balanced = False
        break
      else:
        stack.pop()  # 짝을 이룬 괄호를 스택에서 제거
    elif char == "]":  # 오른쪽 대괄호인 경우
      if not stack or stack[-1] != "[":  # 스택이 비어있거나 짝이 맞지 않는 경우
        is_balanced = False
        break
      else:
        stack.pop()  # 짝을 이룬 괄호를 스택에서 제거
        
  if stack:  # 스택에 남아있는 경우 균형이 맞지 않음
    is_balanced = False

  if is_balanced:
    print("yes")
  else:
    print("no")
