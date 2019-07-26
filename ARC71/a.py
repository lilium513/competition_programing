
P,Q,R = list(map(int,input().split(" ")))

ans = min (P+Q,Q+R,R+P)
print(ans)