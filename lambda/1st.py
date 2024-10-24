sqr=lambda x:x**2
print(sqr(5))


# map
list1=[1,2,3,4,5,6]
sqr1=list(map(lambda x:x**2,list1))
print(sqr1)



# map
list2=["viaks","kumar"]
cap=list(map(lambda x: x.capitalize(),list2))
print(cap)

#map
l1=[1,2,3,4,5]
l2=[1,2,3,4,5]
add=list(map( lambda x,y:x+y,l1,l2))
print(add)

x=(1,2,3)
print(x[2])