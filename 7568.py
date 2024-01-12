# N = int(input())
# rank = N

# list = [0 for _ in range(N)]
# X = [0 for _ in range(N)]
# Y = [0 for _ in range(N)]

# for i in range(N):
#   x, y = map(int, input().split())
#   X[i] = x
#   Y[i] = y

# for i in range(N):
#   for j in range(N):
#     if X[i] > X[j] and Y[i] > Y[j]:
#       rank -= 1
#     elif X[i] < X[j] and Y[i] < Y[j]:
#       continue
#     elif X[i] < X[j] or Y[i] < Y[j]:
#       rank -= 1
#     elif (X[i] == X[j] and Y[i] < Y[j]) or (X[i] < X[j] and Y[i] == Y[j]):
#       rank -= 1
#     elif (X[i] > X[j] and Y[i] == Y[j]) or (X[i] == X[j] and Y[i] > Y[j]):
#       rank -= 1
#     elif i != j and X[i] == X[j] and Y[i] == Y[j]:
#       rank -= 1

#   list[i] = rank
#   rank = N
      
# for i in list:
#   print(i , end = " ")


N = int(input())
people = []

for i in range(N):
    x, y = map(int, input().split())
    people.append((x, y))

ranks = []
for i in range(N):
    rank = 1
    for j in range(N):
        if i == j:
            continue
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank += 1
    ranks.append(rank)

for rank in ranks:
    print(rank, end=" ")
