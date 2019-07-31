from collections import defaultdict

N, K = map(int, input().split())
S = input()

counts = dict()



last_char = S[0]
counts["0"] = []
counts["1"] = []
counts[last_char].append(0)
for s in S:
    if s == last_char:
        counts[s][-1] += 1

    else:
        counts[s].append(1)
        last_char = s

ans = 0:
l = 0
print(counts)