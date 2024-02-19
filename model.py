import json
import view
# save read date show add edit delete information
import datetime

class My_function:

    def save_function(self, note_title, note_content):
        self.title = note_title
        self.content = note_content

        # read file
        with open("myjson.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        current_date = datetime.date.today().isoformat()

        # write file
        data['notes'].append({"title": self.title, "content": self.content, "date": current_date})
        with open("myjson.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(data, indent=2, ensure_ascii=False))

        start = view.Show_information(f"заметка {note_title} успешно сохранена!")
        return start.show_point()

    def read_function(self):
        with open("myjson.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def date_function(self):
        data = self.read_function()
        data = sorted(data['notes'], key=lambda note: note['date'])
        return data

    def show_function(self):
        view.Show_information("ввведите название заметки которую хотите отоброзить")
        choice = input("название: ")
        if choice == "":
            start = view.Show_information("")
            return start.show_point()

        data = self.date_function()
        result = []
        for i in data:
            for k, v in i.items():
                if v == choice:
                    result.append(i)
        if len(result):
            for el in result:
                view.Show_information(f"{el}")
        else:
            view.Show_information("такой заметки нет")
        start = view.Show_information("")
        return start.show_point()

    def show_all_function(self):
        view.Show_information("Вывод всех заметок")
        data = self.date_function()
        for i in data:
            view.Show_information(i)
        start = view.Show_information("")
        return start.show_point()

    def add_function(self):
        print(" что бы добавить новую заметку, сначала введите заголовок заметки, после её содержание. ")
        note_title = input("введите заголовок заметки: ")
        note_content = input("введите содержание заметки: ")

        if note_content == "" or note_title == "":
            start = view.Show_information("")
            return start.show_point()

        return self.save_function(note_title, note_content)

    def edit_function(self):
        view.Show_information("ввведите название заметки которую хотите редактировать")
        choice = input("название: ")
        if choice == "":
            start = view.Show_information("")
            return start.show_point()

        data = self.date_function()
        result = []
        for i in data:
            for k, v in i.items():
                if v == choice:
                    result.append(1)
                    i['content'] = input(f"Введите новые данные для заметки {choice}: ")

        if len(result):
            view.Show_information(f"заметка {choice} успешно изменена!")
        else:
            view.Show_information("такой заметки нет")

        with open("myjson.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(data, indent=2, ensure_ascii=False))

        start = view.Show_information("")
        return start.show_point()

    def delete_function(self):
        # view.Show_information("ввведите название заметки которую хотите удалить")
        # choice = input("название: ")
        # data = self.date_function()
        # result = []
        # for i in data:
        #     for k, v in i.items():
        #         if v == choice:
        #             print(i)
        #             del data[i]
        #             result.append(1)

        # if len(result):
        #     view.Show_information(f"заметка {choice} успешно удалена!")
        # else:
        #     view.Show_information("такой заметки нет")
        #
        # with open("myjson.json", "w", encoding="utf-8") as file:
        #     file.write(json.dumps(data, indent=2, ensure_ascii=False))
        #
        start = view.Show_information("")
        return start.show_point()

