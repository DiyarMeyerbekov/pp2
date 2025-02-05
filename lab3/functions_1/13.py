import random
Running = True
name = str(input("Hello! What is your name?\n"))
print(f'Hello {name}!\n',f"\nWell, {name}, I am thinking of a number between 1 and 20.")
num = random.randint(1,20)
guess_count = 0
while Running:
    guess = int(input("Take a Guess\n"))
    guess_count += 1
    if guess > num:
        print("\nYour guess is too high.")
        continue
    elif guess < num:
        print("\nYour guess is too low.")
        continue
    else:
        print(f'Good job, {name}! You guessed my number in {guess_count} guesses!\n')
        Running = False