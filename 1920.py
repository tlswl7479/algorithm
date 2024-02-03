n = int(input())
n_lst = list(map(int, input().split()))
  
m = int(input())
m_lst = list(map(int, input().split()))

n_lst.sort()

for i in m_lst:
  min = 0
  max = n - 1
  chk = False

  while min <= max:
    mid = (min + max) // 2
    if i == n_lst[mid]:
      chk = True
      print(1)
      break
    elif i > n_lst[mid]:
      min = mid + 1
    else:
      max = mid - 1
  if not chk:
    print(0)
    

