"""
Tomas Meszaros

Randomness detection in the set of numbers.
"""

from pprint import pprint as pp

DATA = ["data/random1.txt",
        "data/random2.txt",
        "data/random3.txt",
        "data/random4.txt",
        "data/random5.txt",
        "data/random6.txt",
        "data/random7.txt"]

def get_numbers(data):
    """ Reads data from random*.txt.
    """
    numbers = open(data)
    numbers = numbers.read().split()
    #numbers = list(map(lambda x: int(x), numbers))
    return numbers

def number_frequency(data):
    """ Counts integer frequency in in data.
    """
    freq = {}
    for number in data:
        if number in freq:
            freq[number] += 1
        else:
            freq[number] = 1
    return freq

def bigram_frequency(data):
    """ Counts bi-gram (pair of two consecutive numbers) frequency in data.
    """
    freq = {}
    for i, number in enumerate(data):
        if i < len(data)-1:
            bigram = data[i] + data[i+1]
            if bigram in freq:
                freq[bigram] += 1
            else:
                freq[bigram] = 1
    return freq

def consecutive_number_frequency(data):
    """ Counts frequencies of consecutive number.

    Input:
    [1, 2, 2, 3, 4, 1, 2, 1, 3, 4]

    Output:
    {1: {1:0, 2:2, 3:1, 4:0},
     2: {1:1, 2:1, 3:1, 4:0},
     3: {1:0, 2:0, 3:0, 4:2},
     4: {1:1, 2:0, 3:0, 4:0}}
    """
    freq = {}
    for i, number in enumerate(data):
        if i < len(data)-1:
            cur_num = data[i]
            consecutive_num = data[i+1]
            if cur_num not in freq:
                freq[cur_num] = {}

            if consecutive_num in freq[cur_num]:
                freq[cur_num][consecutive_num] += 1
            else:
                freq[cur_num][consecutive_num] = 1
    return freq

def run_tests(data_file):
    data = get_numbers(data_file)
    number_freq = number_frequency(data)
    bigram_freq = bigram_frequency(data)
    consecutive_number_freq = consecutive_number_frequency(data)
    print(data_file)
    print("\nnumber frequency:")
    pp(number_freq)
    print("\nbigram frequency:")
    print(bigram_freq)
    print("\nconsecutive number frequency:")
    pp(consecutive_number_freq)
    print()


for data_file in DATA:
    run_tests(data_file)
