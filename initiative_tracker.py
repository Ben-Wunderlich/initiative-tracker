import random
from matrixing import string_sorter, main as full_query
import player_name_changer as default_changer
from num_ensure import formula_ensure, integer_ensure


# note this is modified so if given "main" it will return main
# otherwise it will always return a number from the user


def make_hero_file():
    file2 = open("hero names.txt", "w")
    file2.write("hero1, hero2")
    file2.close()
    print("file for names of heroes created")


class Creature:
    def rename(self, grand_list):
        self.name = make_name_full("What is {}'s new name?".format(self.name), grand_list)

    def reorder(self):
        self.initiative = integer_ensure("what is {}'s new initiative? (currently {}) "
                                         .format(self.name, self.initiative))
        print("\n{}'s initiative is now {}\n".format(self.name, self.initiative))


class Enemy(Creature):
    def __init__(self, init_score, grand_list, name=None, health=None):
        self.side = "enemy"
        self.has_reaction = True
        if name is None:
            self.name = make_name_full("name for enemy?", grand_list)
        else:
            self.name = name
        if init_score == 0:
            self.initiative = random.randint(1, 20)
        else:
            self.initiative = init_score
        if health is None:
            self.health = formula_ensure("how much health does {} have?"
                                     .format(self.name))
        else:
            self.health = health

    def __str__(self):
        return "- {} with initiative of {} and {} health"\
            .format(self.name, self.initiative, self.health)

    def __sub__(self, other):
        self.health -= other
        print()
        if self.health <= 0:
            print(self.name, "is dead with {} health".format(self.health))
            print()
            return True
        else:
            print(self.name, "now has {} health".format(self.health))
            print()
            return False

    def use_reaction(self):
        if self.has_reaction:
            self.has_reaction = False
            print(self.name, "\nhas used it's reaction\n")
        else:
            print("\n", self.name, "does not have it's reaction to use\n")

    def adjust_health(self):
        print("{} currently has {} health".format(self.name, self.health), end=" ")
        new_health_amount = formula_ensure("how much health does {} now have"
                                           .format(self.name))
        self.health = new_health_amount


class Hero(Creature):
    def __init__(self, name, is_new, grand_list):
        self.side = "hero"
        if is_new:
            self.name = make_name_full("what is the name of this hero?", grand_list)
        else:
            self.name = name
        if is_new:
            self.initiative = 42
        else:
            self.initiative = integer_ensure("what is {}'s initiative?".format(self.name))

    def __sub__(self, other):
        print("that is not a valid command for this character")

    def __str__(self):
        result = "- {} with initiative of {}".format(self.name, self.initiative)
        return result

    @staticmethod
    def use_reaction():
        print("it is the player's job to keep track of their reactions")

    @staticmethod
    def adjust_health():
        print("it is the players job to keep track of their health")


# returns name that is valid
def make_name_full(question, grand_list):
    taken_names = []
    for combatant in grand_list:
        taken_names.append(combatant.name)
        taken_names.extend([" ", ""])
    name = input(question)
    while name in taken_names:
        name = input("Not a valid name, give another name")
    return name


# shows the full initiative with one greater than their index
def display_initiative(grand_list, curr_round=None):
    init_order = 1
    print()
    if curr_round is not None:
        show_round(curr_round)
    first_time = True
    for creature in grand_list:
        print(init_order, creature, sep="")
        if first_time:
            print("<>" * 18)
            first_time = False
        init_order += 1
    print()


# for sorting the list by intiative from high to low
def bubble_sort(gr_li):
    n = len(gr_li)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if gr_li[j].initiative < gr_li[j + 1].initiative:
                gr_li[j], gr_li[j + 1] = gr_li[j + 1], gr_li[j]
                swapped = True
        if not swapped:
            break
    display_initiative(gr_li)


# for manual creation of new creatures once running
def new_creature(grand_list):
    is_good = True
    while True:
        hero_villain = input("are they heroes 'h' or villains 'v' or group 'vg?")
        if hero_villain == "h":
            number_of_creatures = integer_ensure("now many heroes are joining the fight?")
            break
        elif hero_villain == "v":
            is_good = False
            number_of_creatures = integer_ensure("how many villains are joining the fight?")
            break
        elif hero_villain == "vg":
            number_of_creatures = integer_ensure("how many minions are joining the fight?")
            base_name = make_name_full("what is the base name", grand_list)
            amount_of_health = formula_ensure("how much health do {}'s have"
                                              .format(base_name))
            is_good = False
            break
        else:
            print("that does not work")

    i = 1
    for _ in range(number_of_creatures):
        if is_good:
            grand_list.insert(0, Hero("", True, grand_list))
        elif hero_villain == "v":
            grand_list.insert(0, Enemy(grand_list[0].initiative + 1, grand_list))
        else:  # this is if hero_villain == "vg
            current_name = base_name + str(i)
            grand_list.insert(0, Enemy
    (grand_list[0].initiative + 1, grand_list, current_name, amount_of_health))

            i += 1
    display_initiative(grand_list)


