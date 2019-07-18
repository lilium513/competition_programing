H,W =list(map(int,input().split(" ")))
mass  = []
for _ in range(H):
    mass.append(input() + "#")

mass.append((W+1)*"#")
tate = [[0 for _ in range(W+1)] for _ in range(H+1)]
yoko = [[0 for _ in range(W+1)] for _ in range(H+1)]
co = 0
for w in range(W+1):
    st = 0
    for h in range(H+1):
        c = mass[h][w]
        if c == "#":
            for temp in range(st,h):
                tate[temp][w] = co
            st = h + 1
            co = 0
        else:
            co += 1

co = 0
for h in range(H+1):
    st = 0
    for w in range(W+1):
        c = mass[h][w]
        if c == "#":
            for temp in range(st,w):
                yoko[h][temp] = co
            st = w + 1
            co = 0
        else:
            co += 1



ans = 0
for h in range(H):
    for w in range(W):
        cand = tate[h][w] + yoko[h][w]
        if tate[h][w] > 0 and yoko[h][w] > 0:
            cand -= 1
        if cand > ans and mass[h][w] != "#":
            ans =  cand


print(ans)