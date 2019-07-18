import math
def swap(i1,i2,ar):
    temp = ar[i2]
    ar[i2] = ar[i1]
    ar[i1] = temp
    return

N = int( input())
amari = (N % 30) % 5
first = (N % 30) //5
cards = []
for i in range(6):
    cards.append((first + i )%6 + 1    )

for i in range(amari):
    i1 = i%5
    i2 = i%5 + 1

    temp = cards[i2]
    cards[i2] = cards[i1]
    cards[i1] = temp

cards = list(map(str,cards))
print("".join(cards))