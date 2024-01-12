l = int(input())
r = 31
string = input()

result = 0
 
for i in range(l):
    num = ord(string[i]) - 96
    result += num * (r ** i)
 
print(result % 1234567891)