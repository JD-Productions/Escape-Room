import json, os
from datetime import datetime as date

def intinput(question=""):
    answer = input(question)
    try:
        int(answer)
        return int(answer)
    except:
        pass

def get_time():
    """get_time() :
    gets the current day and time and returns it as a string"""
    today = str(date.now()).split('.')[0]
    today = today.replace(" ", "-")
    return today

def get_saves():
    path = os.getcwd() + "/Saves"
    saves = [json_data for json_data in os.listdir(path) if json_data.endswith('.json')]
    for save in list(enumerate(saves)):
        num = save[0]
        saves[num] = save[1]
    return saves

def add_save(save):
    saves = get_saves()
    saves.append(save)

def _reset_save(save):
    setup = {
    "room": 0,
    "inventory": []
    }
    fname = get_time()
    with open(f"Saves/{save}.json", "w") as file:
        json.dump(setup, file)
        print(f"USER {save.upper()} HAS BEEN RESET")

def dialogue(name=""):
    name += ".txt"
    path = os.getcwd() + "/Dialogue"
    names = [name for name in os.listdir(path) if name.endswith('.txt')]
    if name not in names:
        raise ValueError()
    with open(name, "r") as file:
        print(file)

class Db:
    def __init__(self, save):
        self.save = save
        if save not in get_saves():
            add_save(save)
        self.setup = {
        "room": 0,
        "inventory": []
        }
        self.path = f"Saves/{self.save}.json"
        self.create_save_file()

    def create_save_file(self, overwrite=False):
        try:
            with open(self.path, "x") as file:
                json.dump(self.setup, file)
        except FileExistsError:
            if overwrite:
                with open(self.path, "w") as file:
                    json.dump(self.setup, file)
            else:
                pass
    
    def get_file(self):
        with open(self.path, "r") as file:
            save = json.load(file)
            return save
    
    def save_file(self, save):
        with open(self.path, "w") as f:
            json.dump(save, f)
    
    def add_item(self, item):
        save = self.get_file()
        if save["inventory"].get(item[0]):
             save["inventory"][item[0]] += item[1]
        else:
            save["inventory"][item[0]] = item[1]
        print(f"add {save}")
        self.save_file(save)
    
    def remove_item(self, item):
        with open(f"{self.save}.json") as file:
            save = json.load(file)
            try:
                save['inventory'].remove(item)
                self.save_file(save)
            except:
                raise

def choose_save():
    saves = get_saves()
    while True:
        print("Type the number for the save")
        i = 1
        for save in list(enumerate(saves)):
            print(f"[{i}] {save}")
            i += 1
        i -= 1
        save = intinput()
        if save == 0:
            name = input("User Name: ").strip().title()
            Db(name)
            return name
        if type(save) == int:
            if save <= i:
                save = saves[save-1]
                break
    return save
