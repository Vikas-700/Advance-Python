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