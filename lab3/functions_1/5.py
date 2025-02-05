from itertools import permutations
def permutation(str):
    all=permutations(str)
    return [''.join(p) for p in all]

str=str(input("Write string "))
print(permutation(str))