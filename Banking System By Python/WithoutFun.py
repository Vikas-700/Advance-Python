Accounts=[]
while True:
    test=int(input(" 1.Create Account \n 2. Deposit Money \n 3. Withdraw Money \n 4. Check Balance \n 5. Exit \n Enter 1 to 5 :"))
    match (test):
        case 1:
            user_name=input("Enter Your Name:")
            user_id=2024+len(Accounts)
            user={
                "Id":user_id,
                "Name":user_name,
                "Balance":0
            }
            Accounts.append(user)
            print(f"{user['Name']}  your Account Created ! And Your Account Number is {user['Id']}")
        case 2:
            aco_no=int(input("Enter Your Account Number:").strip())
            for i in Accounts:
                if i['Id']==aco_no:
                    print(f"== Welcome {i['Name']} ==")
                    user_depo=float(input("Enter Amount:"))
                    i["Balance"]+=user_depo
                    print(f"Your {user_depo} Deposit Done!")
                    break
            else:
                print("Account Not Found!")
        case 3:
            aco_no=int(input("Enter Your Account Number:").strip())
            for i in Accounts:
                if i['Id']==aco_no:
                    print(f"== Welcome {i['Name']} ==")
                    user_with=float(input("Enter Amount:"))
                    if user_with<i["Balance"]:
                        i["Balance"]-=user_with
                        print("You Withdral Done!")
                    else:
                        print("Aukad me Rahkar Nikaal!")
                    break
            else:
                print("Account Not Found!")
        case 4:
            aco_no=int(input("Enter Your Account Number:").strip())
            for i in Accounts:
                if i['Id']==aco_no:
                    print(f"== Welcome {i['Name']} ==")
                    print("Now your Balance :",i["Balance"])
                    break
            else:
                print("Account Not Found!")
        case 5:
            print("Thanks for using our Bank")
            break
        case _:
            print("Please choise Correct Input:")
            break






    