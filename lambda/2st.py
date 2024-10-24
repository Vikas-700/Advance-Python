# map
# Ex.1
l1=[12,34,56,78,23]
result=list(map(lambda x: x**3,l1))
print("x**3 using Map function: ",result)
# Ex.2
l1=[1,2,3,4,5,6]
l2=[1,2,3,4,5,6]
result=list(map(lambda x,y:x*y,l1,l2))
print("l1*l2=",result)
# Ex.3
x=(7,6,5,4)
y=(1,2,3,4)
result=tuple(map(lambda x,y:x//y,x,y))
print("x/y:-",result)


#filter
#Ex.1
result=list(filter(lambda x:x%2==0,l1))
print(result)

#Ex.2
x=[1,2,3,4,5,6,7,8,9,10,35,70]
result=list(filter(lambda x:x%5==0 and x%7==0,x))
print(result)

#Ex.3
x=["Ram","Raj","Vikas","Akash","Rahul"]
result=list(filter(lambda x: x.startswith('R'),x))
print(result)



#reduce
#Ex.1
from functools import reduce 

def calculate_fac(x):
    z=[]
    for i in range(1,x+1):
        z.append(i)
    fac=reduce(lambda x,y:x*y,z)
    return fac
x=int(input("Enter A number:"))
print("Factorial is:",calculate_fac(x))


