def header(text):
    '''Create a pattern headers for the program.'''
    print()
    print(50*'-')
    print(f'{text:^50}')
    print(50*'-')
    print()


def name_validator(text):
    '''Checks if the name entered is valid'''
    while True:
        name = input(text).strip().capitalize()
        if name == '' or name.isdigit() or name.isalnum() is not True:
            print('❌ Enter a valid name.')
        else:
            return name


def choice_validator(text):
    '''Checks if the leval chosen is into the options available'''
    while True:
        choice = input(text).strip().lower()
        if choice not in "easyhard" or choice == '':
            print('❌ Enter with a valid option.')
        else:
            break
    return choice


def difficulty(choice):
    '''Assign a number of attempts based on the user's choice'''
    attempt = 5
    if choice == 'easy':
        attempt = 10
    return attempt


def update_att(name, attempts):
    '''update the number of attempts avallaible'''
    print(f'✔ {name}, you have {attempts} attempts remaning to guess the number.\n')


def guess_validator():
    '''Check is the input guess receveived a valid character'''
    while True:
        guess = input('✔ Make a guess: ')
        if guess.isdigit() is not True:
            print("❌ Enter a valid number.")
        else:
            break
    return int(guess)


def number_reveal(number):
    '''Reveals the secret number'''
    print(f"✔  The secret number was {number}")


def guess_result(attempts, number, name):
    '''Compares the guess with the secret number and give the results and,
       while compares, subtracts the number of the initital attempts available.
    '''
    from sys import exit
    from time import sleep
    while attempts >= 1:
        guess = guess_validator()
        attempts -= 1
        if guess > number:
            print('🤐 Too high\n')
        elif guess < number:
            print('😥 Too low\n')
        else:
            header(f'✌ {name} You goal!!')
            number_reveal(number)
            sleep(0.5)
            exit()

        if attempts != 0:
            update_att(name, attempts)

    header(f"😢 {name}, YOU LOOSE..")
    number_reveal(number)