# instantly removes a creature from the main list
def kill_creature(the_order, curr_round):
    who_died = index_input("which character died?", the_order)
    if who_died == "main":
        return "main"
    print("\n", the_order[who_died].name, "has left the fray\n")
    del the_order[who_died]

    display_initiative(the_order, curr_round)


# allows you to damage an enemy, if their health <= 0 they are removed
def damage_creature(the_list, curr_round):
    see_enemies(the_list)
    print()
    who_damaged = index_input("which monster is being damaged? ", the_list, False)
    if who_damaged == "main":
        return "main"
    while the_list[who_damaged].side == "hero":
        print("it is up to a player to track their own health, pick again")
        who_damaged = index_input("which monster is being damaged? ", the_list, False)
        if who_damaged == "main":
            return "main"

    if who_damaged == "main":
        return "main"
    damage_amount = formula_ensure("how much damage is being inflicted to {}?"
                                   .format(the_list[who_damaged].name))
    #damage_amount = int(damage_amount + 0.5) # rounds it

    is_dead = the_list[who_damaged] - damage_amount
    if is_dead:
        del the_list[who_damaged]
        display_initiative(the_list, curr_round)
        return 1
    else:
        return 0


# shows you list of enemies with one greater than their index
def see_enemies(grand_list):
    init_track = 1
    for creature in grand_list:
        if creature.side == "enemy":
            print(init_track, creature, sep="")
        init_track += 1


# initializes list with heroes and enemies
def starting_part(grand_list, heroes):
    for hero in heroes:
        new_hero = Hero(hero, False, grand_list)
        grand_list.append(new_hero)

    enemy_amount = integer_ensure("how many enemies?")
    if enemy_amount <= 0:
        print("Round: 1")
        bubble_sort(grand_list)
        return

    naming_count = 1
    if enemy_amount != 1:
        is_a_group = input("is there a group of minions? y/n") == "y"
    else:
        is_a_group = False

    if is_a_group:
        many_in_group = integer_ensure("out of the {}, how many are minions?"
                                       .format(enemy_amount))
        base_name = make_name_full\
            ("what is the base name for the minions", grand_list)
        health_amount = formula_ensure("how much health do the {}'s have?"
                                       .format(base_name))

    for _ in range(enemy_amount):
        if is_a_group and many_in_group > 0:
            many_in_group -= 1
            current_name = base_name + str(naming_count)
            naming_count += 1
            new_enemy = Enemy(0, grand_list, current_name, health_amount)
            grand_list.append(new_enemy)
        else:
            new_enemy = Enemy(0, grand_list) # 0 indicates it should be randomized
            grand_list.append(new_enemy)
    print("Round: 1")
    bubble_sort(grand_list)


# puts first value to the end
def cycle_initiative(grand_list):
    temp = grand_list[0]
    list_temp = grand_list[1:]
    list_temp.append(temp)
    return list_temp


# changes name of any creature
def change_name(grand_list):
    who_name_change = index_input("whose name needs to be corrected?", grand_list)
    if who_name_change == "main":
        return "main"
    grand_list[who_name_change].rename(grand_list)
    display_initiative(grand_list)


# advances and keeps track of how many turns have progressed
def round_counting(current_round, till_new_round, grand_list, many_slain):
    is_new_round = False

    till_new_round -= 1
    till_new_round -= many_slain
    if till_new_round <= 0:
        is_new_round = True
        current_round += 1
        till_new_round = len(grand_list)
    display_initiative(grand_list, current_round)
    return current_round, till_new_round, is_new_round


# shows all available commands
def see_commands():
    print("""
      'view' -- see the current order 
      return -- cycle to the next creature's turn
        'c+' -- add a new creature(at current place)
        'c-' -- remove a creature from the combat
       'ord' -- sort all creatures by initiative
' ' or 'dmg' -- deal damage to an enemy
      'name' -- change a creatures name
      'init' -- change a creatures initiative
       'rxn' -- use a monsters reaction
      'turn' -- manually select whose turn it is
      'roll' -- roll dice of any type and amount
     'guide' -- guide to using the dice rolling feature
      'main' -- go back to main menu/exit current process
        'hp' -- manually set a creatures health
   'default' -- change default hero names
      'quit' -- exit out of the program
     'reset' -- resets the program
""")


