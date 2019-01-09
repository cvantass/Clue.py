#coding=utf-8
# file: SetnorClue.py

import time
import sys
import random

#The Deck
rooms = ['room 301', 'room 400', 'the lounge', 'the bathroom',
         'Setnor auditorium', 'the practice room',
         'the electronic music studio', 'the bell tower',
         'behind the organ', 'Hendrix chapel']

weapons = ['the circle egg', 'white jazz music', 'too many cocaine-fueled emails',
           'diversity of thought',
           'the machine of mastery']

names = ['MacDougall', 'Dr. Nic', 'James Tapia', 'Tyme', 'The White Jazz Grand Wizard',
         'The Ghost of Stephen Ferre', 'PMA', 'SAI', 'FYP']

#Player 1 Hand
player1_rooms = [rooms.pop(random.randint(0, (len(rooms) - 1)))]
player1_rooms.append(rooms.pop(random.randint(0, (len(rooms) - 1))))

player1_weapons = [weapons.pop(random.randint(0, (len(weapons) - 1)))]

player1_names = [names.pop(random.randint(0, (len(names) - 1)))]
player1_names.append(names.pop(random.randint(0, (len(names) - 1))))

#Player 2 Hand
player2_rooms = [rooms.pop(random.randint(0, (len(rooms) - 1)))]
player2_rooms.append(rooms.pop(random.randint(0, (len(rooms) - 1))))

player2_weapons = [weapons.pop(random.randint(0, (len(weapons) - 1)))]

player2_names = [names.pop(random.randint(0, (len(names) - 1)))]
player2_names.append(names.pop(random.randint(0, (len(names) - 1))))

#Player 3 Hand
player3_rooms = [rooms.pop(random.randint(0, (len(rooms) - 1)))]
player3_rooms.append(rooms.pop(random.randint(0, (len(rooms) - 1))))

player3_weapons = [weapons.pop(random.randint(0, (len(weapons) - 1)))]

player3_names = [names.pop(random.randint(0, (len(names) - 1)))]
player3_names.append(names.pop(random.randint(0, (len(names) - 1))))

#User's Hand
user_rooms = [rooms.pop(random.randint(0, (len(rooms) - 1)))]
user_rooms.append(rooms.pop(random.randint(0, (len(rooms) - 1))))
user_rooms.append(rooms.pop(random.randint(0, (len(rooms) - 1))))

user_weapons = [weapons.pop(random.randint(0, (len(weapons) - 1)))]

user_names = [names.pop(random.randint(0, (len(names) - 1)))]
user_names.append(names.pop(random.randint(0, (len(names) - 1))))

#Solution
fin_room = rooms.pop(0)
fin_weapon = weapons.pop(0)
fin_suspect = names.pop(0)
final = (fin_suspect + ' did it with ' + fin_weapon + ' in ' + fin_room)


#Game Introduction
print()
print()
print()
print("Welcome to Clue: Setnor School of Music Edition!")
print()
sys.stdout.flush()
time.sleep(1)
print("The Director of the school, Martha Sutter, has been found dead!")
print()
sys.stdout.flush()
time.sleep(2)
print("Now it's your job to find the killer, the weapon they used,")
print("and where the murder took place.")
print()
sys.stdout.flush()
time.sleep(2)
print("What's that? You don't even go here anymore?")
print("You're glad she's dead and they can all die for all you care?")
print("Well too bad! it's time to leave your awkward urinal conversation")
print("with Bradley P. Ethington and solve this mystery!")
print()
print()
sys.stdout.flush()
time.sleep(3)
print("Here is your checklist of possibilities:")
print()

#Checklist
rooms = ['room 301', 'room 400', 'the lounge', 'the bathroom',
         'Setnor auditorium', 'the practice room',
         'the electronic music studio', 'the bell tower',
         'behind the organ', 'Hendrix chapel']

