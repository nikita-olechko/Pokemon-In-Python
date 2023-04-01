import random, time


def randomize_within_10_percent(number_to_multiply):
    number = random.choice([0.90, 0.92, 0.94, 0.96, 0.98, 1.0, 1.02, 1.04, 1.06, 1.08, 1.1])
    rounded_number = int(round(number*number_to_multiply))
    return rounded_number


def print_dialogue(string):
    dialogue = string.split(sep="\n")
    for index, line in enumerate(dialogue):
        if index == 0:
            print(line)
            continue
        line += "\n"
        time.sleep(1)
        for char in line:
            time.sleep(0.03)
            print(char, end="")
