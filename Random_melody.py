from Setting import *
import math
from numpy import random
from scamp import *
from Setting_change import *

def random_melody(instrument, octave=3):
    global notes,note_prob,note_durations,note_duration_prob
    notes = [12*octave+pitch for pitch in notes]
    prev = notes[0]
    pitch = notes[0]
    while True:
        while prev-pitch>6 or prev==pitch:
            pitch = random.choice(notes,p=note_prob)
        prev = pitch
        duration = random.choice(note_durations,p=note_duration_prob)
        isGap = random.choice([True,False],p=(0.10,0.90))
        if not isGap:
            instrument.play_note(pitch,random.uniform(0.8,1.0),duration)
        else:
            wait(duration)

def set_scale(new_key):
    global key,cords,notes
    key,cords,notes = change_scale(cords,notes,key,new_key)


if __name__=="__main__":
    random.seed(95)
    session = Session(tempo=95)
    set_scale('C#')
    # session.print_default_soundfont_presets()
    # session.print_available_midi_output_devices()
    # instrument = session.new_part("Guitar Nylon X")
    instrument = session.new_midi_part("Guitar Nylon X",1)
    random_melody(instrument,4)
