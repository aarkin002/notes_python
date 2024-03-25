import json

class DeleteNote(object):

    def __init__(self):
        cmdRead = 0
        while cmdRead != "end":
             cmdRead = input("Для удаления заметки введите ее ID: ")
             try:
                 with open('notes.json', 'r') as json_file_read:
                     data = json_file_read.readlines()
                 with open('notes.json', 'w') as json_file:
                     for p in data:
                         if cmdRead not in p:
                             json_file.write(p)
                     print("Удалено")
                     break
             except Exception as e:
                 print(e)
