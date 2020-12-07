from art import logo, vs
from game_data import data
from replit import clear
import random

def celebrity_picker():
    '''Picks a random celebrity from the list and returns it.'''
    choice = random.choice(data)
    return choice

def celebrity_comparer(celebrityA, celebrityB):
    '''Compares the celebrityA to be compared to celebrityB to return who has won as a string.'''
    if celebrityA['follower_count'] > celebrityB['follower_count']:
        return 'a'
    else:
        return 'b'

def game():
    '''Runs the game when it is called'''
    
    score = 0
    celeb_a = celebrity_picker()
    lost = False
    while not lost:
        celeb_b = celebrity_picker()
        if celeb_a == celeb_b:
            celeb_b = celebrity_picker()
        print(f"Compare A: {celeb_a['name']}, a {celeb_a['description']}, from {celeb_a['country']}.")
        print(vs)
        print(f"Compare B: {celeb_b['name']}, a {celeb_b['description']}, from {celeb_b['country']}.")
        winner = celebrity_comparer(celeb_a, celeb_b)
        user_selection = input('Who has more followers? A or B: ').lower()
        print("---------------------------------------------------------")
        if user_selection == winner:
            score +=1
            clear()
            print(logo)
            print(f"You're right! Your score is {score}.")
            print("---------------------------------------------------------")
            celeb_a = celeb_b
        else:
            print(f"Sorry, that is wrong. You lose. The final score is {score}.")
            lost = True
            print("---------------------------------------------------------")

start = True
while start:
    restart = input('Would you like to play higher vs lower? Type "y" to play, "n" to quit. ').lower()
    if restart == 'y':
        clear()
        print(logo)
        game()
    else:
        print('Goodbye!')
        start = False


