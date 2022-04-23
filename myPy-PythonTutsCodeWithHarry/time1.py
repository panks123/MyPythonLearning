# import time
#
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S", t)
# print(current_time)
# print(type(current_time))




if __name__ == '__main__':
    N = int(input())
    li=[]
    while(N):
        command=input().split(" ")

        if command[0]=='print':
            print(li)

        elif command[0]=='append':
            #print(int(command[1]))
            li.append(int(command[1]))

        elif command[0]=='insert':
            li.insert(int(command[1]),int(command[2]))
        elif command[0]=='remove':
            li.remove(int(command[1]))
        elif command[0]=='pop':
            li.pop()
        elif command[0]=='reverse':
            li.reverse()
        elif command[0]=='sort':
            li.sort()


        N-=1