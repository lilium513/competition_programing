N ,A,B  =list(map(int,input().split(" ")))
N - 2
ab = A+B

if  A > B : #異常値
    print(0)

elif N == 1 :
    if A==B:
        print(1)
    else:
        print(0)
elif N==2:
    print(1)
else:
    minsum = (N-2) * A + ab
    maxsum = (N-2) * B + ab

    print(maxsum - minsum + 1)