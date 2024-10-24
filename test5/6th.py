# Write a function register_member that accepts arbitrary keyword arguments (**kwargs) for member 
# details (e.g., name, age, membership_type). The function should print all the member details. 
# Register multiple members with different sets of information. 
def register_member(**kwargs):
    for key,values in kwargs.items():
        print(f"{key} : {values}")
register_member(name="x",age=10,membership_type="Golden")

