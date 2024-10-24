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
