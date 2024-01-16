import json, os
from datetime import datetime as date
import tkinter as tk

def get_time():
    """get_time() :
    gets the current day and time and returns it as a string"""
    today = str(date.now()).split('.')[0]
    today = today.replace(" ", "-")
    today = today.replace(":", "_")
    today = today[:-3]
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
    with open(f"Saves/{fname}.json", "w") as file:
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


def intinput(question=""):
    answer = input(question)
    try:
        int(answer)
        return int(answer)
    except:
        pass


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
        print(self.path)
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

button_name = ""

def button_clicked(window, text):
    global button_name
    button_name = text + '.json'
    button_name = button_name.replace(" ", "-").replace(":", "_")
    print(text)
    window.destroy()

def show_choices(choices):
    window = tk.Tk()
    window.overrideredirect(True)
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    window.geometry("300x400+%d+%d" % (width/2-150, height/2-200))
    window.resizable(False, False)
    window.title("Select Save")
    title = tk.Label(window, text="Select Save:", font= ('Aerial 17 bold'))
    title.pack(padx=20, pady=20)
    buttons = []
    for choice in choices:
        print(choice)
        text = choice[1].replace("_", ":").replace("-", " ").split('.')[0]
        buttons.append(tk.Button(
            window,
            text=text,
            font=('Aerial 15 bold')))
        buttons[len(buttons)-1].pack(padx=20, pady=20)
        buttons[len(buttons)-1]['command'] = lambda text=text: button_clicked(window, text)
    window.mainloop()
    return button_name.split('.')[0]

def choose_save():
    saves = get_saves()
    choices = list(enumerate(saves))
    if len(choices) == 0:
        return "NEW PLAYER"
    else:
        save = show_choices(choices)
    return save