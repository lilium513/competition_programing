import itertools
import math

LIM = 50



def do():
    ans = 0
    A,B,C,D,E,F= list(map(int,input().split(" ")))
    waters = []
    for i in range(31):
        for j in range(31):
            water = A*i* 100+B*j* 100
            if water <= F and water != 0:
                waters.append(water)
    solts = []
    for i in range(3000):
        for j in range(3000):
            solt = C * i + D * j
            if solt > E * F /100:
                break
            solts.append(solt)

    max_nodo = -1
    ans_water = 0
    ans_solt = 0
    for solt in solts:
        for water in waters:
            if solt/(water/100) <= E:
                if (100 * solt)/(solt+water) >= max_nodo and water + solt <= F:
                    max_nodo =(100 * solt)/(solt+water)
                    ans_water = water + solt
                    ans_solt = solt

    print(ans_water,ans_solt)





if __name__ == "__main__":
    do()