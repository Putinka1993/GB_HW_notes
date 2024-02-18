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
        data['notes'].append({self.title: [{"content": self.content, "date": current_date}]})
        with open("myjson.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(data, indent=2, ensure_ascii=False))

        start = view.Show_information(f"заметка {note_title} успешно сохранена!")
        return start.show_point()

    def read_function(self):
        with open("myjson.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def date_function(self):
        pass

    def show_function(self):
        info = view.Show_information("ввведите название заметки которую хотите отоброзить")
        choice = input("название: ")
        data = self.read_function()
        for i in data['notes']:
            if i.get(f"{choice}"):
                print(i)

        # start = view.Show_information(f"вывод всех заметок {self.read_function()}")
        # return start.show_point()

    def show_all_function(self):
        start = view.Show_information(f"вывод всех заметок {self.read_function()}")
        return start.show_point()

    def add_function(self):
        print(" что бы добавить новую заметку, сначала введите заголовок заметки, после её содержание. ")
        note_title = input("введите заголовок заметки: ")
        note_content = input("введите содержание заметки: ")

        return self.save_function(note_title, note_content)

    def edit_function(self):
        pass

    def delete_function(self):
        pass

    def information_function(self):
        pass

