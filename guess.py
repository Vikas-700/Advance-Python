# import random
# jacpot=random.randint(1,100)
# guess=int(input("Guess Karo:"))
# while jacpot!=guess:
#     if guess<jacpot:
#         print("guess Higher!")
#     else:
#         print("guess Lower!")
#     guess=int(input("guess karo:"))
#     if guess==jacpot:
#         break
# print("Correct guess!")
   
import random
import itertools

jackpot = random.randint(1, 100)

print("Welcome to the Guessing Game! Guess the correct number between 1 and 100.")

for attempt in itertools.count(1):  # Infinite loop, counting attempts
    guess = int(input(f"Attempt {attempt} - Guess the number: "))
    
    if guess < jackpot:
        print("Guess Higher!")
    elif guess > jackpot:
        print("Guess Lower!")
    else:
        print(f"Correct guess! You won in {attempt} attempts!")
        break
