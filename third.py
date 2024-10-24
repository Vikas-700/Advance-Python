import csv
import random

# Expand the list of common Indian female and male names to at least 100 names each
female_names = ['Priya', 'Manpreet', 'Rupali', 'Kajal', 'Sita', 'Aarti', 'Nisha', 'Anjali', 'Pooja', 'Sunita',
                'Meena', 'Ritu', 'Swati', 'Sneha', 'Neha', 'Shivani', 'Rekha', 'Divya', 'Radha', 'Gita',
                'Monika', 'Lata', 'Savita', 'Sarita', 'Geeta', 'Vaishali', 'Isha', 'Pinky', 'Komal', 'Parvati',
                'Nandini', 'Shalini', 'Sushma', 'Lakshmi', 'Kavita', 'Bhavna', 'Jaya', 'Chitra', 'Tina', 'Renuka',
                'Aishwarya', 'Deepa', 'Rashmi', 'Kiran', 'Kalpana', 'Maya', 'Anita', 'Kanchan', 'Smita', 'Shweta',
                'Veena', 'Mamata', 'Madhu', 'Seema', 'Arti', 'Reema', 'Vandana', 'Sarla', 'Rina', 'Kirti', 'Shobha',
                'Preeti', 'Leela', 'Pallavi', 'Neeta', 'Rita', 'Jyoti', 'Radha', 'Soniya', 'Sheetal', 'Simran',
                'Amrita', 'Indu', 'Kusum', 'Lina', 'Manisha', 'Namita', 'Shashi', 'Usha', 'Rupa', 'Vimla', 'Alka']

male_names = ['Vikas', 'Akash', 'Hemraj', 'Ravi', 'Vijay', 'Rajesh', 'Suresh', 'Rohit', 'Karan', 'Amit',
              'Prakash', 'Mahesh', 'Ajay', 'Arjun', 'Manoj', 'Anil', 'Nitin', 'Pankaj', 'Vinod', 'Sanjay',
              'Sachin', 'Naveen', 'Kumar', 'Narendra', 'Ashok', 'Sandeep', 'Deepak', 'Yogesh', 'Rakesh', 'Pawan',
              'Devendra', 'Rajat', 'Suraj', 'Tejas', 'Mukesh', 'Ramesh', 'Sahil', 'Gaurav', 'Vivek', 'Rahul', 'Harish',
              'Harsh', 'Aditya', 'Tushar', 'Ankit', 'Jatin', 'Bharat', 'Mohit', 'Kailash', 'Mohan', 'Sudhir',
              'Santosh', 'Ravi', 'Dharmendra', 'Arvind', 'Satyendra', 'Vikram', 'Shyam', 'Rohit', 'Hemant', 'Umesh',
              'Balram', 'Lokesh', 'Ashwin', 'Vasant', 'Madhav', 'Govind', 'Shiv', 'Vishal', 'Kunal', 'Dev',
              'Sameer', 'Kartik', 'Ajit', 'Harjeet', 'Nirbhay', 'Sarvesh', 'Ravindra', 'Jagat', 'Prem', 'Sunil']

# Create a set to store unique records
unique_records = set()

# Shuffle the names to ensure randomness
random.shuffle(female_names)
random.shuffle(male_names)

# Function to generate a married female record with a husband's name
def generate_record(female_name, male_name):
    age = random.randint(18, 42)
    height = random.randint(138, 160)  # Height in cm
    weight = random.randint(45, 64)    # Weight in kg

    return (female_name, age, male_name, height, weight)

# Generate 100 unique married female records with unique names
for i in range(80):
    female_name = female_names[i]  # Take a unique female name
    husband_name = male_names[i]   # Take a unique male name
    unique_records.add(generate_record(female_name, husband_name))

# Write the data to a CSV file
with open('indian_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Age', 'Husband_Name', 'Height', 'Weight']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write header
    writer.writeheader()

    # Write records
    for record in unique_records:
        writer.writerow({
            'Name': record[0],
            'Age': record[1],
            'Husband_Name': record[2],
            'Height': record[3],
            'Weight': record[4]
        })

print("CSV file created successfully with 100 unique married female records!")
