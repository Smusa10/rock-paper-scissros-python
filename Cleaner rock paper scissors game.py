import random

# The list of choices in the game
choices = ['rock', 'paper', 'scissors']

# This asks the user to make a choice
def get_user_choice():
    user_choice = input('Choose rock, paper or scissors')
    return user_choice

# The computer picks a random choice from the list
def get_computer_choice():
    return random.choice(choices)

# we need to determine the winner of each round
def determine_winner(user, computer):
    if (
        (user == 'rock' and computer == 'scissors') or
        (user == 'paper' and computer == 'rock') or
        (user == 'scissors' and computer == 'paper')
    ):
        return 'user'
    elif user == computer:
        return 'draw'
    else:
        return 'computer'

# This part runs the full game
def play_game():
        print('Lets Start the Game!')
        user_score = 0
        computer_score = 0

#we need more than 1 round
        for round_number in range(1,5):
            print(f'\nRound {round_number}')
            user = get_user_choice()
            computer = get_computer_choice()

            print('\nYou chose:', user)
            print('Computer chose:', computer)

            winner = determine_winner(user,computer)

            if winner == 'draw':
                print ('Its a draw')

            elif winner == 'user':
                print('You win this round')
                user_score += 1
            else:
                print('Computer wins this round')
                computer_score += 1

            print('\nScore : You:', user_score, 'Computer:', computer_score)

        if user_score > computer_score:
            print('\nYou won this game!')
        elif computer_score > user_score:
            print('\nComputer won the game')
        else:
            print ('\nThe game ended in a stalemate')

# This part starts the game
play_game()
