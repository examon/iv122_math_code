"""
Tomas Meszaros

Various math puzzles.
"""

import math

from pprint import pprint as pp
from collections import OrderedDict


def ex_a_3():
    """ Ex. A. 3.

    Collatzova posloupnost je definována následovně: „vezmi přirozené číslo, pokud je
    sudé, vyděl jej dvěma, pokud je liché, vynásob jej třemi a přičti jedničku; tento
    postup opakuj, dokud nedostaneš číslo jednaÿ. Například pro číslo 27 potřebujeme
    111 kroků, než se dostaneme na číslo 1. Pro které číslo menší než 10000 potřebujeme
    nejvíce kroků?
    """
    def collatz_rec(n, step=0):
        if n == 1:
            return (1, step)
        if n % 2 == 0:
            return collatz_rec(n/2, step+1)
        else:
            return collatz_rec(n*3+1, step+1)

    def collatz(n):
        num = n
        steps = 0
        while n != 1:
            if n % 2 == 0:
                n = n/2
            else:
                n = n*3+1
            steps += 1
        return (num, steps)

    num = {'num': None, 'steps': 0}
    for i in range(1, 10000):
        n, steps = collatz(i)
        if steps > num['steps']:
            num['num'] = n
            num['steps'] = steps
    print("Ex. A. 3.:", num)


def ex_a_1_and_4():
    """ Ex. A. 1. & 4.

    1.

    Které z přirozených čísel menších než 10000 má nejvíce dělitelů? Je odpověď na tuto
    otázku jednoznačná?

    4.

    Jaký je součet všech prvočísel, která jsou menší než 1000 a neobsahují žádnou trojku?
    """
    def num_of_divisors(n):
        nums = []
        for i in range(1, n+1):
            if n % i == 0:
                nums.append(i)
        return (n, len(nums), nums)

    def get_divisors_up_to(max_num):
        num = OrderedDict()
        for i in range(1, max_num):
            n, divisors_count, divisors = num_of_divisors(i)
            if divisors_count not in num:
                num[divisors_count] = [(n, divisors_count, divisors)]
            else:
                num[divisors_count].append((n, divisors_count, divisors))
        return num

    # A. 1.
    divisors_10000 = get_divisors_up_to(10000)
    for number in divisors_10000[max(divisors_10000)]:
        print('Ex. A. 1.: number', number[0], 'has', number[1], 'divisors')

    # A. 4.
    divisors_1000 = get_divisors_up_to(1000)
    primes = set()
    for prime_record in divisors_1000[2]:
        if '3' not in str(prime_record[0]):
            primes.add(prime_record[0])
    print('Ex. A. 4.: number of primes without 3, from 1 to 1000 =', len(primes), ',with sum =', sum(primes))


def ex_a_2():
    """ Ex. A. 2.

    Některá čísla jdou vyjádřit jako součet tří druhých mocnin přirozených čísel, na-
    příklad 964 = 6**2 + 12**2 + 28**2 . Jiná takto vyjádřit nejdou, například číslo 7. Kolik
    přirozených čísel menších než 1000 takto vyjádřit nejde?
    """
    def get_abc(num):
        cap = math.ceil(math.sqrt(num))
        #print(num, cap)
        for a in range(0, cap):
            for b in range(0, cap):
                for c in range(0, cap):
                    if num == a**2 + b**2 + c**2:
                        return (num, (a, a**2), (b, b**2), (c, c**2))
        return (num, None)

    count = 0
    for i in range(0, 1000):
        res = get_abc(i)
        #print(res)
        if res[1] == None:
            count += 1
        #print(count)
    # TODO: count should be 200???
    print("Ex. A. 2.: no. of numters =", count)

def ex_a_5():
    """ Ex. A. 5.

    Uvažme posloupnost, která začíná dvěmi jedničkami a každý další člen je součtem
    dvou předchozích navýšený o jejich největšího společného dělitele. Posloupnost tedy
    začíná: 1, 1, 3, 5, 9, 15, 27, 45, 81, 135, 243, 405. Jaká je hodnota prvního prvku
    této posloupnosti, který je větší než milion?
    """
    def gcd(a, b):
        """ From lecture
        """
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    a = 1
    b = 1
    while True:
        x = b
        y = a + b + gcd(a, b)
        if y > 1000000:
            print("Ex. A. 5.: first number over 1 000 000 =", y)
            break
        a = x
        b = y

ex_a_1_and_4()
ex_a_2()
ex_a_3()
ex_a_5()
