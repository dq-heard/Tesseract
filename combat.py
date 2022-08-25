import classes
import game
import random
import time

bcolors = classes.bcolors

##### Combat System #####
player = classes.player
final_boss = classes.final_boss
grunt_list = classes.grunt_list

def enemy_action(self):
    options = random.randint(0, 1)
    return options

def generate_damage(self):
    rand = random.randint(-5, 5)
    dmg = self.atk + rand
    return dmg
    
def generate_skill_damage(self):
    rand = random.randint(-5, 5)
    dmg = self.mag + rand
    return dmg

def take_damage(self, dmg):
    self.hp -= dmg - self.end

    if self.hp < 0:
        self.hp = 0
    return self.hp

def restore_hp(self, dmg):
    self.hp += dmg

    if self.hp > self.max_hp:
        self.hp = self.max_hp

def restore_mp(self, dmg):
    self.mp += dmg

    if self.mp > self.max_mp:
        self.mp = self.max_mp

def reduce_mp(self, cost):
    self.mp -= cost

def choose_command(self):
    i = 1

    print(f"\n{bcolors.BOLD}COMMANDS:{bcolors.ENDC}")
    for choice in player.commands:
        print(f"    {bcolors.BOLD}{i}) {choice + bcolors.ENDC}")
        i += 1

def choose_skills(self):
    i = 1

    print(f"{bcolors.BOLD + bcolors.OKBLUE}SKILLS:{bcolors.ENDC}")
    for skill in player.skills:
        print(f"    {bcolors.BOLD}{i}) {skill.name} (Cost: {skill.cost}){bcolors.ENDC}")
        i += 1

def choose_item(self):
    i = 1

    print(f"{bcolors.BOLD + bcolors.WARNING}ITEMS:{bcolors.ENDC}")
    for item in player.items:
        print(f"    {bcolors.BOLD}{i}) {item['name'].name}: {item['name'].desc} "
                f"(x {item['quantity']}){bcolors.ENDC}")
        i += 1

def player_stats():
    hp_bar = ""
    hp_stat = (player.hp / player.max_hp) * 100 / 4

    mp_bar = ""
    mp_stat = (player.mp / player.max_mp) * 100 / 10

    while hp_stat > 0:
        hp_bar += "█"
        hp_stat -= 1

    while len(hp_bar) < 25:
        hp_bar += " "

    while mp_stat > 0:
        mp_bar += "█"
        mp_stat -= 1

    while len(mp_bar) < 10:
        mp_bar += " "

    hp_string = f" {player.hp}/{player.max_hp}"
    mp_string = f" {player.mp}/{player.max_mp}"

    while len(hp_string) < 12:
        hp_string += " "

    print(" " * len(player.name) + f"  {bcolors.BOLD}HP{hp_string}              MP{mp_string + bcolors.ENDC}")
    print(f"{bcolors.BOLD + player.name + bcolors.ENDC} |{bcolors.OKGREEN + hp_bar + bcolors.ENDC}|"
            f" |{bcolors.OKBLUE + mp_bar + bcolors.ENDC}|")

def enemy_stats(enemy):
    hp_bar = ""
    hp_stat = (enemy.hp / enemy.max_hp) * 100 / 2

    while hp_stat > 0:
        hp_bar += "█"
        hp_stat -= 1

    while len(hp_bar) < 50:
        hp_bar += " "

    hp_string = f" {enemy.hp}/{enemy.max_hp} "

    print(f" {bcolors.BOLD + enemy.name}'s HP{hp_string + bcolors.ENDC}")
    print(f"|{bcolors.FAIL + hp_bar + bcolors.ENDC}|\n")

