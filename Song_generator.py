from Loop_generator import *
if __name__=="__main__":
    # random.seed(100)
    session = Session(tempo=95)

    instrument = session.new_midi_part("Guitar Nylon X",1)

    hook = random_loop(length=8,cord_octave=2,melody_octave=4)
    bridge = random_loop(length=4,cord_octave=2,melody_octave=4)
    antra1 = random_loop(length=12,cord_octave=2,melody_octave=4)
    antra2 = random_loop(length=12,cord_octave=2,melody_octave=4)
    
    play_loop(instrument, antra1)
    play_loop(instrument, antra1)
    play_loop(instrument, hook)
    play_loop(instrument, hook)
    play_loop(instrument, hook)
    play_loop(instrument, hook)
    play_loop(instrument, antra2)
    play_loop(instrument, antra2)
    play_loop(instrument, bridge)
    play_loop(instrument, hook)
    play_loop(instrument, hook)
    play_loop(instrument, hook)
    play_loop(instrument, hook)
