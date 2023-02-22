from scamp import *
from numpy import random
from Setting import *
import math

def generate_melody_from_cord(cord,duration,cord_octave=3, melody_octave=4):
    global note_durations, note_duration_prob

    pitches = [12*(melody_octave-cord_octave)+pitch for pitch in cord]
    # cord centric notes probability
    prob = generate_prob([40,30,30])

    melody = []
    length = 0
    while length!=duration:
        pitch = random.choice(pitches,p=prob)
        x = random.choice(note_durations,p=note_duration_prob)
        length+=x
        if length>duration:
            length-=x
        else:
            melody.append([pitch,x])
    return melody

def random_cord_and_melody(instrument,cord_octave=3, melody_octave=4):
    global cords,cord_durations,cord_duration_prob,cord_prob

    cords = [[(12*cord_octave+x) for x in row] for row in cords]
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
        melody = generate_melody_from_cord(cord,duration,cord_octave,melody_octave)
        if not isGap:
            instrument.play_chord(cord,random.uniform(0.8,1.0),duration,blocking=False)
            for x in melody:
                instrument.play_note(x[0],random.uniform(0.8,1.0),x[1])
        else:
            wait(1)
    cords = [[(x-12*cord_octave) for x in row] for row in cords]

if __name__=="__main__":
    random.seed(100)
    session = Session(tempo=95)
    # session.print_default_soundfont_presets()
    # session.print_available_midi_output_devices()
    instrument = session.new_part("Guitar Nylon X")
    # instrument = session.new_part("Clean Guitar")
    # instrument = session.new_midi_part("Guitar Nylon X",1)
    random_cord_and_melody(instrument,2,3)
    # session.print_default_soundfont_presets()
