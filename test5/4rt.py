# Write a function apply_discount that takes two arguments: price and an optional discount keyword 
# argument with a default value of 0. It should return the price after applying the discount. If the 
# discount is not provided, the full price is returned.
def apply_discount(price,discount=0):
    return price-discount
print(f"With Discount: {apply_discount(price=20000,discount=1200)}")
print(f"With Out Discount:{ apply_discount(price=20000)}")
