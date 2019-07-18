S = input()
ans = 0
g_count = 0
for c in S:
    if c == "g":
        if g_count > 0:
            g_count-=1
            ans += 1
        else:
            g_count += 1
    else:
        if g_count > 0:
            g_count-=1

        else:
            g_count += 1
            ans -=1
print(ans)