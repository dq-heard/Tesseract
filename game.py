import classes
import combat
import sys
import os
import time
import platform

bcolors = classes.bcolors

##### Map Setup #####
DESCRIPTION = 'desc'
INFO = 'info'
RIDDLE = 'riddle'
ANSWER = 'answer'
REPS = 0
SIDE_UP = 'up'
SIDE_DOWN = 'down'
SIDE_LEFT = 'left'
SIDE_RIGHT = 'right'

cube = {
	'ceiling': {
		DESCRIPTION: "You find yourself standing on clouds, strangely enough.\nHeaven and Earth are one and the same here.",
		INFO: "Even stranger than the ground reflecting the sky is the star that begins speaking to you.\n",
		RIDDLE: f"{bcolors.BOLD}It ominously inquires:\nI conjure love more than Cupid, but create fear unlike any man or beast.{bcolors.ENDC}"
                f"{bcolors.BOLD}\nMy reach is limitless, yet I don't exist. What am I?{bcolors.ENDC}",
		ANSWER: ["imagination", "my imagination", "your imagination", "an imagination", "our imagination"],
		REPS: 0,
		SIDE_UP: 'north',
		SIDE_DOWN: 'south',
		SIDE_LEFT: 'east',
		SIDE_RIGHT: 'west',
	},
	'north': {
		DESCRIPTION: "You find yourself in an Arctic valley\nwith mountains as far as your sight can stretch to see.",
		INFO: "A soft, incandescent glow illuminates a nearby cave\nhousing shadowy figures of varying shapes and sizes.\n",
		RIDDLE: f"{bcolors.BOLD}From seemingly nowhere, you hear:\nYou measure my life in hours and I serve you by expiring.{bcolors.ENDC}"
                f"{bcolors.BOLD}\nI am always eating, but never thirsty. What am I?{bcolors.ENDC}", 
		ANSWER: ["fire", "flame", "fires","flames", "a fire", "a flame"],
        REPS: 0,
		SIDE_UP: 'ceiling',
		SIDE_DOWN: 'floor',
		SIDE_LEFT: 'west',
		SIDE_RIGHT: 'east',
	},
	'floor': {
		DESCRIPTION: "You find yourself in a pretty, but unassuming grassy field.\nSomething feels amiss, as if a piece is missing from this world.",
		INFO: "A rather large, though easily overlookable keyhole sits flush in the middle of the field.\nHow odd.\n",
		RIDDLE: f"{bcolors.BOLD}The key has to be somewhere around here.\nYou seemingly can't do anything in this realm until you find it.{bcolors.ENDC}",
		REPS: 0, #Will work after you solve all other riddles.
		SIDE_UP: 'north',
		SIDE_DOWN: 'south',
		SIDE_LEFT: 'west',
		SIDE_RIGHT: 'east',
	},
	'east': {
		DESCRIPTION: "You find yourself in lively rainforest,\nbursting with wildlife and a cacaphony of chirping.",
		INFO: "A grizzled man sits next to a soggy tent.\nHis gaze is stuck in his binoculars, but he still notices you approaching.\n",
		RIDDLE: f"{bcolors.BOLD}He says to you:\nThere were five birds in this tree, all on the same branch.\n{bcolors.ENDC}"
                f"{bcolors.BOLD}Some fellow came by and cruelly hit one with a slingshot earlier.\nHow many birds were still left in the tree?{bcolors.ENDC}",
		ANSWER: ["none", "zero", "0"],
        REPS: 0,
		SIDE_UP: 'north',
		SIDE_DOWN: 'south',
		SIDE_LEFT: 'floor',
		SIDE_RIGHT: 'ceiling',
	},
	'west': {
		DESCRIPTION: "You find yourself smothered by strong breezes and dry heat.\nThere's no signs of life anywhere...",
		INFO: "A tumbleweed bounces across the sand dunes\nand you hear a voice cutting through the high winds.\n",
		RIDDLE: f"{bcolors.BOLD}It asks:\nWhat can run but never walks, has a mouth but never talks,{bcolors.ENDC}"
                f"{bcolors.BOLD}\nhas pockets that aren't deep, and a bed but never sleeps?{bcolors.ENDC}",
		ANSWER: ["river", "rivers", "a river"],
        REPS: 0,
		SIDE_UP: 'north',
		SIDE_DOWN: 'south',
		SIDE_LEFT: 'ceiling',
		SIDE_RIGHT: 'floor',
	},
	'south': {
		DESCRIPTION: "You find yourself next to a still, soothing pond.\nA lonely, old woman gazes at it from a table nearby.",
		INFO: "You greet the weathered-looking lady.\nYou're the first visitor she's had in a long time\nand she beckons you to take a seat.\n",
		RIDDLE: f"{bcolors.BOLD}She says to you:\nYou have them today, tomorrow you'll have more.\nAs time passes, they're not easy to store.\n{bcolors.ENDC}"
                f"{bcolors.BOLD}They take up no space and only reside in one place. What am I?{bcolors.ENDC}",
		ANSWER: ["memory", "memories", "a memory"],
        REPS: 0,
		SIDE_UP: 'floor',
		SIDE_DOWN: 'ceiling',
		SIDE_LEFT: 'west',
		SIDE_RIGHT: 'east',
	}
}

