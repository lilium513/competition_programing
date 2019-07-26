from collections import defaultdict
import math

def c():
    sosus = "2、3、5、7、11、13、17、19、23、29、31、37、41、43、47、53、59、61、67、71、73、79、83、89、97"
    sosus  = sosus.split("、")
    sosus = list(map(int,sosus))
    dic = dict(zip(sosus,len(sosus) * [0]))
    N =int(input())
    p = 0
    for i in range(2,N+1):
        lim = int(math.sqrt(i)) + 1
        cot = 0
        p = 0
        while   i != 1:
            p = sosus[cot]
            if i % p == 0:
                dic[p] += 1
                i = i // p
            else:
                cot += 1
        if i != 1:
            sosus[i] += 1
    ans = 0

    pats = [[14,4],[24,2]]
    for v in dic.values():
        if v >= 74:
            ans += 1

    for pat in pats:
        temp = 0
        temp2 = 0
        p1,p2 = pat
        for v in dic.values():
            if v>= p1:
                temp += 1
        for v in dic.values():
            if v>= p2:
                temp2 += 1
        ans += max(temp * (temp2 - 1),0)

    temp = 0
    temp2 = 0
    p1,p2 = 4,2
    for v in dic.values():
        if v>= p1:
            temp += 1
    for v in dic.values():
        if v>= p2:
            temp2 += 1
    ans += max(temp * (temp-1) //2 *  (temp2 - 2),0)
    print(ans)
if __name__ == "__main__":
    c()