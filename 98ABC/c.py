import itertools

N = int(input())
S = input()
hidarikara = [0]
for i,c in enumerate(S):
    if S[i] == "W":
         hidarikara.append( hidarikara[i] + 1  )
    else:
        hidarikara.append(hidarikara[i])
S = S[::-1]

migikara = [0]

for i,c in enumerate(S):
    if S[i] == "E":
         migikara.append( migikara[i] + 1  )
    else:
        migikara.append(migikara[i])
anss = [migikara[i] + hidarikara[N-1-i] for i in range(N)]
print(min(anss))