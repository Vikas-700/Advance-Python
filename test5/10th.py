# Write a function meal_cost that takes two positional arguments: meal_price and tip_percent. It 
# should return the total cost of the meal including the tip. Call the function with different values.

def meal_cost(price, tip):
    tips=price * tip / 100
    return price+tips 
print(meal_cost(200, 15))  