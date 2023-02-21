from scamp import *
import random


def play_random_notes(instrument,octave=3):
    pitches = [12,14,16,17,19,21,23,24]
    pitches = [12*octave+pitch for pitch in pitches]
    while True:
        pitch = random.choice(pitches)
        instrument.play_note(pitch,1.0,0.25)

def play_sargam(instrument,octave=3):
    pitches = [12,14,16,17,19,21,23,24]
    pitches = [12*octave+pitch for pitch in pitches]
    while True:
        for pitch in pitches:
            instrument.play_note(pitch,1.0,2)

def random_melody(instrument, octave=3):
    pitches = [12,14,16,17,19,21,23,24]
    pitches = [12*octave+pitch for pitch in pitches]
    long_durations = [0.5,0.75,1.0]
    while True:
        test_number = random.random()
        if test_number < 0.2:
            instrument.play_note(random.choice(pitches),random.uniform(0.7,1.0),0.25)
        elif test_number<0.9:
            instrument.play_note(random.choice(pitches),random.uniform(0.7,1.0),random.choice(long_durations))
        else:
            wait(random.choice(long_durations))

if __name__=="__main__":
    # session = Session()
    random.seed(115)
    session = Session(tempo=95)
    # default tempo is 60bpm
    # session.print_default_soundfont_presets()
    # instrument = session.new_part("clarinet")
    # instrument = session.new_part("piano")
    # instrument = session.new_part("guitar")
    # instrument = session.new_part("Sitar")
    # instrument = session.new_part("Organ 2")
    # instrument = session.new_part("Banjo")
    instrument = session.new_part("Guitar Nylon X")
    # instrument = session.new_part("flute")
    # instrument = session.new_part("oboe")
    # instrument.play_note(60, 1, 2.0)
    # play_random_notes(instrument)
    random_melody(instrument)
    # while True:
    #     instrument.play_chord([48,52,55],1.0,2.0)
    # piano1  = session.new_part("Piano")
    # # pitches = [64,66,71,73,74,66,64,73,71,66,74,73]
    # pitches = [48,50,52,53,55,57,59,60]
    # # play_sargam(piano1,2)
    # play_random_notes(piano1,4)
    # piano1.play_note()




# [48,50,52,53,55,57,59,60]
# C3 = 48
# D3 = 50