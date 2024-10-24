# Write a function plan_trip that takes a destination as a positional argument, and **kwargs for details 
# such as duration, budget, and season. The function should print out a trip summary. 
def plan_trip(des,**kwargs):
    print("Your ",des,"Trip.")
    for key,values in kwargs.items():
        print(f"{key} : {values}")
plan_trip("UK",Duration="120 km",Budget=20000,Season="Summer")