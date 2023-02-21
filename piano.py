from scamp import *
# import random
from numpy import random
import threading
import multiprocessing 
# multiprocessing.set_start_method('spawn')

def generate_prob(weights):
    sum = 0
    for x in weights:
        sum+=x
    div = sum
    sum = 0
    for i in range(len(weights)):
        weights[i] = round(weights[i]/div,2)
        sum+=weights[i]
    # print(sum)
    sum = round(1.00-sum,2)
    # print(sum)
    weights[0] = weights[0]+sum
    return weights

def play_sargam(instrument,octave=3):
    pitches = [12,14,16,17,19,21,23,24]
    pitches = [12*octave+pitch for pitch in pitches]
    while True:
        for pitch in pitches:
            instrument.play_note(pitch,1.0,2)

def random_melody(instrument, octave=3):
    pitches = [5,7,9,11,12,14,16,17,19,21,23,24,26,28,29]
    prob = generate_prob([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5])
    pitches = [12*octave+pitch for pitch in pitches]
    durations = [0.25,0.5,0.75,1.0,2.0]
    prob2 = generate_prob([5,40,20,35,5])
    prev = pitches[0]
    pitch = pitches[0]
    while True:
        while prev-pitch>6 or prev==pitch:
            pitch = random.choice(pitches,p=prob)
        prev = pitch
        duration = random.choice(durations,p=prob2)
        isGap = random.choice([True,False],p=(0.10,0.90))
        if not isGap:
            instrument.play_note(pitch,random.uniform(0.8,1.0),duration)
        else:
            wait(duration)

def random_melody2(instrument, octave=3):
    pitches = [5,7,9,11,12,14,16,17,19,21,23,24,26,28,29]
    prob = generate_prob([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5])
    pitches = [12*octave+pitch for pitch in pitches]
    durations = [0.25,0.5,0.75,1.0,2.0]
    prob2 = generate_prob([1,40,20,35,1])

    while True:
        pitch = random.choice(pitches,p=prob)
        duration = random.choice(durations,p=prob2)
        isGap = random.choice([True,False],p=(0.05,0.95))
        if not isGap:
            instrument.play_note(pitch,random.uniform(0.8,1.0),duration)
        else:
            wait(duration)

def random_cord(instrument, octave=3):
    # cords = [[12,16,19],[14,17,21],[16,19,23],[17,21,24],[19,23,26],[21,24,28],[23,26,29]]
    cords = [[12,16,19],[14,17,21],[16,19,23],[17,21,24],[19,23,26],[21,24,28]]
    prob = generate_prob([15,10,10,10,15,10])
    cords = [[(12*octave+x) for x in row] for row in cords]
    indexs = [x for x in range(len(cords))]
    durations = [1,2,4]
    prob2 = generate_prob([1,5,10])
    prev = 0
    index = 0
    while True:
        while index==prev:
            index = random.choice(indexs,p=prob)
        prev = index
        cord = cords[index]
        duration = random.choice(durations,p=prob2)
        isGap = random.choice([True,False],p=(0.05,0.95))
        # print(cord[0])
        if not isGap:
            instrument.play_chord(cord,random.uniform(0.8,1.0),duration)
        else:
            wait(duration)

# incomplete function 
# aim is to join bass cord and melody together 
def generate_melody_from_cord(cord,duration,cord_octave=3, melody_octave=4):
    # pitches = [5,7,9,11,12,14,16,17,19,21,23,24,26,28,29]
    # prob = generate_prob([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5])
    # pitches = [12*octave+pitch for pitch in pitches]
    pitches = [12*(melody_octave-cord_octave)+pitch for pitch in cord]
    prob = generate_prob([40,30,30])
    durations = [0.25,0.5,0.75,1.0,2.0]
    prob2 = generate_prob([1,40,20,35,1])
    melody = []
    length = 0
    while length!=duration:
        pitch = random.choice(pitches,p=prob)
        x = random.choice(durations,p=prob2)
        length+=x
        if length>duration:
            length-=x
        else:
            melody.append([pitch,x])
    return melody

    
def random_song(instrument,cord_octave=3, melody_octave=4):
    cords = [[12,16,19],[14,17,21],[16,19,23],[17,21,24],[19,23,26],[21,24,28]]
    cords = [[(12*cord_octave+x) for x in row] for row in cords]
    indexs = [x for x in range(len(cords))]
    cord_prob = generate_prob([15,10,10,10,15,10])
    durations = [1,2,4]
    prob2 = generate_prob([1,5,10])
    prev = 0
    index = 0
    while True:
        while index==prev:
            index = random.choice(indexs,p=cord_prob)
        prev = index
        cord = cords[index]
        duration = random.choice(durations,p=prob2)

        isGap = random.choice([True,False],p=(0.05,0.95))
        melody = generate_melody_from_cord(cord,duration,cord_octave,melody_octave)
        if not isGap:
            instrument.play_chord(cord,random.uniform(0.8,1.0),duration,blocking=False)
            for x in melody:
                instrument.play_note(x[0],random.uniform(0.8,1.0),x[1])
        else:
            wait(1)




if __name__=="__main__":
    # session = Session()
    # random.seed(234)
    # seed(13)
    session = Session(tempo=110)
    # default tempo is 60bpm
    # session.print_default_soundfont_presets()
    # instrument = session.new_part("clarinet")
    instrument1 = session.new_part("piano")
    instrument2 = session.new_part("piano")
    # instrument = session.new_part("guitar")
    # instrument = session.new_part("Sitar")
    # instrument = session.new_part("Organ 2")
    # instrument = session.new_part("Banjo")
    # instrument = session.new_part("Guitar Nylon X")
    # instrument = session.new_part("flute")
    # instrument = session.new_part("oboe")
    # instrument.play_note(60, 1, 2.0)
    # play_random_notes(instrument)
    # print(generate_melody_from_cord([12,16,19],4.0,3))

    # random_melody(instrument1,3)
    # random_cord(instrument1,2)
    random_song(instrument1,cord_octave=3, melody_octave=4)
    # solve()
    




# [48,50,52,53,55,57,59,60]
# C3 = 48
# D3 = 50

# 1, 3, 5- give more priority
# 4, 7 note omit if want happy 

# 1, 5 cord weight more
