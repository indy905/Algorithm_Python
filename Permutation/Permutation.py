import unittest


def permutation(n, i):
    if i == len(n) - 1:
        print(n)
    else:
        for j in range(i, len(n)):
            n[i], n[j] = n[j], n[i]
            permutation(n, i + 1)
            n[i], n[j] = n[j], n[i]


permutation([1,2,3], 0)