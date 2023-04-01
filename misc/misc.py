import random


def randomize_within_10_percent(number_to_multiply):
    number = random.choice([0.90, 0.92, 0.94, 0.96, 0.98, 1.0, 1.02, 1.04, 1.06, 1.08, 1.1])
    rounded_number = int(round(number*number_to_multiply))
    return rounded_number
