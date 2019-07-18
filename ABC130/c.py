W,H,x,y =  list(map(int,input().split(" ")))
s = W*H/2

whalf = False
hhalf = False
if W/2 == x and H/2 == y:
    print(s,1)

else:
    print(s,0)