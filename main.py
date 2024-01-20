import database as db
import tkinter as tk
from room import get_room

def hover(event):
    """Called when mouse hovers over a button"""
    event.widget.config(bg="#39FF14", fg="black")

def normal(event):
    """Called when mouse leaves button's space"""
    event.widget.config(bg="black", fg="#39FF14")

def clicked(event):
    """Called when mouse clicks on button"""
    global buttons
    global window
    global entry
    global text
    global room
    global save
    widget = event.widget # Name of widget
    if str(widget) == ".!button4": # If it is the INSPECT button
        e = entry.get().lower().strip()
        print(e)
        entry.delete(0, tk.END)
        if e in room['unlockables'].keys() and room['unlockables'][e][0] not in save.get_file()['inventory']:
            # If e is in the unlockables dictionary
            # and what is in that dictionary isn't in our inventory
            for item in room['unlockables'][e]:
                # Each item in that dictionary
                data = room['unlocks'][item] # Get the text for that item to replace
                save.add_item(item) # Add the item to our inventory
                for i in data:
                    room['interactions'][i] = data[i] # Change the item's text
            room['unlockables'].pop(e) # Remove the item from the list of unlockables so it doesn't run again
        try:
            a = room['interactions'][e] # Text for that item
            text['text'] = a # Change the tk label's text to a
        except:
            print(e)
            print(f"Error for \"{e}\"") # I'm still figuring this part out
    elif str(widget) == ".!button5": # If it is the UNLOCK button
        e = entry.get().lower().strip()
        code = room['code']
        if e == 'door':
            text['text'] = "Enter the code:"
        else:
            try:
                # This try is in case of e not being an intiger
                if int(e) == code:
                    save.change_room()
                    print("hello")
                    if int(save.room_number()) < 5: # TODO: If we add more than 5 rooms, change this number.
                        text['text'] = "You did it! You unlocked the door! You open the door to find... yet another room."
                        room = get_room(save.room_number()+1)
                    else:
                        text['text'] = "You did it! You unlocked the door! You open the door to find... yet another room..............................\nTHE END."
                        # TODO: CUTSCENE. (NOT IN DEMO)
                elif int(e) != code:
                    text['text'] = "Incorrect Code Try again."
            except:
                pass
    elif str(widget) == ".!button6":
        inv = "\n,".join(save.get_file()['inventory'])
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
    
    
