from random import randint
from time import sleep
from art import art
from functions import difficulty, name_validator, header, choice_validator, update_att, guess_result

# print the art ascii
print(art)

# Main program
header("✅ Let's Start!!")

name = name_validator("✔ Enter your name: ")
print(f'\n✔ {name}, welcome to the number guessing name')

header('✅ Choice a level!')

choice = choice_validator(f"✔ {name}, choose a difficulty. Type 'easy' or 'hard': ")
attempts = difficulty(choice)

header('✅ The game!')

update_att(name, attempts)

header('✅ The machine is choosing a number.')
number = randint(0, 100)
sleep(1)
print("🔗 The number was choosen!")

header("✅ It's your time!")

guess_result(attempts, number, name)
