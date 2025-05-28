import random

# Generate random number from 1 to 10
secret_number = random.randint(1, 10)

# Get the user's guess
guess = int(input("I'm thinking of a number from 1 to 10. Can you guess what it is? "))

# Validate input before matching
if guess < 1 or guess > 10:
    print("Invalid input. Please enter a number between 1 and 10.")
else:
    # Match case block for valid input
    match guess:
        #If the user gets it right
        case _ if guess == secret_number:
            print("Congratulations, you guessed it!")

            #Ask if the user wants to play again
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again == 'yes' :
                print(". . . (game restarts)")
            else:
                print("Thanks for playing!")

        # If the guess is too low 
        case _ if guess < secret_number:
            print("Nope, your guess is too low. Try again.")

        # If the guess is too high
        case _ if guess > secret_number:
            print("Oops, your guess is too high. Try again.")
