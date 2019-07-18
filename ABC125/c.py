def GCD( a,  b ):
    if b == 0:
        # print("--" * 10)
        return a
    else:
        # print(b)
        return GCD(b, a % b)

N = int(input())
As = list(map(int,input().split(" ")))

left = [0]

for i,A in enumerate(As[:]):
    left.append(GCD(A,left[i]))
Bs = As[::-1]
right = [0]

for i,B in enumerate(Bs[:]):
    right.append(GCD(B,right[i]))
# print(left)
# print(right)

left = left[::-1]

ans = []
for i in range(0,N):
    ans.append(GCD(left[i+1],right[i]))
print(max(ans))
