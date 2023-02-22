from scamp import *
from numpy import random
from Setting import *
import math

def random_cord(instrument, octave=3):
    global cords,cord_prob,cord_durations,cord_duration_prob
    cords = [[(12*octave+x) for x in row] for row in cords]
    indexs = [x for x in range(len(cords))]
    prev = 0
    index = 0
    while True:
        while index==prev:
            index = random.choice(indexs,p=cord_prob)
        prev = index
        cord = cords[index]
        duration = random.choice(cord_durations,p=cord_duration_prob)
        isGap = random.choice([True,False],p=(0.05,0.95))
        if not isGap:
            instrument.play_chord(cord,random.uniform(0.8,1.0),duration)
        else:
            wait(duration)

if __name__=="__main__":
    random.seed(152)
    session = Session(tempo=95)
    # instrument1 = session.new_part("Guitar Nylon X")
    instrument = session.new_midi_part("Guitar Nylon X",1)
    random_cord(instrument,2)
    