import time

initial_time = 0

def timer(chkr, seconds:int):
    start = time.time()
    while chkr!=True:
        time.sleep(seconds)
    end = time.time()
    val = end-start
    return val*1000
