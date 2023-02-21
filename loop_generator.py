from piano import *
def random_loop(instrument, length=4,cord_octave=3,melody_octave=4):
    loop = []
    cords = [[12,16,19],[14,17,21],[16,19,23],[17,21,24],[19,23,26],[21,24,28]]
    cords = [[(12*cord_octave+x) for x in row] for row in cords]
    indexs = [x for x in range(len(cords))]
    cord_prob = generate_prob([15,10,10,10,15,10])
    durations = [1,2,4]
    prob2 = generate_prob([2,8,12])
    prev = 0
    index = 0
    looplen = 0
    loop_cords = []
    while looplen!=length:
        while index==prev:
            index = random.choice(indexs,p=cord_prob)
        prev = index
        cord = cords[index]
        duration = random.choice(durations,p=prob2)
        looplen+=duration
        if looplen>length:
            looplen-=duration
        else:
            loop_cords.append([cord,duration])
    loop = []
    for cord in loop_cords:
        loop.append({'cord':cord,'melody':generate_melody_from_cord(cord[0],cord[1],cord_octave,melody_octave)})

    return loop

def play_loop(instrument,loop):
    for item in loop:
        cord = item['cord']
        melody = item['melody']
        instrument.play_chord(cord[0],random.uniform(0.8,1.0),cord[1],blocking=False) 
        for note in melody:
            instrument.play_note(note[0],random.uniform(0.8,1.0),note[1]) 

if __name__=="__main__":
    # random.seed(100)
    session = Session(tempo=95)
    # session.print_default_soundfont_presets()
    # session.print_available_midi_output_devices()
    # instrument = session.new_part("Guitar Nylon X")
    # instrument = session.new_part("Clean Guitar")
    instrument = session.new_midi_part("Guitar Nylon X",1)
    # random_song(instrument,2,4)
    loop = random_loop(instrument, length=12,cord_octave=2,melody_octave=4)
    print(loop)
    while True:
        play_loop(instrument,loop)