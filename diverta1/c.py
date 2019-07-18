
N = int(input())
acount = 0
bcount = 0
ab = 0
ans = 0
for i in range(N):
    s = input()
    ans += s.count("AB")
    if s[-1] == "A" and s[0] == "B":
        ab += 1
    if s[-1] == "A":
        acount += 1
    if s[0] == "B":
        bcount += 1
add = min (acount,bcount)
if ab == acount and ab == bcount:
    add -= 1


# if ans + add < 0:
#     print(0)
# else:
print(ans + add)