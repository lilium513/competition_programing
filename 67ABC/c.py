import itertools
import math
N = int(input())
cards = list(map(int,input().split(" ")))
ruiseki = [cards[0]]
su  = sum(cards)
for i,card in enumerate(cards[1:-1]): #[1:-1]→片方が全部取るケースを除外
    ruiseki.append(ruiseki[i]+card)

ans = 10e15
for temp  in ruiseki:
    x = temp
    y = su - temp
    cand = abs(x-y)
    if cand < ans:
        ans = cand

print(ans)