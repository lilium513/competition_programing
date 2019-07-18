
import math
N= int(input())
traget = list(map(int,input().split(" ")))
process = [0] * N 
ans = 0
while True:
    end_flag = True
    target_start = True

    for i in range(N):
        if traget[i] != process[i]:
            process[i] += 1
            end_flag = False
            if target_start:
                ans += 1
                target_start = False
        else:    #targetに到達しているとき
            target_start = True


    # print ("process:",process)
    # print("traget:",traget)
    # print("--"*30)
    if end_flag:
        break
print(ans)