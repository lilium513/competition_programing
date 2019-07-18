N  = int (input())
S = input()

#.#
b = S.count("#")
w = S.count(".")

cotB = 0
cotW = 0
ans = w
for i,s in enumerate(S):
    if s ==".":
        cotW+= 1
    else:
        cotB+=1
    if ans >=  cotB + (w - cotW):
        ans = cotB + (w - cotW)
print(ans)