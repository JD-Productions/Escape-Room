import json, os
import tkinter as tk

def is_new_player():
    try:
        with open("save.json", "r") as f:
            return False
    except FileNotFoundError:
        return True


def add_save(save):
    saves = get_saves()
    saves.append(save)


def _reset_save(save):
    setup = {
    "room": 1,
    "inventory": []
    }
    with open(f"save.json", "w") as file:
        json.dump(setup, file)
        print(f"GAME HAS BEEN RESET")


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
    def __init__(self):
        self.path = "save.json"
        new = is_new_player()
        self.setup = {
        "room": 1,
        "inventory": []
        }
        if new:
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
                print("Error: You messed up somewhere.")
    
    def get_file(self):
        with open(self.path, "r") as file:
            save = json.load(file)
            return save
    
    def room_number(self):
        save = self.get_file()
        room = save['room']
        return room
    
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
        save = self.get_file()
        try:
            save['inventory'].remove(item)
            self.save_file(save)
        except:
            raise

button_name = ""