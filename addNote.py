import datetime, json, uuid


class AddNote(object):


    def __init__(self):

        title_note = input("Введите заголовок заметки: ")
        body_note = input("Введите тело заметки: ")
        note_time = str(datetime.datetime.now())
        data_note = {}
        ID = str(uuid.uuid4())
        data_note[ID] = []
        data_note[ID].append({
            'Заголовок' : title_note,
            'Тело' : body_note,
            'Время создания' : note_time,
            'Время изменения' : note_time
        })

        with open('notes.json', 'a', encoding='utf-8') as outfile:
            json.dump(data_note, outfile)
            outfile.write('\n')
