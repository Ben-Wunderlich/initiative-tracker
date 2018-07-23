from num_ensure import numeric_ensure


def main():
    try:
        file = open("hero names.txt", "r")
        names = file.read()
        names = list(names.split(", "))
    except IOError as e:
        print(e)
        print("something went wrong, restart the program,"
              " make sure the file 'hero names.txt' exists")
        input()
        return
    next_choice(names)


def help_commands():
    print("""
    'rename' -- rename a hero
         '+' -- add a hero
         '-' -- remove a hero
      'save' -- saves the current list of heroes
      'quit' -- leaves the program/returns to main menu, SAVE FIRST
      'view' -- shows the names of all th heroes
    """)


def see_heroes(heroes, show_index=False):
    print("the current heroes are:\n")
    for i, hero in enumerate(heroes):
        if show_index:
            print(i, end=" ")
        print(hero)
    print()


def get_index(question, hero_list):
    while True:
        index_of_list = numeric_ensure(question)
        if not (0 <= index_of_list <= len(hero_list) - 1):
            print("that is not a valid character")
        else:
            return index_of_list


def remove_hero(hero_names):
    see_heroes(hero_names, True)
    who_gone = get_index("which hero do you want to remove?", hero_names)
    legacy_name = hero_names[who_gone]
    del hero_names[who_gone]
    print("\n{} is no longer in the party\n".format(legacy_name))
    see_heroes(hero_names)


def get_name(hero_names, prompt):
    is_valid_name = False
    while not is_valid_name:
        new_name = input(prompt)
        if new_name.replace(" ", "") == "":
            pass
        elif new_name in hero_names:
            pass
        else:
            is_valid_name = True
    return new_name


def add_hero(hero_names):
    new_name = get_name(hero_names, "what is the name of the new hero")
    hero_names.append(new_name)
    print("\n" + new_name, "has joined the party!\n")
    see_heroes(hero_names)


def rename(hero_names):
    see_heroes(hero_names, True)
    question = "what is the index of the hero that is going to be renamed?"
    which_hero = get_index(question, hero_names)
    old_name = hero_names[which_hero]
    new_name = get_name(hero_names,
                        "what is {}'s new name?".format(old_name))
    hero_names[which_hero] = new_name
    print("\n" + old_name, "is now know as", new_name + "\n")
    see_heroes(hero_names)


def next_choice(hero_names):
    see_heroes(hero_names)
    the_input = ""
    quit_question = "make sure to save before leaving, do you still want to leave? y/n"
    while the_input != "quit":
        the_input = input("what do you want to do? 'help' to see commands")
        if the_input == "help":
            help_commands()
        elif the_input == "rename":
            rename(hero_names)
        elif the_input == "quit" or the_input == "main":
            if input(quit_question) == "y":
                return
        elif the_input == "+":
            add_hero(hero_names)
        elif the_input == "-":
            remove_hero(hero_names)
        elif the_input == "save":
            write_file(hero_names)
            print("\nfile saved\n")
        elif the_input == "view":
            see_heroes(hero_names)
        else:
            print("that is not a valid command, type"
                  " 'help' for a list of commands")


def write_file(list_of_names):
    out_file = open("hero names.txt", "w")
    last_val = list_of_names[-1]
    for name in list_of_names:
        if name != last_val:
            out_file.write(name + ", ")
        else:
            out_file.write(name)
    out_file.close()

if __name__ == "__main__":
	main()

