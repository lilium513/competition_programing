from collections import defaultdict
import math
ans = 0
import
def rec(num,step,used,pat):
    global ans
    needs = pat[step]


    if step ==len(pat)-1:
        for k,v in num:
            if v >=needs and v not in used:
                ans += 1

    else:
        for  i,(k, v) in enumerate(num):
            if v >= needs and v not in used:
                num[i][1] -= needs
                used.append(k)
                rec(num,step + 1,used,pat)


def c():

    sosus = "2、3、5、7、11、13、17、19、23、29、31、37、41、43、47、53、59、61、67、71、73、79、83、89、97"
    sosus  = sosus.split("、")
    sosus = list(map(int,sosus))
    dic = defaultdict(lambda :0)
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

    pats = [[74],[4,4,2],[14,4],[24,2]]
    for pat in pats:
        nums = list(dic.items())
        nums = list(map(list,nums))
        rec(nums,0,[],pat) #3つがバラバラでなければならない
    print(ans)
if __name__ == "__main__":
    c()