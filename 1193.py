x = int(input())
line = 1

while x > line:
  x -= line
  line += 1

if line % 2 == 0:
  r = x
  c = line - x + 1
elif line % 2 == 1:
  r = line - x + 1
  c = x

print(f'{r}/{c}')
