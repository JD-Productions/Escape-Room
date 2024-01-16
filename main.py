import tkinter as tk
import database
from PIL import ImageTk, Image
from time import sleep

image1 = Image.open("media/splash_screen.png")

name = database.choose_save()
if name == "NEW PLAYER":
    name = database.get_time()
save = database.Db(name)

window = tk.Tk()
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

def intro():
    label1.destroy()
    label2.place(relx = 0.5, rely = 0.5, anchor = 'center')
    sleep(1)

def intro2():
    global text
    global label2
    t = ""
    for char in text:
        print(char)
        t += char
        label2.config(text=t)
        label2.update()
        sleep(0.1)

window.after(5000, intro)
window.after(7000, intro2)

window.mainloop()