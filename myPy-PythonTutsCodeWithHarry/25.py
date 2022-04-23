# time module

# finding the execution time

import time

initial=time.time()  # Returns the ticks---accuracy is in milliseconds

for i in range(50):
    print("This is Pankaj")

print(time.time()-initial)


i=0
initial2 =time.time()
while i<5:
    print("This is Pankaj")
    time.sleep(1)  # It takes seconds in argument
    i+=1
print(time.time()-initial2)

print(time.localtime(time.time()))   # this returns a tuple
print(time.asctime(time.localtime(time.time())))  # asctime() converts the time in tuple into presentable time


