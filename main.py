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
    widget = event.widget


def Button(text):
    button = tk.Button(text=text, font="terminal 30", bg="black", fg="#39FF14")
    button.bind("<Enter>", hover)
    button.bind("<Leave>", normal)
    button.bind("<Button-1>", clicked)
    return button


def play(window):
    save = db.Db()
    room_num = save.room_number()
    room = get_room(room_num)
    text = tk.Label(text="", font="terminal 30", bg="black", fg="#39FF14")
    text.pack(pady="30")
    entry = tk.Entry(bg="black", font="terminal 30", fg="#39FF14")
    entry.pack()
    inspect = Button("INSPECT")
    inspect.pack(pady=30)
    unlock = Button("UNLOCK")
    unlock.pack()
    inventory = Button("UNVENTORY")
    inventory.pack(pady=30)
    #while True:
    text['text'] = room['intro']
    
    