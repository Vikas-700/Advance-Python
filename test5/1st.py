# Create a function donation_total that accepts a positional-only argument donation_amount, a 
# keyword-only argument service_fee_percent, and returns the total amount including the service fee.
def donation_total(amount,S_fee):
    fee=(amount*S_fee)/100
    return fee+amount
print(donation_total(30000,S_fee=7))
