

S = input()
N = int(input())
l = len(S)

sub = {}
for i in range(1,6):
    for j in range(0,l+1-i):
        temp = S[j:j+i]
        if temp not in sub:
            sub [temp]  = True

sub = list(sub.keys())
sub.sort()
print(sub[N-1])



