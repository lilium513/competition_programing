from datetime import datetime as dt
def getDt(day):
    temp = day.split("/")
    temp = list(map(int,temp))
    return dt(temp[0],temp[1],temp[2])

a, b = input().split(" ")
a = int(a)
b = int(b)

if a == 0:
    print(0)
else:
    vip_attends = {}
    for i in range(a):
        spacial_schedules = input().split(" ")
        for day in spacial_schedules[1:]:
            if day not in vip_attends :
                vip_attends[day] = 1
            else:
                vip_attends[day] += 1
    attends = {}
    for day, num in vip_attends.items():
        if num == a:
            attends[day] = num

    for i in range(b):
        schedules = input().split(" ")
        for day in schedules[1:]:
            if day in attends:
                attends[day] += 1



    attends = sorted(attends,getDt())
    max_k = max(attends)
    print(max_k + " " + str(attends[max_k]) )