##### Title Screen #####
def title_screen_menu():
    choice = input('\n> ')
    index = int(choice) - 1

    if index == 0:
        start_game()
    elif index == 1:
        help_menu()
    elif index == 2:
        sys.exit()
    elif choice not in [1, 2, 3]:
        title_screen()

#Clears the terminal of previous code.
def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def title_screen():
        clear()
        print('#' * 29)
        print(f'#{bcolors.BOLD + bcolors.HEADER} Tesseract: The War Within {bcolors.ENDC}#')
        print('#' * 29 + '\n')
        print(f"{bcolors.BOLD}       .: (1) Play :.{bcolors.ENDC}")
        print(f"{bcolors.BOLD}       .: (2) Help :.{bcolors.ENDC}")
        print(f"{bcolors.BOLD}       .: (3) Quit :.{bcolors.ENDC}")
        print('\nSelect the corresponding number')
        print('of the menu item & press "Enter."') 
        title_screen_menu()

##### Help Menu #####
def help_menu():
    clear()
    print('               '"#############\n"
        '               'f"# {bcolors.HEADER}Help Menu{bcolors.ENDC} #\n"
        '               '"#############\n")
    print("~" * 45)
    print("Use the number pad or (number row keys) to")
    print("nagivate the levels of the tesseract.\n")
    print("Choose your path by traveling and typing out")
    print("the answer to the riddles in each room.\n")
    print("Making your way through the cube leads you to")
    print("powerful enemies that test your strength")
    print("and skill in battle. Good luck!")
    print("~" * 45 + "\n")
    print(f"{bcolors.BOLD}               .: (1) Play :.{bcolors.ENDC}")
    print(f"{bcolors.BOLD}               .: (2) Quit :.{bcolors.ENDC}")
    print('\n       Select the corresponding number')
    print('       of the menu item & press "Enter."')
    help_screen_menu()

def help_screen_menu():
    choice = input('\n> ')
    index = int(choice) - 1

    if index == 0:
        start_game() 
    elif index == 1:
        sys.exit()
    elif choice not in [1, 2]:
        title_screen()

##### Game Setup #####
player = classes.player
final_boss = classes.final_boss
grunt_list = classes.grunt_list

#This will occur throughout the dialogue code. It allows the string to be typed gradually - like a typewriter.
def typewriter(character):
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.06)

