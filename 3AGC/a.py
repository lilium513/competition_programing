S = input()
n = S.count("N")
s = S.count("S")
w = S.count("W")
e = S.count("E")
ans = "Yes"
if n * s ==0:
    if n != 0 or s != 0:
        ans = "No"

if w * e ==0:
    if w != 0 or e != 0:
        ans = "No"

print(ans)