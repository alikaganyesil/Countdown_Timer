import time

def countdown(t):
    while t:
        # divmod(a,b) = (a//b, a%b)
        # we can calculate mins and seconds with this method
        mins, sec = divmod(t, 60)
        timer = f"{mins} minute, {sec} second"
        print(timer)
        time.sleep(1)
        t = t - 1

t = input("please enter the time in seconds: ")
countdown(int(t))