from pygame import mixer
from time import time
#import datetime
from datetime import date,datetime
def music_loop(music_file,stopVar,msg):
    mixer.init()
    mixer.music.load(music_file)
    mixer.music.play(-1)
    while(True):
        user_input=input()
        if stopVar==user_input:
            mixer.music.stop()
            write_log(msg)
            break
def write_log(msg):
    with open("water_exercise_eye_EASYMethod.txt","a") as file:
        file.write(f"{msg}: {datetime.now()}\n")

if __name__ == '__main__':
    water_init=time()
    exer_init=time()
    eye_init=time()

    water_sec=60*125
    exer_sec=60*45
    eye_sec=60*30
    while(True):

        if time() - water_init>=water_sec:
            print("Time to drink water\nType 'd' if you have drank water")
            music_loop("C:\\Users\\gowat\\PycharmProjects\\music\\mind_my_business.mp3","d","Drank water at")
            water_init=time()
        elif time() - eye_init>=eye_sec:
            print("Time to do Eye exercise\nType 'e' to quit alarm")
            music_loop("C:\\Users\\gowat\\PycharmProjects\\music\\Eye To Eye.mp3","e","Eye activity done at")
            eye_init=time()
        elif time() - exer_init>=exer_sec:
            print("Time to do physical activity\nType 'p' to quit alarm")
            music_loop("C:\\Users\\gowat\\PycharmProjects\\music\\Workout.mp3","p","Physical activity done at")
            exer_init=time()


