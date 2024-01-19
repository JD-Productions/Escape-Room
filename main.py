import database as db
import tkinter as tk
from room import get_room

def hover(event):
    event.widget.config(bg="#39FF14", fg="black")

def normal(event):
    event.widget.config(bg="black", fg="#39FF14")

def clicked(event):
    global buttons
    global window
    global entry
    global text
    global room
    global save
    widget = event.widget
    if str(widget) == ".!button4":
        e = entry.get().lower().strip()
        print(e)
        entry.delete(0, tk.END)
        if e in room['unlockables'].keys() and room['unlockables'][e][0] not in save.get_file()['inventory']:
            for item in room['unlockables'][e]:
                data = room['unlocks'][item]
                save.add_item(item)
                for i in data:
                    room['interactions'][i] = data[i]
            room['unlockables'].pop(e)
        try:
            a = room['interactions'][e]
            text['text'] = a
        except:
            print(e)
            print(f"Error for \"{e}\"")
    elif str(widget) == ".!button5":
        e = entry.get().lower().strip()
        if e == 'door':
            code = room['code']
            text['text'] = "Enter the code:"
        else:
            code = room['code']
            try:
                if int(e) == code:
                    text['text'] = "You did it! You unlocked the door! You open the door to find... yet another room."
                    save.change_room()
                    room = get_room(save.room_number()+1)
                elif int(e) != code:
                    text['text'] = "Incorrect Code Try again."
            except:
                pass
    elif str(widget) == ".!button6":
        inv = save.get_file()['inventory']
        text['text'] = inv


def Button(text):
    button = tk.Button(text=text, font="terminal 30", bg="black", fg="#39FF14")
    button.bind("<Enter>", hover)
    button.bind("<Leave>", normal)
    button.bind("<Button-1>", clicked)
    return button


def play(window):
    global entry
    global text
    global room
    global save
    length = window.winfo_screenwidth()
    save = db.Db()
    room_num = save.room_number()
    room = get_room(room_num)
    text = tk.Label(wraplength=length-50, justify="center", text="", font="terminal 30", bg="black", fg="#39FF14")
    text.pack(pady="30")
    entry = tk.Entry(bg="black", font="terminal 30", fg="#39FF14")
    entry.pack()
    inspect = Button("INSPECT")
    inspect.pack(pady=30)
    unlock = Button("UNLOCK")
    unlock.pack()
    inventory = Button("INVENTORY")
    inventory.pack(pady=30)
    text['text'] = room['intro']
    
    
