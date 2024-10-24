import mysql.connector
import uuid
from datetime import datetime

# Connect to MySQL database
def connect_db():
    connection = mysql.connector.connect(
        host="localhost",  # Your MySQL host
        user="root",       # Your MySQL username
        password="root",  # Your MySQL password
        database="restaurant"  # Database name
    )
    return connection

# Function to generate and store the order details in MySQL
def generate_order(username, gender, age, marital_status, items_ordered, total_price):
    # Generate a unique order ID
    order_id = str(uuid.uuid4())
    
    # Capture current date and time
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")
    
    # Determine meal type based on time
    current_hour = now.hour
    if 5 <= current_hour < 12:
        meal_type = "Breakfast"
    elif 12 <= current_hour < 17:
        meal_type = "Lunch"
    else:
        meal_type = "Dinner"
    
    # Combine items and quantities into a single string
    items_str = "; ".join([f"{item} (x{quantity})" for item, quantity in items_ordered.items()])
    
    # Insert order details into MySQL database
    connection = connect_db()
    cursor = connection.cursor()

    # Insert query
    insert_query = """
    INSERT INTO orders (id, date, time, username, meal_type, gender, age, marital_status, items_ordered, total_bill)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    order_data = (order_id, date, time, username, meal_type, gender, age, marital_status, items_str, total_price)
    
    cursor.execute(insert_query, order_data)
    connection.commit()

    print(f"Order saved with ID: {order_id}")
    
    cursor.close()
    connection.close()

# Main function to take user input for order
def take_order():
    # Personal details input
    username = input("Enter your name: ")
    gender = input("Enter your gender (Male/Female): ")
    age = int(input("Enter your age: "))
    marital_status = input("Enter your marital status (Single/Married/Couple/Divorced): ")

    total_price = 0
    items_ordered = {}

    # Loop to take multiple item orders
    while True:
        user_in = int(input(" 1. Pizza \n 2. Burger \n 3. Tea \n 4. Cold Drink \n 5. Pasta \n Choose any item: "))
        
        match user_in:
            case 1:
                p = int(input("Quantity: "))
                total_price += p * price["Pizza"]
                items_ordered["Pizza"] = items_ordered.get("Pizza", 0) + p
            case 2:
                p = int(input("Quantity: "))
                total_price += p * price["Burger"]
                items_ordered["Burger"] = items_ordered.get("Burger", 0) + p
            case 3:
                p = int(input("Quantity: "))
                total_price += p * price["Tea"]
                items_ordered["Tea"] = items_ordered.get("Tea", 0) + p
            case 4:
                p = int(input("Quantity: "))
                total_price += p * price["Cold Drink"]
                items_ordered["Cold Drink"] = items_ordered.get("Cold Drink", 0) + p
            case 5:
                p = int(input("Quantity: "))
                total_price += p * price["Pasta"]
                items_ordered["Pasta"] = items_ordered.get("Pasta", 0) + p
            case _:
                print("Invalid choice, please choose again.")
                continue

        l = input("Do you want to order any other item? (Yes/No): ").lower()
        if l != "yes":
            print("Your Bill:", total_price)
            break
    
    # Generate the order and save to MySQL
    generate_order(username, gender, age, marital_status, items_ordered, total_price)


# Prices of items
price = {
    "Pizza": 1000,
    "Burger": 300,
    "Tea": 100,
    "Cold Drink": 200,
    "Pasta": 700
}

# Call the function to start taking orders
take_order()
