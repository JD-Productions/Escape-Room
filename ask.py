import tkinter as tk

window = tk.Tk()

window.title("ESCAPE GAME")

title = tk.Label(text="ROOM 1")
title.pack()

label = tk.Label()
label.pack()

def answer(text):
    print(text)

def onKeyRelease(event):
    global entry
    if event.keysym == "Return":
        text = entry.get()
        entry.delete(0, tk.END)
        answer(text)

def ask(question="What do you do?"):
    global label
    global entry
    label.configure(text=question)
    entry = tk.Entry()
    entry.bind("<KeyRelease>", onKeyRelease)
    entry.pack()
    inspect = tk.Button(text="Inspect")
    unlock = tk.Button(text="Unlock")
    inventory = tk.Button(text="Inventory")
    inspect.pack()
    unlock.pack()
    inventory.pack()

ask()
window.mainloop()