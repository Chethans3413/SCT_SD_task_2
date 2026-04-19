import random

def game():
    # 1. Generate the number ONCE before the loop starts
    secret_number = random.randint(1, 100)
    
    # UNCOMMENT THE LINE BELOW TO CHEAT FOR TESTING:
    # print(f"(Debug: The answer is {secret_number})")

    print("I have picked a number between 1 and 100.")
    
    while True:
        try:
            # 2. Convert input to an integer (Critical Step)
            user_input = input("Enter your guess: ")
            guess = int(user_input) 

            # 3. Comparison Logic
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print("Correct! You got it.")
                break # This exits the loop when they win

        except ValueError:
            print("That's not a number! Please enter digits only.")

game()