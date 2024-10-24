def multi(args):
    total=1
    for i in args:
        total*=int(i)
    print(f"Total multiply:{total}")
input_user=input("Enter All Number in A single line(Ex. 1 2 34 4):").split()
multi(input_user)