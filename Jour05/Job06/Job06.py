def arrondir_notes(notes):
    notes_arrondies = []
    for note in notes:
        if note < 40:
            notes_arrondies.append(note)
        elif note % 5 >= 3 and note >= 38:
            note_arrondie = (note // 5 + 1) * 5
            notes_arrondies.append(note_arrondie)
        else:
            notes_arrondies.append(note)
    return notes_arrondies
notes = [42, 78, 85, 89, 91, 36, 72, 57]
notes_arrondies = arrondir_notes(notes)
print(notes_arrondies)