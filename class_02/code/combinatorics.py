"""
Tomas Meszaros

Permutations, combinations and variations.
"""

import itertools

def permutations(n):
    if len(n) == 1:
        return [n]
    res = []
    for i in n:
        tmp = n[:]
        tmp.remove(i)
        for p in permutations(tmp):
            res.append([i] + p)
    return res

def combinations(n, k, result, var=False):
    """
    Example for: n=[1,2,3] and k=2

    n = [1,2,3]:
        - [] + [2,3] = [2,3]
            - result = [[2,3]]
        - [1] + [3] = [1,3]
            - result = [[2,3], [1,3]]
        - [1,2] + [] = [1,2]
            - result - [[2,3], [1,3], [1,2]]
    """
    if len(n) < k:
        return None
    if len(n) == k:
        if n not in result:
            # throw away already discovered results
            result.append(n)
        if var:
            x = list(reversed(n))
            if x not in result:
                result.append(x)
        return result
    else:
        for item_index, _ in enumerate(n):
            result = combinations(n[:item_index]+n[item_index+1:], k, result, var=var)
        return result

def variations(n, k):
    """ Reusing variations function, just adding reverse of each result.
    """
    return combinations(n, k, [], var=True)

d = [1,2,3,4]
print("permutations:", permutations(d))
print("combinations:", sorted(combinations(d, 2, [])))
print("variations:", sorted(variations(d, 2)))

