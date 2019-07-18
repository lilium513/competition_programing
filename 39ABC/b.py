S = input()
kai = ["Do","Re","Mi","Fa","So","La","Si"]
do = "WBWBWWBWBWBWWBWBWWBW"
i = 0
on = 0
while True:
    if do[i] == "W":
      if do[i:] == S[  : len(do[i:])]:
          print(kai[on])
          exit()
      else:
          on += 1
    i += 1