def start_game():
    clear()
            
    #QUESTION NAME: Obtains the player's name.
    def first_question():
        greeting = "Greetings, stranger.\n"
        warmth = "It's nice to see a new face from time to time.\n"
        introduction = "So, who are you? What's your name?\n\n"

        for character in greeting:
            typewriter(character)
        time.sleep(0.4)
        for character in warmth:
            typewriter(character)
        time.sleep(0.8)
        clear()
        for character in introduction:
            typewriter(character) 
        player_name = input(str("> "))
        print("\n")

        confirm = "Are you sure that's it? [Y/N]\n\n"
        for character in confirm:
            typewriter(character)
        answer = input("> ").lower()

        if answer != 'y':
            clear()
            first_question()
        else:
            player.name = player_name

    first_question()

    #QUESTION DESIRE: Obtains the player's class & stats.
    def second_question():
        clear()
        intrigue = f"Well, {player.name}...\n"
        question = "What do you desire?\n\n"

        for character in intrigue:
            typewriter(character)
        time.sleep(0.6)
        for character in question:
            typewriter(character)

        valor = f"1) {bcolors.FAIL}Valor: A rugged body that will endure even the toughest challenges.{bcolors.ENDC}\n\n"
        for character in valor:
            typewriter(character)

        wisdom = f"2) {bcolors.OKBLUE}Wisdom: A sharp mind that will grant you mastery of wondrous power.{bcolors.ENDC}\n\n"
        for character in wisdom:
            typewriter(character)

        balance = f"3) {bcolors.OKGREEN}Balance: A body and mind of both equal merit and equal potential.{bcolors.ENDC}\n\n"
        for character in balance:
            typewriter(character)

        choice = input("> ")
        print("\n")
        index = int(choice) - 1

        if index == 0:
            player.hp = 120
            player.max_hp = 120
            player.mp = 100
            player.max_mp = 100
            player.atk = 16

        elif index == 1:
            player.hp = 90
            player.max_hp = 90
            player.mp = 120
            player.max_mp = 120
            player.mag = 17

        elif index == 2:
            player.hp = 105
            player.max_hp = 105
            player.mp = 110
            player.max_mp = 110
            player.end = 13

        elif choice not in [1, 2, 3]:
            clear()
            second_question()

        confirm = f"Is this what you desire? [Y/N]\n\n"
        for character in confirm:
            typewriter(character)
        answer = input("> ").lower()

        if answer != 'y':
            clear()
            second_question()

        else:
            #Character Confirmation
            power = player.power[index]
            clear()
            combined = (f"So, {player.name} the {power}?\n"
            "Hmm...\n\n")
            final_confirm = f"Is this the power you seek? [Y/N]\n\n"

            for character in combined:
                typewriter(character)
            time.sleep(0.6)
            for character in final_confirm:
                typewriter(character)
            final_answer = input("> ").lower()

            if final_answer != 'y':
                clear()
                first_question()
            else:
                clear()
    
    second_question()

    #Leads the player into the cube puzzle now!
    accept = "Interesting.\n"
    pre_speech = f"It seems this is where we must part, {player.name}.\n\n"
    speech1 = "Before you go, I must tell you that you're in the center of a tesseract.\n"
    speech2 = "Every face inside this cube houses a different, seperate realm from the others.\n"
    speech3 = "I can't say how anyone ever actually makes it here. "
    speech4 = "Nobody really knows.\n\n"
    speech5 = "You're probably thinking about making it out now, aren't you?\n" 
    speech6 = "Well, you would be the first to actually do it."

    for character in accept:
        typewriter(character)
    time.sleep(0.6)
    for character in pre_speech:
        typewriter(character)
    time.sleep(0.6)
    clear()
    for character in speech1:
        typewriter(character)
    time.sleep(0.6)
    for character in speech2:
        typewriter(character)
    time.sleep(0.6)
    for character in speech3:
        typewriter(character)
    time.sleep(0.6)
    for character in speech4:
        typewriter(character)
    time.sleep(0.6)
    for character in speech5:
        typewriter(character)
    time.sleep(0.6)
    for character in speech6:
        typewriter(character)
    time.sleep(1)
    main_game_loop()

##### Game Handling #####
#Makes a border when printed and prints the cube floor information for the player.
def print_location():
    print('#' * (4 +len(player.position)))
    print(f'# {bcolors.HEADER}{player.position.upper()}{bcolors.ENDC} #')
    print('#' * (4 +len(player.position)))

def prompt():
    clear()
    print_location()
    print('\n' + (cube[player.position][DESCRIPTION]))
    if (cube[player.position][REPS]) >= 1:
        (cube[player.position][REPS]) == 1
        player.solves == player.solves
        print(f"{bcolors.BOLD}\nSomething seems different, but nothing's changed here.{bcolors.ENDC}")

    if player.position == "floor" and player.solves == 5:
        print(f"{bcolors.BOLD}\nSomething feels different here, but nothing's changed yet.{bcolors.ENDC}")

    print("\nWhat would you like to do?")
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
    choose_action()

    choice = input(f"{bcolors.UNDERLINE}\nChoose action:{bcolors.ENDC} ")
    index = int(choice) - 1

    if index == 0:
        examine()
    elif index == 1:
        move()
    elif index == 2:
        sys.exit()
    elif choice not in [1, 2, 3]:
        clear()
        prompt()

def choose_action():
    i = 1
    print(f"\n{bcolors.BOLD + bcolors.HEADER}ACTIONS:{bcolors.ENDC}")
    for choice in player.actions:
            print(f"    {bcolors.BOLD}{i}) {choice + bcolors.ENDC}")
            i += 1

def choose_location():
    i = 1
    print(f"\n{bcolors.BOLD + bcolors.HEADER}DIRECTIONS:{bcolors.ENDC}")
    for choice in player.directions:
            print(f"    {bcolors.BOLD}{i}) {choice + bcolors.ENDC}")
            i += 1

