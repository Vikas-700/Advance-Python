radius=float(input("Enter radius of cylender in cm:"))
hight=float(input("Enter hight of cylender in cm:"))
volume=22/7*radius**2*hight
liter_volume=volume*0.001
print(f"Volume of cylinder in liter:{liter_volume:.2f} liter")
milk_cost=40*liter_volume
print(f"Cost of milk:{milk_cost:.2f} Rs")

