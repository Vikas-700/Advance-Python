def smart_calculator():
    try:
        x = float(input("Enter the first number: ").strip())
        y = float(input("Enter the second number: ").strip())
        s = input("Enter an operator (+, -, *, /, **, %): ").strip()

        operations = {
            '+': x + y,
            '-': x - y,
            '*': x * y,
            '/': x / y if y != 0 else "Cannot divide by zero",
            '**': x ** y,
            '%': x % y if y != 0 else "Cannot modulo by zero"
        }

        result = operations.get(s, "Invalid operator")
        return result 

    except ValueError:
        return "Invalid input. Please enter numeric values."

# Call the function
print("Result:", smart_calculator())
