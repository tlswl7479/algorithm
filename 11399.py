N = int(input())

t_list = list(map(int, input().split()))
t_list.sort()

num_list = []
count = 0

#1 2 3 3  4 
#1 3 6 9 13 
#32 
for i in range(N):
  count += t_list[i]
  num_list.append(count)

print(sum(num_list))