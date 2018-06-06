import random

#this is a change
def display_characters():
    global grand_list
    for j in range(len(grand_list)):
        print(j, grand_list[j][1])


def make_hero():
    name_plz = input("what is the name of this hero?")
    initiative = input("what is there initiative roll?")
    while initiative.isnumeric() == False:
        initiative = input("NO! what is their initiative roll?")
    initiative = int(initiative)
    return [initiative, name_plz]


def make_villain():
    name_plz = input("what is their name? ")
    health_plz = numeric_ensure("how much health do they have?")
    return [random.randint(1, 20), name_plz, int(health_plz)]


def destroy_enemy(the_indx):
    global grand_list
    del grand_list[the_indx]


def numeric_ensure(question):
    frustrated = False
    while True:
        try:
            if frustrated:
                varia = int(input("I SAID, " + question))
                break
            else:
                varia = int(input(question))
                break
        except ValueError:
            frustrated = True
            continue
    return varia


grand_list = []
number_of_enemies = numeric_ensure("how many enemies are there?")
for _ in range(int(number_of_enemies)):
    grand_list.append(make_villain())

num_of_heroes = numeric_ensure("how many heroes are there?")

for _ in range(num_of_heroes):
    grand_list.append(make_hero())
grand_list.sort()
grand_list.reverse()
print(grand_list)
print("\nit is {0}'s turn to fight!\n".format(grand_list[0][1]))

while True:

    what_now = input(
        "type '' to go to next, 'c-' to get rid of creature, "
        "'c+' to add one, 'dmg' to subtract damage, 'ord' to see order, 'quit'")
    if what_now == "":
        temp = grand_list[0]
        grand_list = grand_list[1:]
        grand_list.append(temp)
        print("\nit is {0}'s turn to fight!\n".format(grand_list[0][1]))

    elif what_now == "quit":
        break

    elif what_now == "ord":
        display_characters()
        continue

    elif what_now == "c-":
        display_characters()
        who_died = numeric_ensure("which character died?")
        print(grand_list[who_died][1], "has fallen")
        destroy_enemy(who_died)

    elif what_now == "c+":
        hero_villain = input("is it a hero 'h' or villain 'v'?")
        while not hero_villain == "h" and not hero_villain == "v":
            hero_villain = input("I SAID is it a hero 'h' or villain 'v'?")
        if hero_villain == "h":
            new_creature = make_hero()
        if hero_villain == "v":
            new_creature = make_villain()
        #creature_list = [new_creature]
        #print(creature_list)
        grand_list.insert(0, new_creature)
        print("\nit is {0}'s turn to fight!\n".format(grand_list[0][1]))


    elif what_now == "dmg":
        display_characters()
        while True:
            try:
                dmg_choice = numeric_ensure("who is being damaged?")
                # CHECK HOW MANY ARGUMENTS
                dmg_amount = numeric_ensure("how much damage is being done?")
                grand_list[dmg_choice][2] -= dmg_amount
                break
            except IndexError:
                print("it is up to the player to track their health, "
                      "choose another target")
        print("the health of {0} is now {1}".format
              (grand_list[dmg_choice][1], grand_list[dmg_choice][2]))
        if grand_list[dmg_choice][2] <= 0:
            print(grand_list[dmg_choice][1], "has fallen")
            destroy_enemy(dmg_choice)
