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

    