for i in range(10):
    for j in range(1):
        if i==0:
            print(" "*11,"*")
        if i==7:
            print(" "*3,"* "*9)
        print(" "*(10-i),"*"," "*(i*2),"*",end=" ")
    print()