a=int(input("Enter A"))
b=int(input("Enter B"))
c=int(input("Enter C"))
if a<b+c and b<a+c and c<a+b:
    print("This is Valid Tringle.")
else:
    print("This is Not Valid Tringle.")