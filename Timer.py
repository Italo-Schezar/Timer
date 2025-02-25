import time

time1 = int(input("Time in seconds: "))

for i in range(time1, 0 , -1):
    sec = i % 60 
    minu = int(i / 60) % 60
    hour = int(i / 3600) % 24
    days = int (i / 86400) % 30
    months = int (i / 2629744) % 12
    years = int(i / 31536000) % 12
    print(f"{years:02}:{months:02}:{days:02}:{hour:02}:{minu:02}:{sec:02}")
    time.sleep(1)
    
print("It's done the time is over")
