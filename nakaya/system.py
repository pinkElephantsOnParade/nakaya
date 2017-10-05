
import sys
import time

def pathList():
    print("[Python System Path List]")
    for item in sys.path:
        print(item)    

def loopProcess(func, args=(), maxRetry=100, isPrint=False, Exceptions=(Exception,)):
    count = 0
    dst = None
    while (1 <= maxRetry):
        try:
            dst = func(*args)
            maxRetry = -1 
        except Exceptions as e:
            if isPrint:
                print(e)
            time.sleep(5)
            maxRetry = maxRetry - 1
            count = count + 1
        if isPrint:
            print( "[" + func.__name__ +":count]" + str(count))
    return dst

def timeMeasure(func, args=()):
    start = time.time()
    func(*args)
    elapsed_time = time.time() - start
    return elapsed_time