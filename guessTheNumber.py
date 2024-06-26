secret_number = "5"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_number and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Take a guess: ")
        guess_count += 1
        if guess > secret_number:
            print("The guess is too high.")
        elif guess < secret_number:
            print("The guess is too low.")
        elif guess == secret_number:
            print("The guess is correct. You won the game.")
    else:
        out_of_guesses = True

if out_of_guesses and guess != secret_number:
    print("Out of guesses, you lose!")
