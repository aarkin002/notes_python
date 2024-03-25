import addNote
import changeNote
import deleteNote
import readNote


cmdNote = 0
uniquieId = 0

while cmdNote != "end":
    cmdNote = input("Введите (английские без ковычек) 'r' для чтения, 'a' для добавления, 'd' для удаления Заметок или 'end', чтобы выйти: ")
    if cmdNote == "end":
        break

    elif cmdNote == "a":
        addNote.AddNote()
        break

    elif cmdNote == "r":
        readNote.ReadNote()
        break

    elif cmdNote == "d":
        deleteNote.DeleteNote()
        break

    elif cmdNote == "e":
        changeNote.ChangeNote()
        break







