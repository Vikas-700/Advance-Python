# positinal Argument
def nar(name,age):
    print(f"Name:{name} Age :{age}")
nar("Vikas",20)

# keybord Argument
def nar(name,age):
    print(f"Name:{name} Age :{age}")
nar(age=20,name="Vikas")

#Overrides The Default argument
def greet(name="XYZ"):
    print(f"Hello sir you are {name}")
greet("")



# *args (Non Keyword Argument)
def sum_number(*args):
    total=sum(args)
    print(f"Sum: total")
sum_number(1,2,3,4,5)


#test
def multi(args):
    total=1
    for i in args:
        total*=int(i)
    print(f"Total multiply:{total}")
input_user=input("Enter All Number in A single line(Ex. 1 2 34 4):").split()
multi(input_user)


# kwargs (Keyword Argoments)
def state(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
state(Punjab="Chandighar",Up="Lucknow",Rajshthan="Jaypur", jhammu_Kashmeer="Shree nagar",uk="Halduani") 