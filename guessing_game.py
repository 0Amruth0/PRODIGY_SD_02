import random

def guess_the_number():
  secret_number = random.randint(1, 100)
  num_guesses = 0

  while True:
    try:
      guess = int(input("Guess a number between 1 and 100: "))
      num_guesses += 1

      if guess == secret_number:
        print(f"You guessed it! The number was {secret_number}. It took you {num_guesses} tries.")
        break
      elif guess < secret_number:
        print("Your guess is too low. Try again!")
      else:
        print("Your guess is too high. Try again!")
    except ValueError:
      print("Invalid input. Please enter a number.")

if __name__ == "__main__":
  guess_the_number()
