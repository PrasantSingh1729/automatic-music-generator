from piano import *
if __name__=="__main__":
    random.seed(54)
    session = Session(tempo=95)
    # session.print_default_soundfont_presets()
    # session.print_available_midi_output_devices()
    instrument = session.new_part("Guitar Nylon X")
    # instrument = session.new_midi_part("Guitar Nylon X",1)
    random_song(instrument,2,4)