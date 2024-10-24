# Create a function donation_total that accepts a positional-only argument donation_amount, a 
# keyword-only argument service_fee_percent, and returns the total amount including the service fee.
def donation_total(amount,S_fee):
    fee=(amount*S_fee)/100
    return fee+amount
print(donation_total(30000,S_fee=7))


# --- End of 1st.py ---

# Write a function order_summary that takes an order_id as a positional argument, arbitrary *items, 
# and keyword arguments for shipping_cost and tax_percent. The function should return the total cost 
# of the order. 
def order_summary(id,s_cost,tax,**items):
    total=0
    for i in items.values():
        total+=i
    tax=(total*tax)/100
    total+=s_cost
    return id,tax+total
print(order_summary("1",shirt=700,jeens=1600,shoes=20000,s_cost=40,tax=18,food=1200))

    

# --- End of 2st.py ---

# Write a function plan_trip that takes a destination as a positional argument, and **kwargs for details 
# such as duration, budget, and season. The function should print out a trip summary. 
def plan_trip(des,**kwargs):
    print("Your ",des,"Trip.")
    for key,values in kwargs.items():
        print(f"{key} : {values}")
plan_trip("UK",Duration="120 km",Budget=20000,Season="Summer")

# --- End of 3rd.py ---

# Write a function apply_discount that takes two arguments: price and an optional discount keyword 
# argument with a default value of 0. It should return the price after applying the discount. If the 
# discount is not provided, the full price is returned.
def apply_discount(price,discount=0):
    return price-discount
print(f"With Discount: {apply_discount(price=20000,discount=1200)}")
print(f"With Out Discount:{ apply_discount(price=20000)}")


# --- End of 4rt.py ---

# Create a function vacation_cost that takes a positional argument days, an arbitrary number of 
# *activities, and keyword arguments for flight_cost and hotel_cost. The function should calculate the 
# total vacation cost by adding the cost of activities, flight, and hotel.
def vacation_cost(days,flight,hotel,**all):
    print(days," Days of Vacation Total Cost.")
    total=flight+hotel
    for i in all.values():
        total+=i
    return total
print(vacation_cost(7,flight=134000,hotel=17000,rideing=1200,swimming=1600,lanch=3400,taxi=2000))

# --- End of 5th.py ---

# Write a function register_member that accepts arbitrary keyword arguments (**kwargs) for member 
# details (e.g., name, age, membership_type). The function should print all the member details. 
# Register multiple members with different sets of information. 
def register_member(**kwargs):
    for key,values in kwargs.items():
        print(f"{key} : {values}")
register_member(name="x",age=10,membership_type="Golden")



# --- End of 6th.py ---

# Write a function checkout that takes an arbitrary number of item prices using *args and returns the 
# total cost. Simulate the checkout process for a few different customers buying multiple items.

def checkout(*args):
    total_cost = sum(args)
    return total_cost

print(checkout(10, 20, 30))  


# --- End of 7th.py ---

# Create a function convert_temperature that takes a temperature argument and a scale argument 
# with a default value of "Celsius". The function should convert the temperature to Fahrenheit if the 
# scale is "Celsius", otherwise convert it to Celsius. Call the function with and without the scale 
# argument. 
def convert_temperature(temp, scale="Celsius"):
    if scale == "Celsius":
        return temp * 9/5 + 32
    else:
        return (temp - 32) * 5/9

print(convert_temperature(30))  
print(convert_temperature(30, "Fahrenheit"))  


# --- End of 8th.py ---

# Write a function gym_membership that takes three keyword arguments: name, membership_type, 
# and duration. The function should return a message detailing the gym membership. Call the function 
# with keyword arguments.

def gym_membership(name, mem, duration):
    return f"{name}'s {mem} membership lasts for {duration} months."

print(gym_membership(name="John Doe", mem="Standard", duration=12))

# --- End of 9th.py ---

# Write a function meal_cost that takes two positional arguments: meal_price and tip_percent. It 
# should return the total cost of the meal including the tip. Call the function with different values.

def meal_cost(price, tip):
    tips=price * tip / 100
    return price+tips 
print(meal_cost(200, 15))  

# --- End of 10th.py ---

a=[45,7,9,9,1,2,3,4,5]
a.insert(1,3)
print(a)