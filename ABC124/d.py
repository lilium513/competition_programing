N,K =list(map(int,input().split(" ")))
S = input()
S = list(map(int,list(S)))
cnts = []
cnt = 0
check = 1
for s in S:
  if s == check:
    cnt += 1
  else:
    cnts.append(cnt)
    cnt = 1
    check = 1 - check
cnts.append(cnt)

if S[0] == 0:
    cnts.insert(0,0)

print(cnts)

limit = len(cnts)
size = 2 * K + 1
right  = min(size,limit) -1
left =0

while True:
    print("-"*30)
    print(tmp)
    print("left = ",cnts[left])
    print("right = ",cnts[right])
    print("-"*30)
    tmp += cnts[right]
    tmp -= cnts[left]
    if tmp > ans:
        ans = tmp
    right += 2
    left  += 2
    
    if right > limit:
        break

print(ans)