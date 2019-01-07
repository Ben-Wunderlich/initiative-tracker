# function based full dice roller with statistics
from random import randint


def xdx_eval(given_str, sign, get_the_avg, minimum_val2, max_val2):
    try:
        total_val = 0
        split_index = given_str.index("d")
        num_of_dies = int(given_str[:split_index])
        die_val = int(given_str[split_index + 1:])
        if num_of_dies != 1:
            print("\nrolling {} {} sided dice...".format(num_of_dies, die_val))
        else:
            print("\nrolling {} {} sided die...".format(num_of_dies, die_val))
        for _ in range(num_of_dies):  # number of times to roll the dice
            if get_the_avg:  # only used when getting statistics
                if sign:
                    minimum_val2 += 1
                    max_val2 += die_val
                else:
                    minimum_val2 -= die_val
                    max_val2 -= 1
            current_roll = randint(1, die_val)  # most important line
            if current_roll == die_val:
                print("You got the maximum roll of {0}!".format(current_roll))
            else:
                print("You rolled a {1} out of {0}".format(die_val, current_roll))
            total_val += current_roll
        return total_val, minimum_val2, max_val2
    except ValueError:
        print("That input was not valid, try again using notation like 2d8-3d5+5")


def sign_pls(first_dig):
    if first_dig.isdecimal():
        return True
    elif "+" in first_dig:
        return True
    elif "-" in first_dig:  # I can't bring myself to turn this into an else
        return False


def operator_index(strong):  # gets the index of the next required split
    pos_incl = "+" in strong
    neg_incl = "-" in strong
    if pos_incl:
        where_pos = strong.index("+")
    if neg_incl:
        where_neg = strong.index("-")
    if pos_incl and not neg_incl:
        return where_pos
    elif neg_incl and not pos_incl:
        return where_neg
    elif pos_incl and neg_incl:
        if where_neg < where_pos:
            return where_neg
        else:
            return where_pos
    else:
        return len(strong)


def number_check(string):
    try:
        int(string)
    except:
        return False
    return True


def string_sorter(die_choose, get_average=False):
    die_choose.replace(" ", "")
    grand_tot = max_val = minimum_val = 0  # resets all the values
    grp_amt = die_choose.count("+")
    neg_amt = die_choose.count("-")

    for i in range(grp_amt + neg_amt + 1):  # +1 for if it is just a number
        if die_choose. replace(" ", "") == "":
            break
        front_sign = sign_pls(die_choose[0])  # checks if is + or -
        if not die_choose[0].isnumeric():
            die_choose = die_choose[1:]  # gets rid of +- at start of  string
        next_indx = operator_index(die_choose)
        is_negative = 1 if front_sign else -1
        if front_sign:
            print("+" + die_choose[:next_indx])
        else:
            print("-" + die_choose[:next_indx])
        if number_check(die_choose[:next_indx]):  # if the next thing is a number
            grand_tot += int(die_choose[:next_indx]) * is_negative
            minimum_val += int(die_choose[:next_indx]) * is_negative
            max_val += int(die_choose[:next_indx]) * is_negative
        else:  # if the next thing is not just a number
            try:
                add_amount = xdx_eval(die_choose[:next_indx], front_sign, get_average, minimum_val, max_val)
                grand_tot += add_amount[0] * is_negative
                if get_average:
                    minimum_val += add_amount[1]
                    max_val += add_amount[2]
            except TypeError:
                print()
                return
        die_choose = die_choose[next_indx:]  # takes off part that was just used

    if get_average:
        return grand_tot, minimum_val, max_val
    else:
        return grand_tot


def average_calculator(last_string):
    if last_string != "":
        display_result(string_sorter(last_string, True), last_string)
    else:
        print("you need to put in a calculation before finding its average\n")


def display_result(result, roll):
    if type(result) == tuple:
        print("\nthe maximum possible roll for {} is:".format(roll), result[2])
        print("the minimum roll is:", result[1])
        print("the average roll is:", (result[2] + result[1]) / 2)
        print("\nyour total roll is:", result[0], "\n")
    else:
        print("\nyour total roll is:", result, "\n")
    return


def main():
    repeat_saver = ""
    input_die = ""
    while "quit" not in input_die:
        input_die = input("enter the number and type of dice you would like "
            "to roll, type 'quit' to quit, hit enter to redo the last roll "
            "or 'avg' to see the probability of your last roll \n")
        if "quit" in input_die:
            continue
        input_die.replace(" ", "")
        if input_die == "":
            input_die = repeat_saver
            if input_die == "":
                print("you don't have a calculation to redo, try again\n")
                continue
            print("redoing", repeat_saver)

        if "avg" in input_die:  # add chance of the roll happening
            average_calculator(repeat_saver)
            continue
        repeat_saver = input_die
        display_result(string_sorter(input_die, False), repeat_saver)


if __name__ == "__main__":
    print("welcome to dice roller 2018, an example roll is 2d4 + 3d6 - 4\n")
    main()