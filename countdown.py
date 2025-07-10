
import time

import winsound

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer, end="\r")

        if t <= 3:
            winsound.Beep(1000, 500)

        time.sleep(1)
        t -= 1

    print("run, run, run!")
    winsound.Beep(2000, 2000)
    
    

t = input('Enter the time in seconds: ')

countdown(int(t))