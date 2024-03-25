import datetime, json

class ChangeNote(object):

    def __init__(self):
        cmdRead = 0
        while cmdRead != "end":
            usr_id_input = input("Введите ID заметки для изменения: ")
            cmdRead = input("Для изменения заголовка 1, для изменения тела 2: ")

            if cmdRead == "1":
                usr_input_z = input("Введите новый заголовок: ")
                try:
                    with open('notes.json', 'r') as json_file_read:
                        data = json_file_read.readlines()
                        for p in data:
                            json_str = json.loads(p)
                            for j in json_str:
                                if j == usr_id_input:
                                    ID = j
                                    body_note = json_str[f'{j}'][0]['Тело']
                                    create_time = json_str[f'{j}'][0]['Время создания']

                    with open('notes.json', 'w') as json_file:
                        for p in data:
                            if usr_id_input in p:
                                note_time = str(datetime.datetime.now())
                                data_note = {}
                                data_note[ID] = []
                                data_note[ID].append({
                                'Заголовок': usr_input_z,
                                'Тело': body_note,
                                'Время создания': create_time,
                                'Время изменения': note_time
                                })
                            else:
                                json_file.write(p)

                    with open('notes.json', 'a', encoding='utf-8') as outfile:
                        json.dump(data_note, outfile)
                        outfile.write('\n')

                except Exception as e:
                    print(e)


            if cmdRead == "2":
                usr_input_t = input("Введите новое тело: ")
                try:
                    with open('notes.json', 'r') as json_file_read:
                        data = json_file_read.readlines()
                        print("test1")
                        for p in data:
                            json_str = json.loads(p)
                            print("test2")
                            for j in json_str:
                                if j == usr_id_input:
                                    print("test3")
                                    id_old = j
                                    note_z_ch_b = json_str[f'{j}'][0]['Заголовок']
                                    create_time =  json_str[f'{j}'][0]['Время создания']

                    with open('notes.json', 'w') as json_file:
                        for p in data:
                            if usr_id_input in p:
                                print("test4")
                                note_time = str(datetime.datetime.now())
                                data_note = {}
                                data_note[id_old] = []
                                data_note[id_old].append({
                                'Заголовок': note_z_ch_b,
                                'Тело': usr_input_t,
                                'Время создания': create_time,
                                'Время изменения': note_time
                                })
                            else:
                                json_file.write(p)
                                print("test5")

                    with open('notes.json', 'a', encoding='utf-8') as outfile:
                        json.dump(data_note, outfile)
                        outfile.write('\n')
                        print("test6")

                except Exception as e:
                    print(e)


