from piano import *
if __name__=="__main__":
    random.seed(152)
    session = Session(tempo=95)
    # instrument1 = session.new_part("Guitar Nylon X")
    instrument = session.new_midi_part("Guitar Nylon X",1)
    random_cord(instrument,2)
    