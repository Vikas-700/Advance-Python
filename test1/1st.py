x=int(input("Enter first Age:"))
y=int(input("Enter Second Age:"))
z=int(input("Enter third Age:"))
if x>y:
    if x>z:
        print("oldest Age :",x)
    else:
        print("Oldest Age:",z)
if y>z:
    if y>x:
        print("Oldest Age:",y)
    else:
        print("Oldest Age:",x)
else:
    print("Oldest Age:",z)
