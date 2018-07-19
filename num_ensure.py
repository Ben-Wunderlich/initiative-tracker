#from num_ensure import numeric_ensure
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