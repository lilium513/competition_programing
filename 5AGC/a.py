S = input()
scount = 0
tcount = 0
ans = 0
l = len(S)
for c in S:
    if c == "S":
        scount += 1
    else:
        if scount >0:
            scount -=1
            ans += 2

ans += min (scount,tcount) * 2
ans = len(S) -ans
print(ans)