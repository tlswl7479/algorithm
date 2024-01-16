while True:
    num = input()
    if num == '0':
        break
    if num == num[::-1]:  #반전시킨 수가 원래수와 같은지 비교
        print('yes')
    else:
        print('no')