# returns index of creature displayed
def index_input(question, grand_list, show_init=True):
    if show_init:
        display_initiative(grand_list)
    answer = -1
    # -1 is an arbitrary number
    #  that will make the loop run at least once
    while answer > len(grand_list) or answer < 1:
        answer = input(question)
        if answer == "main":
            return "main"
        else:
            answer = integer_ensure(question, answer)
    answer -= 1
    return answer


# makes has_reactions true for each creature
def give_reactions_back(grand_list):
    for creature in grand_list:
        if creature.side == "enemy":
            creature.has_reaction = True


# expends the reaction for one monster
def use_reaction(grand_list):
    see_enemies(grand_list)
    inp = index_input("which enemy uses their reaction?", grand_list, False)
    grand_list[inp].use_reaction()


# jumps to anyone's turn manually
def turn_selector(grand_list):
    chosen_creature = index_input("which creatures turn do you want it to be?",
                                  grand_list)
    chosen_name = grand_list[chosen_creature].name
    while grand_list[0].name != chosen_name:
        grand_list = cycle_initiative(grand_list)
    display_initiative(grand_list)
    return grand_list


# prints what round it currently is
def show_round(curr_round):
    print("Round:", curr_round)


# shows how to use the dice roller
def dice_guide():
    print('''the form for dice rolling is as follows, 
     the number before the "d" is the number of dice and the number
     after the "d" is the type of die to be rolled.
     
     so 4d6 is four six sided dice, you can add or subtract any number
     of these as well as single numbers, so 3d6 - 2d5 + 6 - 9d28 is
     a possible roll''')


# rolls the dice
def dice_rolling():
    total_statement = "\nYour roll total is: "
    query = "select which dice you want to roll(1d4 form), 'main' to go back"
    die_roll = None
    while die_roll != "main":
        die_roll = input(query)
        if die_roll == "main":
            continue
        elif die_roll == "full":
            print()
            full_query()
            break
        print(total_statement, string_sorter(die_roll, False), "\n")


def change_health(grand_list):
    see_enemies(grand_list)
    which_enemy = index_input("which enemy's health is changing?",
                              grand_list, False)
    grand_list[which_enemy].adjust_health()
    print("{} now has {} health".
          format(grand_list[which_enemy].name,
                 grand_list[which_enemy].health))


def main(all_the_heroes):
    grand_list = []
    curr_round = 1
    starting_part(grand_list, all_the_heroes)
    switches = len(grand_list)
    choice = ""
    slain_creatures = 0

    while choice != "quit":
        choice = input("enter a command, type 'help' if unsure ")
        if choice == "":
            grand_list = cycle_initiative(grand_list)
            curr_round, switches, is_new_round = round_counting\
                (curr_round, switches, grand_list, slain_creatures)
            slain_creatures = 0
            if is_new_round:
                give_reactions_back(grand_list)

        elif choice == "quit":
            break
        elif choice == "view":
            display_initiative(grand_list, curr_round)
        elif choice == "c+":
            new_creature(grand_list)
        elif choice == "ord":
            bubble_sort(grand_list)
        elif choice == "c-":
            kill_creature(grand_list, curr_round)
            slain_creatures += 1
        elif choice == " " or choice == "dmg":
            fatalities = damage_creature(grand_list, curr_round)
            if fatalities == "main":
                continue
            slain_creatures += fatalities
        elif choice == "name":
            change_name(grand_list)
        elif choice == "help":
            see_commands()
        elif choice == "init":
            to_be_changed = index_input("whose initiative should change?", grand_list)
            if to_be_changed == "main":
                continue
            grand_list[to_be_changed].reorder()
            display_initiative(grand_list, curr_round)
        elif choice == "reset":
            main(list_of_heroes)
            return
        elif choice == "rxn":
            use_reaction(grand_list)
        elif choice == "turn":
            grand_list = turn_selector(grand_list)
        elif choice == "roll":
            dice_rolling()
            display_initiative(grand_list, curr_round)
        elif choice == "guide":
            dice_guide()
        elif choice == "hp":
            change_health(grand_list)
        elif choice == "main":
            print("you are currently in the main menu")
            display_initiative(grand_list, curr_round)
            continue
        elif choice == "default":
            default_changer.main()
        else:
            print("that command is not familiar to me, try again")


def define_heroes():
    try:
        file = open("hero names.txt", "r")
    except IOError as e:
        print(e)
        print("file: hero names.txt not found, creating file")
        make_hero_file()
        file = open("hero names.txt", "r")
    list_of_heroes1 = file.read()
    file.close()
    list_of_heroes1 = list(list_of_heroes1.split(", "))

    heroes_to_remove = []
    for hero in list_of_heroes1:
        if hero[0] == "#":
            heroes_to_remove.append(hero)

    for person in heroes_to_remove:
        list_of_heroes1.remove(person)

    return list_of_heroes1


list_of_heroes = define_heroes()

main(list_of_heroes)
