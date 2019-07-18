import itertools
import math
N = input()
N = int(N)
passes = ["a","b","c"]

temp = list(itertools.product(passes, repeat=N))
for i in temp:
    print("".join(i))