N  = int (input())
S = input()

#.#
tilnow = []
tilnow.append(S[0])
ans1 = 0

#白を断固として消すパターン
for i,s in enumerate(S[1:]):
    if s == ".": 
        if tilnow[i-1] == "#":
            ans1+=1
            tilnow.append("#")
        else:
            tilnow.append(".")
    else:
        tilnow.append("#")


ans2 = 0
#黒を断固として消すパターン
i= 0

while True:
  s = S[i]
  if i+1 == N:
    break
  if s == "#":
        if S[i+1] == ".":
            ans2+=1
            tilnow.append(".")
        else:
            tilnow.append("#")
  else:
      tilnow.append(".")
  i+=1


print(min(ans1,ans2))
