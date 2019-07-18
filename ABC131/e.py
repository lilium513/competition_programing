N,K =  list(map(int,input().split(" ")))
co = 1/2 * (N-2)*(N-1)
co = int(co)
if K > co:
    print(-1)
    exit()
edges = []
diff = co - K
for i in range(2,N+1):
    edges.append((1,i))

co = 0
#diffに達するまで結ぶ
flag = False
for i in range(2,N+1):
    for j in range(i+1,N+1):
        if co == diff:
            flag = True
            break
        edges.append((i,j))
        co += 1
    if flag:
        break

M = len(edges)
print(M)
for edge in edges:
    a,b = edge
    print(a,b)