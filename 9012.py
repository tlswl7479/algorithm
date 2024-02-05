t = int(input())

for _ in range(t):
    count = 0
    chk = True
    s = input()
    
    for i in range(len(s)):
        if s[i] == '(':
            count += 1
        elif s[i] == ')':
            count -= 1

        if count < 0:
            chk = False
            break

    if chk and count == 0:
        print('YES')
    else:
        print('NO')
