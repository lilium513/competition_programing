k = "keyence"
S = input()
num = len(k)
rem = len(S) - num

flag = False
if S == k:
    flag = True

for i in range(len(S)-rem):
    if S[0:i] + S[i+rem:] == k:
        flag = True
if flag:
    print("YES")
else:
    print("NO")
