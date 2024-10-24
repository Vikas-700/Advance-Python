#how to find it leap year or not
x=int(input("Enter A year:"))
if x%400==0:
    print("It's a Leap year.")
elif x%100==0:
    print("It's not a leap year.")
elif x%4==0:
    print("It's a Leap year.")
else:
    print("It's not a leap year.")



