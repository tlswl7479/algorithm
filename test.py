lst = [(1, 'b'), (1, 'a'), (2, 'x'), (3, 'y')]
lst.sort(key = lambda x : (x[0], x[1])) 
print(lst)