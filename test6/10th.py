l1=[1,2,3,4,5,6,7,8,9,10]
even_square=list(map(lambda x: x**2 ,filter(lambda z:z%2==0,l1)))
print(even_square)