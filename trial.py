import json
import datetime
class Control:
    def __init__(self):
        self.file = "myjson.json"

    def write(self):
        data = self.read()
        data['notes'].append(Notes().__dict__)
        with open("myjson.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(data, indent=2, ensure_ascii=False))
    def read(self):
        with open("myjson.json", "r", encoding="utf-8") as data:
            return json.load(data)
class Notes:
    def __init__(self):
        self.title = "Title"
        self.content = "Content"

# start = Control()
#
# start.read()
# start.write()
#
# #в json должен быть такой массив
# data = {"notes" : []}
# data["notes"].append(Notes().__dict__)
# print(data["notes"])


# current_date = datetime.date.today().isoformat()
# print(current_date)
temp = "test"
with open("myjson.json", "r", encoding="utf-8") as file:
    data = json.load(file)
for i in data['notes']:
    if i.get(f"{temp}"):
        print(i)