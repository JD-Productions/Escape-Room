import tkinter as tk
import database
from PIL import ImageTk, Image
from time import sleep
import main

image1 = Image.open("media/splash_screen.png")

new = database.is_new_player() # Returns a bool
save = database.Db()

window = tk.Tk() # The tk window
window.title("Escape Room")
window.config(bg="black")
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
pic_width = image1.width
pic_height = image1.height
image1 = image1.resize((pic_width*2, pic_height*2))
window.geometry("%dx%d" % (width, height))
test = ImageTk.PhotoImage(image1)
label1 = tk.Label(image=test)
label1.image = test
label1.config(bg="black")
label1.pack()

label2 = tk.Label()
label2['font'] = "terminal 25"
label2['bg'] = 'black'
label2['fg'] = "#39FF14"

text="Hello.\nYou are in a place where time and space are irrelevent.\nYou are in a place where anything is possible.\nA place where you can be you.\nWelcome, to the Escape Room."

def splash_screen():
    label1.destroy()


def intro():
    global text
    global label2
    label2.place(relx = 0.5, rely = 0.5, anchor = 'center')
    t = ""
    for char in text:
        t += char
        label2.config(text=t)
        label2.update()
        sleep(0.15)
    sleep(4)
    label2.destroy()

buttons = []

def Button(text):
    """Creates a tk.Button object and returns it."""
    button = tk.Button(text=text, font="terminal 30", bg="black", fg="#39FF14")
    return button

def hover(event):
    """Called when the mouse hovers over the button"""
    event.widget.config(bg="#39FF14", fg="black")

def normal(event):
    """Called when the mouse leaves the button's space"""
    event.widget.config(bg="black", fg="#39FF14")

def clicked(event):
    """Called when button is clicked"""
    global buttons
    global window
    widget = event.widget
    if str(widget) == ".!button":
        for button in buttons:
            button.destroy()
        title.destroy()
        main.play(window)
    elif str(widget) == ".!button2":
        pass
        #options.menu()
    elif str(widget) == ".!button3":
        pass
        #main.credit()

def title_screen():
    """Sets up and shows the title screen"""
    global buttons
    global title
    title = tk.Label(text="Escape Room", font="terminal 50", bg="black", fg="#39FF14")
    title.pack(pady=50)
    play = Button("PLAY")
    buttons.append(play)
    play.pack(pady=50)
    options = Button("OPTIONS")
    buttons.append(options)
    options.pack()
    credit = Button("CREDITS")
    buttons.append(credit)
    credit.pack(pady=50)
    for button in buttons:
        button.bind("<Button-1>", clicked)
        button.bind("<Enter>", hover)
        button.bind("<Leave>", normal)
    

window.after(5000, splash_screen) # Waits 5,000 milliseconds (5 seconds) then calls splash_screen
window.after(5001, title_screen) # Waits 5,001 milliseconds then calls title_screen
window.mainloop() # Starts a loop to check for events