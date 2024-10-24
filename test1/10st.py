cost=float(input("Enter Cost Price:"))
sell=float(input("Enter Selling Price:"))
if cost<sell:
    print("Profit is:",sell-cost)
else:
    print("Loss is:",cost-sell)