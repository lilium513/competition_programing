

import itertools
import math

class Emp():
    def __init__(self):
        self.buka = []
        self.sal = 0

N = input()
N = int(N)

emp = [Emp() for i in range(0,N+1)]
for i in range(2,N+1):
    temp = int(input())
    emp[temp].buka.append(i)

for i  in range(N,0,-1):
    if len(emp[i].buka) == 0:
        emp[i].sal = 1
    elif len(emp[i].buka) == 1:
        emp[i].sal = emp[emp[i].buka[0]].sal * 2 + 1
    else :
        sals = [emp[temp].sal for temp in  emp[i].buka]
        emp[i].sal =min(sals) + max(sals) + 1
print(emp[1].sal)