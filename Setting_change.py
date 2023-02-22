key_number = {'C':0, 'C#':1, 'D':2, 'D#':3, 'E':4, 'F':5, 'F#':6, 'G':7, 'G#':8, 'A':9, 'A#':10, 'B':11}

def change_scale(cords,notes,old_scale,new_scale):
    '''
    return [key,cords,notes]
    '''
    key = old_scale
    global key_number
    new_scale = key_number[new_scale.upper()]
    cords = [[((new_scale-key)+x) for x in row] for row in cords]
    notes = [(new_scale-key)+note for note in notes]
    key = new_scale
    return [key,cords,notes]

def change_cord_octave(cords,old_octave,new_octave):
    '''
    return [cord_octave,cords]
    '''
    cord_octave = old_octave
    cords = [[(12*(new_octave-cord_octave)+x) for x in row] for row in cords]
    cord_octave = new_octave
    return [new_octave,cords]

def change_note_octave(notes,old_octave,new_octave):
    '''
    return [note_octave,notes]
    '''
    note_octave = old_octave
    notes = [12*(new_octave-note_octave)+note for note in notes]
    note_octave = new_octave
    return [new_octave,notes]
