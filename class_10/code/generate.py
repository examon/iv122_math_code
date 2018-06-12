import random

def generate_random_data(filename, sample_size, x_min, x_max, y_min, y_max):
    f = open(filename, 'w')
    for _ in range(sample_size):
        x = random.choice(range(x_min, x_max))
        y = random.choice(range(y_min, y_max))
        f.write("%d %d\n" % (x, y))

generate_random_data("data/generated1.txt", 100, 0, 10, 50, 100)
