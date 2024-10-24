# Write a function gym_membership that takes three keyword arguments: name, membership_type, 
# and duration. The function should return a message detailing the gym membership. Call the function 
# with keyword arguments.

def gym_membership(name, mem, duration):
    return f"{name}'s {mem} membership lasts for {duration} months."

print(gym_membership(name="John Doe", mem="Standard", duration=12))