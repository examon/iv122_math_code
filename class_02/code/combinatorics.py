"""
Tomas Meszaros

Permutations, variations and combinations.

TODO:
- variations
- combinations
"""

def permutation(ns):
    if len(ns) == 1:
        return [ns]

    res = []
    for i in ns:
        tmp = ns[:]
        tmp.remove(i)
        for p in permutation(tmp):
            res.append([i] + p)
    return res
print(permutation(['a', 'b', 'c']))

def var(ns, k):
    if len(ns) == 1:
        return [ns]

    res = []
    for i in ns:
        tmp = ns[:]
        tmp.remove(i)
        for p in var(tmp, k-1):
            print(p)
            res.append([i] + [p])
    return res
#print(var(['a', 'b', 'c', 'd'], 2))
