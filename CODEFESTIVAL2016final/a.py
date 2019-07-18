S = input()
place = [0,4,6,8]
cands = []
for b1 in [True,False]:
    for b2 in [True, False]:
        for b3 in [True, False]:
            for b4 in [True, False]:
                akb = list("AKIHABARA")
                if b1:
                    akb[0] = ""
                if b2:
                    akb[4] = ""
                if b3:
                    akb[6] = ""
                if b4:
                    akb[8] = ""
                cands.append("".join(akb))
if S in cands:
    print("YES")
else:
    print("NO")