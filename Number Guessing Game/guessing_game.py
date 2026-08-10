import random

print("===== NUMBER GUESSING GAME =====")
print("I'm thinking of a number between 1 and 100.")

secret_number = random.randint(1, 100)
max_attempts = 10
attempts = 0

while attempts < max_attempts:
    try:
        guess = int(input("\nEnter your guess: "))

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")

        elif guess > secret_number:
            print("Too high! Try again.")

        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

        print(f"Attempts remaining: {max_attempts - attempts}")

    except ValueError:
        print("Invalid input! Please enter a whole number.")

else:
    print("\nGame over!")
    print(f"The correct number was {secret_number}.")