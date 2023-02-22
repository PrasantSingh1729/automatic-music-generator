# from Random_music import *
from scamp import *
from numpy import random
from Setting import *
import math
from Random_cord_and_melody import generate_melody_from_cord


def random_loop(length=4,cord_octave=3,melody_octave=4):
    loop = []
    global cords,cord_prob,cord_durations,cord_duration_prob
    cords = [[(12*cord_octave+x) for x in row] for row in cords]
    indexs = [x for x in range(len(cords))]
    
    prev = 0
    index = 0
    looplen = 0
    loop_cords = []
    loop = []
    while looplen!=length:
        while index==prev:
            index = random.choice(indexs,p=cord_prob)
        prev = index
        cord = cords[index]
        duration = random.choice(cord_durations,p=cord_duration_prob)
        looplen+=duration
        if looplen>length:
            looplen-=duration
        else:
            loop_cords.append([cord,duration])
            loop.append({'cord':[cord,duration],'melody':generate_melody_from_cord(cord,duration,cord_octave,melody_octave)})
    
    cords = [[(x-12*cord_octave) for x in row] for row in cords]
    return loop

def play_loop(instrument,loop):
    for item in loop:
        cord = item['cord']
        melody = item['melody']
        instrument.play_chord(cord[0],random.uniform(0.8,1.0),cord[1],blocking=False) 
        for note in melody:
            instrument.play_note(note[0],random.uniform(0.8,1.0),note[1]) 


if __name__=="__main__":
    # random.seed(18)
    session = Session(tempo=95)

    # instrument = session.new_part("Guitar Nylon X")
    instrument = session.new_midi_part("Guitar Nylon X",1)


    loop = random_loop(length=12,cord_octave=2,melody_octave=3)
    while True:
        play_loop(instrument,loop)