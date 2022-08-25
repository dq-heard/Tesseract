##### Text Customization #####
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

##### Character Setup #####
class Person:
    def __init__(self, name, hp, mp, atk, end, mag, skills, items):
        self.name = name
        self.position = 'floor'
        self.won = False
        self.solves = 0
        self.actions = ['Search','Travel', 'Quit']
        self.directions = ['Up', 'Left', 'Right', 'Down']
        ##### Starting Stats #####
        self.desire = ['Valor', 'Wisdom', 'Balance']
        self.power = ['Warrior', 'Mystic', 'Guardian']
        ##### Combat #####
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp
        self.atk = atk
        self.end = end
        self.mag = mag
        self.skills = skills
        self.items = items
        self.commands = ['Attack', 'Skills', 'Items']

##### Skill Setup #####
class Skill:
    def __init__(self, name, cost, color):
        self.name = name
        self.cost = cost
        self.color = color

##### Item Setup #####
class Item:
    def __init__(self, name, desc, value):
        self.name = name
        self.desc = desc
        self.value = value

##### Skill Instatiation #####
fire = Skill("Fire", 4, "black")
thunder = Skill("Thunder", 4, "black")
ice = Skill("Blizzard", 4, "black")
cure = Skill("Cure", 4, "white")
earth = Skill("Quake", 4, "black")
flare = Skill("Flare", 27, "black")
meteor = Skill("Meteor", 45, "black")

#Movesets
boss_skills = [earth, flare, meteor]
chimera_skills = [fire, thunder, ice]
player_skills = [fire, thunder, ice, cure]

##### Item Instatiation #####
potion = Item("Potion", "Heals 100 HP.", 100)
ether = Item("Ether", "Restores 100 MP.", 100)
grenade = Item("Grenade", "Deals 20 damage.", 20)

player_items = [{"name": potion, "quantity": 3}, {"name": ether, "quantity": 1}, {"name": grenade, "quantity": 5}]

##### Character Instantiation #####
player = Person('', 100, 100, 11, 8, 12, player_skills, player_items)
final_boss = Person("Agathor", 200, 200, 26, 0, 20, boss_skills, [])

grunt_list = [
    Person("Wolf", 40, 24, 18, 0, 14, [ice], []),
    Person("Goblin", 50, 24, 19, 0, 14, [fire], []),
    Person("Basilisk", 60, 24, 20, 0, 15, [thunder], []),
    Person("Chimera", 70, 24, 22, 0, 18, chimera_skills, []),
    Person("Golem", 80, 24, 24, 0, 18, [earth], [])
]