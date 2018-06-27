list_of_heroes = ["hero1", "hero2"]

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
'''in order to make things faster, this is where 
you should input the heroes in your party, it must be in 
exactly the same format, otherwise it will not work'''

import random


def numeric_ensure(question):
    frustrated = False
    while True:
        try:
            if frustrated:
                response = int(input("I SAID, " + question))
                break
            else:
                response = int(input(question))
                break
        except ValueError:
            frustrated = True
            continue
    return response


'''def total_enclosure(the_phrase):
    length = len(the_phrase)
    print("-"*(length + 4))
    print("| {} |".format(the_phrase))
    print("-"*(length + 4))'''


class Creature:
    def rename(self):
        self.name = input("What is {}'s new name?".format(self.name))

    def reorder(self):
        self.initiative = numeric_ensure("what is {}'s new initiative?"
                                         .format(self.name))


class Enemy(Creature):
    def __init__(self, init_score):
        self.side = "enemy"
        if init_score == 0:
            self.initiative = random.randint(1, 20)
        else:
            self.initiative = init_score
        self.name = input("name for enemy?")
        self.health = numeric_ensure("how much health does {} have"
                                     .format(self.name))

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


class Hero(Creature):
    def __init__(self, name, is_new):
        self.side = "hero"
        if is_new:
            self.name = input("what is the name of this hero?")
        else:
            self.name = name
        if is_new:
            self.initiative = 42
        else:
            self.initiative = numeric_ensure("what is {}'s initiative?".format(self.name))

    def __sub__(self, other):
        print("that is not a valid command for this character")


def display_initiative(order):
    init_order = 1
    print()
    first_time = True
    for creature in order:
        if creature.side == "hero":
            print("{2}- {0} with initiative of {1}".format(creature.name, creature.initiative, init_order))
        else:
            print("{3}- {0} with initiative of {1} and {2} health"
                  .format(creature.name, creature.initiative, creature.health, init_order))
        if first_time:
            print("<>" * 18)
            first_time = False
        init_order += 1
    print()


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j].initiative < arr[j + 1].initiative:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    display_initiative(arr)


def new_creature(initiative):
    hero_villain = input("are they heroes 'h' or villains 'v'?")
    is_good = True
    while not hero_villain == "h" and not hero_villain == "v":
        hero_villain = input("I SAID is it a hero 'h' or villain 'v'?")
    if hero_villain == "v":
        number_of_creatures = numeric_ensure("now many villains are joining the fight")
        is_good = False
    if hero_villain == "h":
        number_of_creatures = numeric_ensure("now many heroes are joining the fight")

    for _ in range(number_of_creatures):
        initiative.insert(0, create_creature(is_good, initiative))
    display_initiative(initiative)


def create_creature(char_good, le_list):
    if char_good:
        return Hero("", char_good)
    else:
        return Enemy(le_list[0].initiative+1)


def kill_creature(the_order):
    display_initiative(the_order)
    who_died = numeric_ensure("which character died?") - 1
    print("\n", the_order[who_died].name, "has fallen\n")
    del the_order[who_died]
    display_initiative(the_order)


def damage_creature(the_list):
    see_enemies(the_list)
    who_damaged = numeric_ensure("which monster is being damaged") - 1
    damage_amount = numeric_ensure("how much damage is being inflicted to {}?"
                                   .format(the_list[who_damaged].name))
    is_dead = the_list[who_damaged] - damage_amount
    if is_dead:
        del the_list[who_damaged]
        display_initiative(the_list)
        return 1
    else:
        return 0


def see_enemies(booba_list):
    init_track = 1
    for booba in booba_list:
        if booba.side == "hero":
            init_track += 1
        else:
            print("{}- {} with {} health"
                  .format(init_track, booba.name, booba.health))
            init_track += 1


def starting_part(the_big_list, heroes):
    for hero in heroes:
        new_hero = Hero(hero, False)
        the_big_list.append(new_hero)

    for i in range(numeric_ensure("how many enemies?")):
        new_orc = Enemy(0)
        the_big_list.append(new_orc)

    print("Round: 1")
    bubble_sort(the_big_list)


def cycle_initiative(initiative):
    temp = initiative[0]
    list_temp = initiative[1:]
    list_temp.append(temp)
    return list_temp


def backwards(combat_order):
    saved_val = combat_order[-1]
    del combat_order[-1]
    combat_order.insert(0, saved_val)
    display_initiative(combat_order)


def change_name(combat_list):
    who_name_change = index_input("whose name needs to be corrected?", combat_list)
    combat_list[who_name_change].rename()
    display_initiative(combat_list)


def round_counting(current_round, till_new_round, big_ol_list, many_slain):
    till_new_round -= 1
    till_new_round -= many_slain
    if till_new_round <= 0:
        current_round += 1
        till_new_round = len(big_ol_list)
    print("Round:", current_round)
    display_initiative(big_ol_list)
    return current_round, till_new_round


def see_commands():
    print("""
'view' -- to see the current order 
hit return -- to cycle to the next person's turn
'quit' -- to exit out of the program
'c+' -- to add a new creature(at current place)
'c-' -- to remove a creature from the combat
'reorder' -- to sort all creatures
' ' -- to deal damage to an enemy
'rename' -- to change a creatures name
'initiative' -- to change a creatures initiative""")


def index_input(question, grandiose_list):
    display_initiative(grandiose_list)
    answer = numeric_ensure(question) - 1
    return answer


def main(all_the_heroes):
    grand_list = []
    starting_part(grand_list, all_the_heroes)
    round_count = 1
    switches = len(grand_list)
    choice = ""
    slain_creatures = 0

    while choice != "quit":
        choice = input("enter a command, type 'help' if unsure ")
        if choice == "":
            grand_list = cycle_initiative(grand_list)
            round_count, switches = round_counting\
                (round_count, switches, grand_list, slain_creatures)
            slain_creatures = 0
        elif choice == "quit":
            break
        elif choice == "view":
            display_initiative(grand_list)
        elif choice == "c+":
            new_creature(grand_list)
        elif choice == "reorder":
            bubble_sort(grand_list)
        elif choice == "c-":
            kill_creature(grand_list)
            slain_creatures += 1
        elif choice == " ":
            slain_creatures += damage_creature(grand_list)
        elif choice == "rename":
            change_name(grand_list)
        elif choice == "help":
            see_commands()
        elif choice == "back":#THIS IS GOING TO NEED A LOT OF WORK
            print("please note that this is still in construction and does not work")
            backwards(grand_list)
            round_count, switches = round_counting\
                (round_count, switches, grand_list, slain_creatures)
        elif choice == "initiative":
            grand_list[index_input("whose initiative should change?", grand_list)].reorder()
        else:
            print("that command is not familiar to me, try again")


main(list_of_heroes)
