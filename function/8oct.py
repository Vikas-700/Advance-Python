def Memory_transpose(x):
    size_kb=0
    for i in x:
        if i[-2:]=='kb':
            size_kb+=int(i[:-2])
        elif i[-2:]=='mb':
            size_kb+=int(i[:-2])*1024  
        else:
            print("This is invalid!",i)
    return size_kb
a=input("Enter Memory size:").lower().split('+')
print("Memory in Kb:",Memory_transpose(a))

