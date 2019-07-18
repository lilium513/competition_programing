import itertools
sx,sy,tx,ty = list(map(int,input().split(" ")))
diffX = tx - sx
diffY = ty - sy
ans = ""
ans+=diffY*"U"
ans+=diffX*"R"
ans+=diffY*"D"
ans+=diffX*"L"
ans+="L"
ans+=(diffY+1)*"U"
ans+=(diffX+1)*"R"
ans+="D"

ans+="R"
ans+=(diffY+1)*"D"
ans+=(diffX+1)*"L"
ans+="U"
print(ans)