#excercise7--- Healthy programmer


from pygame import  mixer
from datetime import  datetime
from time import time

def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break

        elif a=='quit':
            exit()
        else:
            print("wrong input")



def log(msg):
    with open('mylog.txt','a') as f:
        f.write(f"{msg} : {datetime.now()}\n")

if __name__=='__main__':
    #musiconloop("some.mp3","stop")
    init_water=time()
    init_eyes=time()
    init_exercise=time()
    water_interval=60*60    #for 1 hour
    eyes_interval=40*60     #for 40 minutes
    exercise_interval=120*60    #for 2 hours
    while True:
        if time() - init_water > water_interval:
            print("Reminder: Water drinking time \n\n Enter 'done' to stop the alarm or Enter 'quit' to quit")
            musiconloop('some.mp3', 'done')
            init_water=time()
            log('Drank water at')

        if time() - init_eyes > eyes_interval:
            print("Reminder: Do some eyes work \n\n Enter 'done' to stop the alarm or Enter 'quit' to quit")
            musiconloop('some.mp3', 'done')
            init_eyes=time()
            log('Eyes relaxed at')


        if time()-init_exercise>exercise_interval:
            print("Reminder: Physical activity time\n\nEnter 'done' to stop the alarm or Enter 'quit' to quit")
            musiconloop('some.mp3', 'done')
            init_exercise=time()
            log('Physical activity done at')




