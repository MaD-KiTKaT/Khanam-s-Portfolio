import pygame
import random
import time
import threading


def countdown(t):
    while t > 0:
        print(t)
        t -= 1
        time.sleep(1)

def ask_q():
    q = input("Choose either Rock(R), Paper(P), or Scissors(S): ")
    return q

print("Welcome to Khanam's Rock, Paper, Scissors Game!")

Com = ['rock', 'paper', 'scissors']
Ran = random.choice(Com)
pygame.init()

my_sound = pygame.mixer.Sound('C:/Users/RPC-K/AppData/Local/CapCut/Videos/0421.MP3')
my_sound.play()

# Prompt the user for their choice before starting the countdown
choice = ask_q()

# Start the countdown thread
countdown_thread = threading.Thread(target=countdown, args=(10,))
countdown_thread.start()

# Wait for the countdown thread to finish
countdown_thread.join()

# Print the result after the countdown finishes
print("\nTIME'S UP!")
print("Computer has chosen... " + Ran)


# Add the rest of your game logic using the captured user_choice

if choice == Ran:
    print("It's a Tie!")

if choice == "R":
    if Ran == "paper":
        print("You have LOST!!")
    elif Ran == "scissors":
        print("Congrats! You have WON!!!")
    
if choice == "P":
    if Ran == "rock":
        print("Congrats! You have WON!!!")
    elif Ran == "scissors":
        print("You have LOST!!")
    
if choice == "S":
    if Ran == "rock":
        print("You have LOST!!")
    elif Ran == "paper":
        print("Congrats! You have WON!!!")
        
        
    
    
    








    
