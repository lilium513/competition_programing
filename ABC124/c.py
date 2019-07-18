S = input()
s1 = list(S)
s2 = list(S)

ans1 = 0
ans2 = 0
for i,t in enumerate(s1):
    if i%2 == 0:
        if t == "0":
            ans1 += 1
    else:
        if t == "1":
            ans1 += 1


for i,t in enumerate(s1):
    if i%2 == 0:
        if t == "1":
            ans2 += 1
    else:
        if t == "0":
            ans2 += 1
print(min (ans1,ans2))
