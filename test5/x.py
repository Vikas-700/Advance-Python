def add(x,y):
    print(x+y)
list=[1,2,3,4,5,add,8]
list[-2](list[0],list[1])

check=lambda x: 'a' in x
print(check("Vikas"))


odd_even=lambda x: "Even" if x%2==0 else "Odd"
print(odd_even(34))