weapons = ['the circle egg', 'white jazz music', 'too many cocaine-fueled emails',
           'diversity of thought',
           'the machine of mastery']

names = ['MacDougall', 'Dr. Nic', 'James Tapia', 'Tyme', 'The White Jazz Grand Wizard',
         'The Ghost of Stephen Ferre', 'PMA', 'SAI', 'FYP']

print("ROOMS")
for i in rooms:
    print(i)
    sys.stdout.flush()
    time.sleep(0.5)
sys.stdout.flush()
time.sleep(1)
print()

print("WEAPONS")
for i in weapons:
    print(i)
    sys.stdout.flush()
    time.sleep(0.5)
sys.stdout.flush()
time.sleep(1)
print()

print("SUSPECTS")
for i in names:
    print(i)
    sys.stdout.flush()
    time.sleep(0.5)
sys.stdout.flush()
time.sleep(1)
print()

#Your Hand
print("Here's what you know DIDN\'T happen!")
print()
print(user_rooms)
print(user_weapons)
print(user_names)
print()

#Keeps track of guesses
player1_guess = [0, True]
player2_guess = [0, True]
player3_guess = [0, True]

#Gameplay
while player1_guess[1] == True or player2_guess[1] == True or player3_guess[1] == True:
    print("You may make your guess: ")
    sys.stdout.flush()
    time.sleep(0.5)

    guess_room_1 = input("Room? ")
    while guess_room_1 not in rooms or guess_room_1 in user_rooms:
        if guess_room_1 not in rooms:
            guess_room_1 = input("Sorry, that's not in the list! Please guess again: ")
        else:
            guess_room_1 = input("You already know this one! Guess again: ")
    guess_weapon_1 = input("Weapon? ")
    while guess_weapon_1 not in weapons or guess_weapon_1 in user_weapons:
        if guess_weapon_1 not in weapons:
            guess_weapon_1 = input("Sorry, that's not in the list! Please guess again: ")
        else:
            guess_weapon_1 = input("You already know this one! Guess again: ")
    guess_name_1 = input("Suspect? ")
    while guess_name_1 not in names or guess_name_1 in user_names:
        if guess_name_1 not in names:
            guess_name_1 = input("Sorry, that's not in the list! Please guess again: ")
        else:
            guess_name_1 = input("You already know this one! Guess again: ")
    print()

    player1_guess = [0, True]
    player2_guess = [0, True]
    player3_guess = [0, True]

#Check PLAYER 1    
    if guess_room_1 in player1_rooms:  
        for i in player1_rooms:
            if guess_room_1 == i:
                print('Player 1 says ' + i + ' is incorrect!')
                print()
                add = input("Would you like to add this to your list? ")
                print()
                if add.upper() == 'YES' or add.upper() == 'Y':
                    user_rooms.append(i)
                    print("Here's what you know DIDN\'T happen!")
                    print()
                    print(user_rooms)
                    print(user_weapons)
                    print(user_names)
                    print()
    elif guess_weapon_1 in player1_weapons:
        for i in player1_weapons:
            if guess_weapon_1 == i:
                print('Player 1 says ' + i + ' is incorrect!')
                print()
                add = input("Would you like to add this to your list? ")
                print()
                if add.upper() == 'YES' or add.upper() == 'Y':
                    user_weapons.append(i)
                    print("Here's what you know DIDN\'T happen!")
                    print()
                    print(user_rooms)
                    print(user_weapons)
                    print(user_names)
                    print()
    elif guess_name_1 in player1_names:
        for i in player1_names:
            if guess_name_1 == i:
                print('Player 1 says ' + i + ' is incorrect!')
                print()
                add = input("Would you like to add this to your list? ")
                print()
                if add.upper() == 'YES' or add.upper() == 'Y':
                    user_names.append(i)
                    print("Here's what you know DIDN\'T happen!")
                    print()
                    print(user_rooms)
                    print(user_weapons)
                    print(user_names)
                    print()
    else:
        print("Player 1 says: I got nothin'!")
        player1_guess[0] += 1
        player1_guess[1] = False

    sys.stdout.flush()
    time.sleep(1)
    
