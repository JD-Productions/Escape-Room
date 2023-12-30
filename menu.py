from keybinds import keys
import ran, importlib, rand
import rooms as r
c = ran.c 

def reload():
    importlib.reload(ran)
    importlib.reload(r)
    global c
    c = ran.c

class Room:
    def __init__(self, room=int):
        rom = r.room
        self.interactions = rom.interactions
        self.choices = rom.choices
        self.unlockables = rom.unlockables
        self.unlockables_items = rom.unlockables_items
        self.items = rom.items
        self.room_num = rom.room_num

rooms = Room(ran.room)

class UI:
    def __init__(self):
        self.interactions = rooms.interactions
        self.unlockables = rooms.unlockables
        self.u_items = rooms.unlockables_items
        self.take = rooms.items
        self.unlocked = []
        self.items = []
        self.visited = []

    def view(self):
        print(":: Inventory- [")
        for item in self.items:
            print(item)
        print("]\n")

    def choices(self):
        items = "Inspect: " + ", ".join(self.interactions.keys())
        take = "Take: " + ", ".join(self.take.keys())
        print(items,take, sep="\n")
        del items

    def update(self, key, value):
        self.interactions.update({key, value})
    
    def remove(self, key):
        self.interactions.pop(key)
        self.items.pop(key)
    
    def check_visited(self, area=str):
        print()
        print(self.interactions[area])
        print()
        if area in self.unlockables:
            self.visited.append(area)
            for key, value in self.unlockables[area].items():
                self.interactions.update({key: value})
                self.unlocked.append(key)
                if key in self.u_items.keys():
                    x = self.u_items[key]
                    self.take.update({key: x})
                    del self.u_items[key]
                    del x
            del self.unlockables[area]
            print(f":: Unlocked: {[i for i in self.unlocked]}")

    def check_taken(self, item=str):
        if item in self.take and item in self.interactions:
            print()
            print(self.take[item])
            print()
            self.items.append(item)
            del self.take[item]
            del self.interactions[item]
            print(f":: Took: {item}")
        else:
            print(f":: Cannot take {item}")
            print()

u = UI()

class Menu:
    def __init__(self, room=rooms.room_num):
        self.room = room
        self.win = False
        reload()
        self.ask()

    def choices(self):
        choice = rooms.choices
        choice[0] = choice[0].format(", ".join(list(u.interactions)))
        choice[2] = choice[2].format(", ".join(list(u.take)))
        for i in choice:
            print(i)

    def ask(self, question="What do you do? "):
        while not self.win:
            u.choices()
            text = input(question)
            self.check_keys(text)
		

    def check_keys(self, text):
        text = text.lower().split()
        for key in keys:
            if text[0] in keys[key]:
                self.check_action(key, text)
                break
        else:
            print("Sorry. :< Invalid command.")

    def check_action(self, key, text):
        self.items = u.items
        self.interactions = u.interactions
        if key == 'i':
            if text[1] in self.interactions:
                u.check_visited(text[1])
        
        if key == 't':
            u.check_taken(text[1])
		
        if key == 'v':
            u.view()
		
        def write():
            with open('ran.py', 'w') as f:
                rando = rand.Run()
                f.write(f"c = {str(rando.c)!r}\nroom = {rooms.room_num+1}")
                self.win = True
            reload()

        if key == 'u':
            if 'door' in self.interactions:
                if rand.doorcodes[ran.room] > 0:
                    passwd = input("""You walk up to the door and enter a {0}-digit code, You enter: """.format(rand.doorcodes))
                    print(passwd)
                    if len(passwd) == rand.doorcodes[ran.room] and passwd == c:
                        print("The code worked! You’re free!")
                        write()
                elif rand.doorcodes[ran.room] == 0:
                    print(u.interactions['door'])
                    print("You walk through the open doorway. You're free, for now...")
                    write()


def run():
    room = 0
    while True:
        room += 1
        rand.Run(room)
        Menu(room)
