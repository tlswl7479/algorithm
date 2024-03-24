def make_sequence(sequence):
  stack = []
  result = []
  current = 1

  for num in sequence:
    # 스택에 넣어야 할 숫자(num)이 현재 값(current)보다 작을 때까지 push
    while current <= num:
      stack.append(current)
      result.append('+')
      current += 1
  
    # 스택의 맨 위에 있는 숫자가 수열과 일치할 때까지 pop
    if stack[-1] == num:
      stack.pop()
      result.append('-')
    else:
      # 만약 수열을 만들 수 없는 경우
      print("NO")
      return
  
  # 모든 수열이 만들어졌을 경우
  for op in result:
    print(op)

# 입력 받기
n = int(input())
sequence = [int(input()) for _ in range(n)]

make_sequence(sequence)
