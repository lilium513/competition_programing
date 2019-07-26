import math
import bisect
A,B,Q = list(map(int,input().split(" ")))
Ss = [int(input())for _ in range(A)]
Ts = [int(input())for _ in range(B)]
Xs = [int(input())for _ in range(Q)]
Ss.sort()
Ts.sort()
ss = len(Ss)
ts = len(Ts)
for x in Xs:
    si = bisect.bisect_right(Ss,x)
    ti = bisect.bisect_right(Ts, x)
    cands = [[],[]]
    if si > 0:
        cands[0].append(Ss[si-1])
    if si < ss:
        cands[0].append(Ss[si])
    if ti > 0:
        cands[1].append(Ts[ti-1])
    if ti < ts:
        cands[1].append(Ts[ti])
    anss = []
    temp = 0
    for i in [0,1]:
        for t1 in cands[i]: #最初による所
            for t2 in cands[1-i]: #次に寄る所
                temp = abs(x-t1) +  abs(t2-t1)
                anss.append(temp)
    print(min(anss))
