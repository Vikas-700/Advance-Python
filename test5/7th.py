# Write a function checkout that takes an arbitrary number of item prices using *args and returns the 
# total cost. Simulate the checkout process for a few different customers buying multiple items.

def checkout(*args):
    total_cost = sum(args)
    return total_cost

print(checkout(10, 20, 30))  # Output: 60