#Check PLAYER 2
    if player1_guess[1] == False:
        if guess_room_1 in player2_rooms:
            for i in player2_rooms:
                if guess_room_1 == i:
                    print('Player 2 says ' + i + ' is incorrect!')
                    print()
                    add = input("Would you like to add this to your list? ")
                    print()
                    if add.upper() == 'YES' or add.upper() == 'Y':
                        user_rooms.append(i)
                        print("Here's what you know DIDN\'T happen!")
                        print()
                        print(user_rooms)
                        print(user_weapons)
                        print(user_names)
                        print()
        elif guess_weapon_1 in player2_weapons:
            for i in player2_weapons:
                if guess_weapon_1 == i:
                    print('Player 2 says ' + i + ' is incorrect!')
                    print()
                    add = input("Would you like to add this to your list? ")
                    print()
                    if add.upper() == 'YES' or add.upper() == 'Y':
                        user_weapons.append(i)
                        print("Here's what you know DIDN\'T happen!")
                        print()
                        print(user_rooms)
                        print(user_weapons)
                        print(user_names)
                        print()
        elif guess_name_1 in player2_names:
            for i in player2_names:
                if guess_name_1 == i:
                    print('Player 2 says ' + i + ' is incorrect!')
                    print()
                    add = input("Would you like to add this to your list? ")
                    print()
                    if add.upper() == 'YES' or add.upper() == 'Y':
                        user_names.append(i)
                        print("Here's what you know DIDN\'T happen!")
                        print()
                        print(user_rooms)
                        print(user_weapons)
                        print(user_names)
                        print()
        else:
            print("Player 2 says: I got nothin'!")
            player2_guess[0] += 1
            player2_guess[1] = False

    sys.stdout.flush()
    time.sleep(1)

#Check PLAYER 3
    if player1_guess[1] == False and player2_guess[1] == False:
        if guess_room_1 in player3_rooms:
            for i in player3_rooms:
                if guess_room_1 == i:
                    print('Player 3 says ' + i + ' is incorrect!')
                    print()
                    add = input("Would you like to add this to your list? ")
                    print()
                    if add.upper() == 'YES' or add.upper() == 'Y':
                        user_rooms.append(i)
                        print("Here's what you know DIDN\'T happen!")
                        print()
                        print(user_rooms)
                        print(user_weapons)
                        print(user_names)
                        print()
        elif guess_weapon_1 in player3_weapons:
            for i in player3_weapons:
                if guess_weapon_1 == i:
                    print('Player 3 says ' + i + ' is incorrect!')
                    print()
                    add = input("Would you like to add this to your list? ")
                    print()
                    if add.upper() == 'YES' or add.upper() == 'Y':
                        user_weapons.append(i)
                        print("Here's what you know DIDN\'T happen!")
                        print()
                        print(user_rooms)
                        print(user_weapons)
                        print(user_names)
                        print()
        elif guess_name_1 in player3_names:
            for i in player3_names:
                if guess_name_1 == i:
                    print('Player 3 says ' + i + ' is incorrect!')
                    print()
                    add = input("Would you like to add this to your list? ")
                    print()
                    if add.upper() == 'YES' or add.upper() == 'Y':
                        user_names.append(i)
                        print("Here's what you know DIDN\'T happen!")
                        print()
                        print(user_rooms)
                        print(user_weapons)
                        print(user_names)
                        print()
        else:
            print("Player 3 says: I got nothin'!")
            print()
            player3_guess[0] += 1
            player3_guess[1] = False

    sys.stdout.flush()
    time.sleep(1)
    
#Mystery Solved
if guess_room_1 == fin_room and guess_weapon_1 == fin_weapon and guess_name_1 == fin_suspect:
        print("You solved the mystery!")
        print(final)
