import json

class ReadNote(object):

    def __init__(self):
        cmdRead = 0
        while cmdRead != "end":
            cmdRead = input("Для вывода всех данных - 1, для вывода конкретной заметки по ID - 2, по дате создания - 3: ")

            if cmdRead == "1":
                try:
                    with open('notes.json') as json_file:
                        data = json_file.readlines()
                        #print(data)
                        for p in data:
                            json_str = json.loads(p)
                            for j in json_str:
                                print("ID: " + j)
                                print("Заголовок: " + json_str[f'{j}'][0]['Заголовок'])
                                print("Тело: " + json_str[f'{j}'][0]['Тело'])
                                print("Время создания: " + json_str[f'{j}'][0]['Время создания'])
                                print("Время изменения: " + json_str[f'{j}'][0]['Время изменения'])
                                print()
                except Exception as e:
                    print(e)


            elif cmdRead == "2":
                usr_id_input = input("Введите ID: ")
                try:
                    with open('notes.json') as json_file:
                        data = json_file.readlines()
                        for p in data:
                            json_str = json.loads(p)
                            for j in json_str:
                                if j == usr_id_input:
                                    print("ID: " + j)
                                    print("Заголовок: " + json_str[f'{j}'][0]['Заголовок'])
                                    print("Тело: " + json_str[f'{j}'][0]['Тело'])
                                    print("Время создания: " + json_str[f'{j}'][0]['Время создания'])
                                    print("Время изменения: " + json_str[f'{j}'][0]['Время изменения'])
                                    print()
                except Exception as e:
                    print(e)


            elif cmdRead == "3":
                usr_id_input = input("Введите дату (создания) в формате гггг-мм-дд: ")
                try:
                    with open('notes.json') as json_file:
                        data = json_file.readlines()
                        for p in data:
                            json_str = json.loads(p)
                            for j in json_str:
                                if usr_id_input in json_str[f'{j}'][0]['Время создания']:
                                    print("ID: " + j)
                                    print("Заголовок: " + json_str[f'{j}'][0]['Заголовок'])
                                    print("Тело: " + json_str[f'{j}'][0]['Тело'])
                                    print("Время создания: " + json_str[f'{j}'][0]['Время создания'])
                                    print("Время изменения: " + json_str[f'{j}'][0]['Время изменения'])
                                    print()
                except Exception as e:
                    print(e)


