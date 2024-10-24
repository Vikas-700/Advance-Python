import random 
list1=["Rock","Pepper","Seisor"]
you=0
computer=0
try:
    while True:
        input_guess=int(input(" 1.Rock \n 2.Pepper \n 3.Seisor \n 4.Exit \nChoise Any one:"))
        com_guess=random.choice(list1)
        if input_guess==4:
            if you-computer>0:
                print("You Won the  Overall Game!")
            else:
                print("Computer Won the  Overall Game!")
            print("Thank you!")
            break
        if input_guess==1:
            if com_guess=="Pepper":
                print("Computer pepper beat your Rock \n computer won!")
                computer+=1
            elif com_guess=="Seisor":
                print("Your Rock beat  computer Seisor \n you Won!")
                you+=1
            else:
                print("Draw!")
        if input_guess==2:
            if com_guess=="Seisor":
                print("Computer Seisor beat your pepper \n computer won!")
                computer+=1
            elif com_guess=="Rock":
                print("Your Pepper beat computer Rock \n you Won!")
                you+=1
            else:
                print("Draw!")
        if input_guess==3:
            if com_guess=="Rock":
                print("Computer Rock beat your Seisor \n computer won!")
                computer+=1
            elif com_guess=="Pepper":
                print("Your Seisor beat computer pepper \n you Won!")
                you+=1
            else:
                print("Draw!")
except:
    print("Invalid Input.")