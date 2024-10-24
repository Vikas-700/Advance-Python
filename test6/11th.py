from functools import reduce 
numbers = [1, 2, 3, 4, 5] 
result = reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, numbers)) 
print(result) 