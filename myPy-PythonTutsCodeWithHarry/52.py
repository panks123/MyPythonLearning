#Function caching

#suppose there is a function which takes 3 seconds to run in a single call using an input
#then if it is called 10 times then it will take 10*3=30 seconds

#e.g.
from functools import lru_cache        #lru_cache is a decorator
import time

@lru_cache(maxsize=3)   #it will save latest 3 calls
def some_work(n):
    time.sleep(n)

    return  n

if __name__=='__main__':
    print("running some work")
    some_work(3)
    print("Done...Again running some work")
    some_work(1)
    print("Done...Again running some work")
    some_work(6)
    print("Done...Again running some work")
    some_work(9)
    print("Done...Again running some work")   #this will take 3 seconds as it does not belong to latest maxsize=3 calls
    some_work(1)
    print("Done...Again running some work")   #this will not take 3 seconds as it belongs to latest maxsize=3 calls
    some_work(6)
    print("Done...Again running some work")   #this will not take 3 seconds as it belongs to latest maxsize=3 calls
    some_work(3)
    print("Done")    #this will take 3 seconds as it does not belong to latest maxsize=3 calls

    #So this will take 3*2=6 seconds although we are performing same thing again
    #So for this we implement function caching using which it willtake only ~3 seconds


