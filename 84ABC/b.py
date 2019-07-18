import itertools
import math

def judY(y):
    if  0<=y and y <= 99:
        return True
    else:
        return  False

def judM(m):
    if  0<m and m <=12:
        return True
    else:
        return  False



s1 = input()
zenhan = int (s1[0:2])
kohan  = int(s1[2:])

zenhanY = False
zenhanM = False
kohanY = False
kohanM = False
if judY(zenhan):
    zenhanY = True

if judM(zenhan):
    zenhanM = True

if judM(kohan):
    kohanM = True

if judY(kohan):
    kohanY = True


YYMM = False
MMYY = False
if zenhanY and kohanM:
    YYMM = True

if zenhanM and kohanY:
    MMYY = True

if YYMM and not MMYY:
    print("YYMM")
elif not YYMM and  MMYY:
    print("MMYY")
elif YYMM and MMYY:
    print("AMBIGUOUS")
else:
    print("NA")




