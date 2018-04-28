"""
Tomas Meszaros

https://en.wikipedia.org/wiki/Central_limit_theorem
"""

import random

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

"""
red_patch = mpatches.Patch(color='red', label='The red data')
plt.legend(handles=[red_patch])
plt.show()
"""

def roll_fair_dice():
    return random.choice([1,2,3,4,5,6])

def roll_weighted_dice():
    return random.choice(([6]*6)+([5]*5)+([4]*4)+([3]*3)+([2]*2)+[1])

def roll_inverted_weighted_dice():
    return random.choice([6]+([5]*2)+([4]*3)+([3]*4)+([2]*5)+([1]*6))

def roll_pick_random_dice():
    """ pick random dice
    """
    pass

def roll_dice_get_average(dice, rolls):
    rolls_sum = 0
    for _ in range(rolls):
        rolls_sum += dice()
    return (rolls_sum/rolls)

def roll_experiment(dice, samples, rolls):
    results = []
    for _ in range(samples):
        results.append(roll_dice_get_average(dice, rolls))
    return results

def make_experiment_and_histogram(samples, rolls, alpha=1):
    # Draw legends
    plot = plt.figure()
    plt.xlabel("number of averages: {SAMPLES}, dice rolls to get average: {ROLLS}".format(
            SAMPLES=samples, ROLLS=rolls))
    plt.ylabel("number of averages")
    plot.legend(handles=[mpatches.Patch(color="green", label="inverse"),
                         mpatches.Patch(color="blue", label="fair"),
                         mpatches.Patch(color="orange", label="weighted")])

    fair = roll_experiment(roll_fair_dice, samples, rolls)
    plt.hist(fair, alpha=alpha)
    weighted = roll_experiment(roll_weighted_dice, samples, rolls)
    plt.hist(weighted, alpha=alpha)
    inverted = roll_experiment(roll_inverted_weighted_dice, samples, rolls)
    plt.hist(inverted, alpha=alpha)

    plt.savefig("img/dice_histogram_samples_{SAMPLES}_rolls_{ROLLS}.png".format(SAMPLES=samples, ROLLS=rolls))


make_experiment_and_histogram(samples=1000, rolls=10, alpha=0.8)
make_experiment_and_histogram(samples=1000, rolls=100, alpha=0.8)
make_experiment_and_histogram(samples=1000, rolls=1000, alpha=0.8)
make_experiment_and_histogram(samples=1000, rolls=10000, alpha=0.8)

make_experiment_and_histogram(samples=10, rolls=1000, alpha=0.8)
make_experiment_and_histogram(samples=100, rolls=1000, alpha=0.8)
make_experiment_and_histogram(samples=1000, rolls=1000, alpha=0.8)
make_experiment_and_histogram(samples=10000, rolls=1000, alpha=0.8)

