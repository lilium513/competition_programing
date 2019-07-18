S = input()
T  = input()
OKs = ["a","t","c","o","d","e","r"]
for c1,c2 in zip(S,T):
    if c1 == c2:
        pass
    elif c1 == "@" and c2 in OKs :
        pass
    elif c2 == "@" and c1 in OKs :
        pass
    else:
        print("You will lose")
        exit()
print("You can win")