def battle(enemies):
    enemy_party = []
    start = random.randint(0, 3)
    running = True
    i = 0

    #Enemy Setup
    if enemies == grunt_list:
        grunt = random.randrange(0, len(grunt_list))
        enemy_party.append(grunt_list[grunt])
        enemy = enemy_party[0]
    
    elif enemies == final_boss:
        enemy_party.append(final_boss)
        enemy = enemy_party[0]
        
    ##### Battle Phases #####
    if start == 0 or enemies == final_boss:
        game.clear()
        enemy_dmg = generate_damage(enemy)
        take_damage(player, enemy_dmg)

        if enemies == grunt_list:
            print(f"{bcolors.BOLD + bcolors.FAIL}The {enemy.name} ambushed you!\n"
                f"{bcolors.ENDC}")
        else:
            print(f"{bcolors.BOLD + bcolors.FAIL + enemy.name} ambushed you!\n"
                f"{bcolors.ENDC}")
    else:
        game.clear()
        print(f"{bcolors.BOLD + bcolors.HEADER}First Strike!\n{bcolors.ENDC}")

    enemy_stats(enemy)
    print("\n")
    player_stats()
        
    while running:
        print("==========================================================================\n")
        #Player KO Check Between Turns
        if player.hp == 0:
            game.clear()
            print(f"{bcolors.BOLD + bcolors.FAIL + player.name} has fallen.{bcolors.ENDC}\n")
            print(f"{bcolors.BOLD + bcolors.FAIL}Game Over...{bcolors.ENDC}")

            running = False
            sys.exit()
        else:
            #Command Menu
            choose_command(player)

        choice = input(f"{bcolors.UNDERLINE}\nChoose action:{bcolors.ENDC} ")
        index = int(choice) - 1

        #Player Attack
        if index == 0:
            game.clear()
            player_dmg = generate_damage(player)
            take_damage(enemy, player_dmg)

            if enemies == grunt_list:
                print(f"{bcolors.BOLD + player.name} attacked the {enemy.name}.{bcolors.ENDC}\n")
            else:
                print(f"{bcolors.BOLD + player.name} attacked {enemy.name}.{bcolors.ENDC}\n")
            enemy_stats(enemy)
            print("\n")

        #Player Skills
        elif index == 1:
            print("\n------------------------------------------------------------------------\n")
            choose_skills(player)
            skill_choice = int(input(f"\n{bcolors.UNDERLINE}Choose skill:{bcolors.ENDC} ")) - 1

            skill = player.skills[skill_choice]
            current_mp = player.mp

            #No Negative MP
            if current_mp < skill.cost:
                game.clear()
                current_mp == player.mp
                print(f"{bcolors.BOLD + bcolors.FAIL}Not enough MP.{bcolors.ENDC}\n")
            else:
                reduce_mp(player, skill.cost)

                #Player White Skills
                if skill.color == "white":
                    game.clear()

                    #Restorative Skills
                    if skill.name == "Cure":
                        heal_dmg = generate_skill_damage(player)
                        restore_hp(player, heal_dmg * 3)

                        print(f"{bcolors.BOLD + bcolors.OKGREEN + skill.name} restored {player.name}'s HP.{bcolors.ENDC}\n")   
                        player_stats()
                        print("\n")

                #Player Black Skills
                elif skill.color == "black":
                    game.clear()
                    magic_dmg = generate_skill_damage(player)
                    take_damage(enemy, magic_dmg)

                    if enemies == grunt_list:
                        print(f"{bcolors.BOLD + bcolors.OKBLUE + player.name} used {skill.name} on the {enemy.name}.\n"
                                f"{bcolors.ENDC}")
                    else:
                        print(f"{bcolors.BOLD + bcolors.OKBLUE + player.name} used {skill.name} on {enemy.name}.\n"
                                f"{bcolors.ENDC}")
                    enemy_stats(enemy)
                    print("\n")

        #Player Item
        elif index == 2:
            print("\n------------------------------------------------------------------------\n")
            choose_item(player)

            item_choice = int(input(f"\n{bcolors.UNDERLINE}Choose item:{bcolors.ENDC} ")) - 1
            item = player.items[item_choice]["name"]

            #Out of Stock Check
            if player.items[item_choice]["quantity"] == 0:
                game.clear()
                print(f"{bcolors.BOLD + bcolors.FAIL}No more {item.name}s.{bcolors.ENDC}\n")
            else:
                player.items[item_choice]["quantity"] -= 1

                #Attack Items
                if item.name == "Grenade":
                    game.clear()
                    item_dmg = take_damage(enemy, item.value)

                    if enemies == grunt_list:
                        print(f"{bcolors.BOLD + player.name} used {bcolors.WARNING + item.name + bcolors.ENDC}"
                                f"{bcolors.BOLD} on the {enemy.name + bcolors.ENDC}.\n")
                    else:
                        print(f"{bcolors.BOLD + player.name} used {bcolors.WARNING + item.name + bcolors.ENDC}"
                                f"{bcolors.BOLD} on {enemy.name + bcolors.ENDC}.\n")
                    enemy_stats(enemy)
                    print("\n")

                #Restorative Items
                else:
                    if item.name == "Potion":
                        game.clear()
                        restore_hp(player, item.value)
                        print(f"{bcolors.BOLD + bcolors.OKGREEN + item.name} restored {item.value} "
                            f"of {player.name}'s HP.{bcolors.ENDC}\n")

                    elif item.name == "Ether":
                        game.clear()
                        restore_mp(player, item.value)
                        print(f"{bcolors.BOLD + bcolors.OKGREEN + item.name} restored {item.value} "
                            f"of {player.name}'s MP.{bcolors.ENDC}\n")
                    player_stats()
                    print("\n")
        else:
            game.clear()
            choose_command(player)

        #Enemy KO Check Between Turns
        if enemy.hp == 0:
            game.clear()
            print(f"{bcolors.BOLD + bcolors.OKGREEN}Victory!{bcolors.ENDC}")
            time.sleep(1)
            running = False
        else:
            choice = enemy_action(enemy)  

        #Enemy Attack
        if choice == 0:
            enemy_dmg = generate_damage(enemy)
            enemy_attack = take_damage(player, enemy_dmg)

            if enemies == grunt_list:
                print(f"{bcolors.BOLD + bcolors.FAIL}The {enemy.name} attacked you.{bcolors.ENDC}\n")
            else:
                print(f"{bcolors.BOLD + bcolors.FAIL + enemy.name} attacked you.{bcolors.ENDC}\n")
            player_stats()

        #Enemy Skills
        elif choice == 1:
            if len(enemy.skills) == 0:
                skill = enemy.skills[0]
            else:
                skill_choice = random.randrange(0, len(enemy.skills))
                skill = enemy.skills[skill_choice]

            skill_dmg = generate_skill_damage(enemy)
            mp_left = enemy.mp

            #Enemy MP Check
            if mp_left >= skill.cost:
                reduce_mp(enemy, skill.cost)

                #Enemy Black Magic
                if enemies == grunt_list and skill.color == "black":
                    take_damage(player, skill_dmg * 2)

                    #Special Grunt Skills
                    if enemy.name == "Wolf":
                        print(f"{bcolors.BOLD + bcolors.FAIL}The {enemy.name} howls and sends chills down your spine!\n"
                            f"{bcolors.ENDC}")

                    elif enemy.name == "Goblin":
                        print(f"{bcolors.BOLD + bcolors.FAIL}The {enemy.name} summons a fireball and throws it at you!\n"
                            f"{bcolors.ENDC}")

                    elif enemy.name == "Basilisk":
                        print(f"{bcolors.BOLD + bcolors.FAIL}The {enemy.name} closes in quick and strikes like lightning!\n"
                            f"{bcolors.ENDC}")

                    elif enemy.name == "Golem":
                        print(f"{bcolors.BOLD + bcolors.FAIL}The {enemy.name} swings and crushes the ground below you!\n"
                            f"{bcolors.ENDC}")

                    elif enemy.name == "Chimera":
                        print(f"{bcolors.BOLD + bcolors.FAIL}The {enemy.name} used {skill.name} on you.{bcolors.ENDC}\n")
                    player_stats()
                    
                #Boss HP/MP Restoration
                elif enemies == final_boss:
                    heal = random.randint(0, 1)
                    hp_pct = enemy.hp / enemy.max_hp * 100
                    mp_pct = enemy.mp / enemy.max_mp * 100

                    if heal == 0 and hp_pct < 40:
                        restore_hp(enemy, skill_dmg * 2)
                        print(f"{bcolors.BOLD + bcolors.FAIL + enemy.name} fortified and regained his health!{bcolors.ENDC}\n")
                        enemy_stats(enemy)

                    elif heal == 0 and mp_pct < 50:
                        restore_mp(enemy, skill_dmg * 2)
                        print(f"{bcolors.BOLD + bcolors.FAIL + enemy.name} focused and charged his mana!{bcolors.ENDC}\n")
                        player_stats()

                    else:
                        take_damage(player, skill_dmg)
                        print(f"{bcolors.BOLD + bcolors.FAIL + enemy.name} used {skill.name} on you.\n"
                                f"{bcolors.ENDC}")
                        player_stats()

            #Enemy Skill Fallthrough
            elif mp_left < skill.cost:
                enemy_dmg = generate_damage(enemy)
                enemy_attack = take_damage(player, enemy_dmg)

                if enemies == grunt_list:
                    print(f"{bcolors.BOLD + bcolors.FAIL}The {enemy.name} attacked you.{bcolors.ENDC}\n")
                else:
                    print(f"{bcolors.BOLD + bcolors.FAIL + enemy.name} attacked you.{bcolors.ENDC}\n")
                player_stats()