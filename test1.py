import time

while(True):
    t = time.localtime()
    f = time.localtime()
    Time = time.strftime("%S",t)
    Ti = time.strftime("%H:%M:%S",f)
    print(Ti)
    if(Time == 1):
        print("1")