def move():
    clear()
    print_location()
    print('\n' + (cube[player.position][DESCRIPTION]))
    print("\nWhere would you like to move to?")
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
    choose_location()

    destination = input(f"{bcolors.UNDERLINE}\nChoose destination:{bcolors.ENDC} ")
    index = int(destination) - 1

    if index == 0:
        move_dest = cube[player.position][SIDE_UP]
        move_player(move_dest)
    elif index == 1:
	    move_dest = cube[player.position][SIDE_LEFT]
	    move_player(move_dest)
    elif index == 2:
	    move_dest = cube[player.position][SIDE_RIGHT]
	    move_player(move_dest)
    elif index == 3:
	    move_dest = cube[player.position][SIDE_DOWN]
	    move_player(move_dest)
    else:
        clear()
        move()

def move_player(move_dest):
	player.position = move_dest

def examine():
    clear()
    print_location()

    if (cube[player.position][REPS]) == 0:
        print('\n' + (cube[player.position][INFO]))
        print((cube[player.position][RIDDLE]))

        if player.position == 'floor':
            print('\n\n(Press "Enter" to continue.)')
        else:
            print('\n\n(Type your answer and press "Enter.")')

        riddle_answer = input("> ").lower()
        checkpuzzle(riddle_answer)

def checkpuzzle(riddle_answer):
    if player.position == 'floor':
        if player.solves == 5:
            clear()
            inquire = f"{bcolors.FAIL}Who dares try to escape {final_boss.name}'s tesseract?!\n"
            reveal = "It was I who summoned you here.\n"
            big_reveal = "It was me who made you "
            anger = f"{bcolors.BOLD}WHO YOU ARE!{bcolors.ENDC}\n"
            cocky = f"{bcolors.FAIL}You think that you have what it takes to break out?\n"
            last_words = f"Good luck.{bcolors.ENDC}\n"

            for character in inquire:
                typewriter(character)
            time.sleep(0.4)
            for character in reveal:
                typewriter(character)
            time.sleep(0.3)
            for character in big_reveal:
                typewriter(character)
            for character in anger:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.08)
            time.sleep(0.1)
            for character in cocky:
                typewriter(character)
            time.sleep(0.2)
            for character in last_words:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.09)
            time.sleep(0.4)

            combat.battle(final_boss)
            if final_boss.hp == 0:
                player.won == True
                endspeech1 = f"{bcolors.BOLD}With the last bastion of evil fading, a massive key emerges from its ashes.\n"
                endspeech2 = "You place it in the large, yet easily overlookable keyhole in the field...\n"
                endspeech3 = "The key begins to rotate on its own and ends with a crisp, satisfying click.\n\n"
                endspeech4 = "All of the sides of the tesseract begin to crumble inward.\n"
                endspeech5 = "The fabric rips between each realm and you see them all at once.\n"
                endspeech6 = "Light shines through the cracked walls. "
                endspeech7 = "A final flash blinds you as the rumbling stops.\n"
                endspeech8 = f"You have escaped!{bcolors.ENDC}"

                clear()
                for character in endspeech1:
                    typewriter(character)
                time.sleep(0.4)
                for character in endspeech2:
                    typewriter(character)
                time.sleep(0.4)
                for character in endspeech3:
                    typewriter(character)
                time.sleep(0.4)
                for character in endspeech4:
                    typewriter(character)
                time.sleep(0.4)
                for character in endspeech5:
                    typewriter(character)
                time.sleep(0.4)
                for character in endspeech6:
                    typewriter(character)
                time.sleep(0.4)
                for character in endspeech7:
                    typewriter(character)
                time.sleep(0.4)
                for character in endspeech8:
                    typewriter(character)
                time.sleep(0.4)
                print(f"{bcolors.BOLD + bcolors.HEADER}\n\nCONGRATULATIONS!{bcolors.ENDC}")
                time.sleep(1)
                sys.exit()
        else:
            choose_action()

    elif riddle_answer in (cube[player.position][ANSWER]):
        (cube[player.position][REPS]) += 1
        player.solves += 1

        clear()
        print(f"{bcolors.BOLD}You have solved the riddle. Onwards!{bcolors.ENDC}")
        print(f"{bcolors.BOLD}\nRiddles solved: {bcolors.ENDC}" + str(player.solves))

        if player.solves == 5:
            print(f"{bcolors.BOLD + bcolors.HEADER}\nWas that a click I just heard? Hmm...{bcolors.ENDC}")
        time.sleep(3)
    else:
        clear()
        print(f"{bcolors.BOLD + bcolors.FAIL}Wrong answer...{bcolors.ENDC}")
        time.sleep(1)
        combat.battle(grunt_list)
            
def main_game_loop():
    while player.won == False:
        prompt()