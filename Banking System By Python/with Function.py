Accounts=[]
def create_account():
    user_name = input("Enter Your Name: ")
    user_id = 2024 + len(Accounts)
    user = {
        "Id": user_id,
        "Name": user_name,
        "Balance": 0
    }
    Accounts.append(user)
    print(f"{user['Name']} your Account Created! And Your Account Number is {user['Id']}")
def deposit_money():
    aco_no = int(input("Enter Your Account Number: ").strip())
    for i in Accounts:
        if i['Id'] == aco_no:
            print(f"== Welcome {i['Name']} ==")
            user_depo = float(input("Enter Amount: "))
            i["Balance"] += user_depo
            print("Your Deposit Done!")
            break
    else:
        print("Account Not Found!")
def withdraw_money():
    aco_no = int(input("Enter Your Account Number: ").strip())
    for i in Accounts:
        if i['Id'] == aco_no:
            print(f"== Welcome {i['Name']} ==")
            user_with = float(input("Enter Amount: "))
            if user_with <= i["Balance"]:
                i["Balance"] -= user_with
                print("Withdrawal Done!")
            else:
                print("Aukad Nahi Hai AApki!")

            break
    else:
        print("Account Not Found!")
def check_balance():
    aco_no = int(input("Enter Your Account Number: ").strip())
    for i in Accounts:
        if i['Id'] == aco_no:
            print(f"== Welcome {i['Name']} ==")
            print(f"Your Balance is {i['Balance']}")
            break
    else:
        print("Account Not Found!")
def menu():
    while True:
        print("\n=== Banking System Menu ===")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = int(input("\nEnter your choice: "))
        
        if choice == 1:
            create_account()
        elif choice == 2:
            deposit_money()
        elif choice == 3:
            withdraw_money()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            print("Thanks for useing our Bank.")
            break
        else:
            print("Please choise Correct Input:")
menu()
