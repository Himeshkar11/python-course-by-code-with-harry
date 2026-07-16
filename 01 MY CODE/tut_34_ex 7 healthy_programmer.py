# import pygame as p
# # p.mixer.init()
# # # what it does is it starts the sound systemm it must be called before starting the music
# # p.mixer.music.load('water.mp3')
# # # this loads the song into the memory
# # p.mixer.music.play(loops=)
# # # this stats the playback
# # # we can select loops = 0 for single time playback
# # # we can select loops = 1 for infinte time playback
# # p.mixer.music.stop()
# # # this stops the playback immediately
# # p.mixer.music.pause()
# # p.mixer.music.unpause()
# # # these are used to pause and unpase the song / audio
# # p.mixer.music.get_busy()
# # # this returns true if music is playing else false
# def get_water():
#     p.mixer.init()
#     p.mixer.music.load("water.mp3")
#     p.mixer.music.play(loops=-1)
# get_water()
from pygame import mixer
from datetime import datetime
from time import time 
def musiconloop(file,stopper):
    # file is the file which wewnat to play 
    # stopper stops the music when the user wants 
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}")
def log_water(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}")
def log_eyes(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}")  
def log_exercise(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}")

if __name__  == '__main__':
    # musiconloop("water.mp3","stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs=5
    exsecs = 10
    eyessecs=20
    while True:
        if time() - init_water > watersecs:
          print("Water drinking time . Enter 'drank to stop the alarm ")  
          musiconloop('water.mp3','drank')
          log_water("Drank  water At")
        if time() - init_eyes > eyessecs:  
          print("eyes exercise time . Enter 'doneeyes to stop the alarm ")  
          musiconloop('eyes.mp3','doneeyes')
          log_eyes("Done eyes exercise At")
        if time() - init_exercise > exsecs:
          print("Exercise time . Enter 'doneexercise to stop the alarm ")  
          musiconloop('exercise.mp3','doneexercise')
          log_exercise("Done exercise At")
          musiconloop('water.mp3','drank')
          log_water("Drank  water At")