title = """
=======]  =========]   =======]     ==     ======   =======]
|         |            |           /  \    |     |  |
|====]     =======    |           /    \   |=====   |====]
|                 |    |         /======\  |        |
=======] [=========    =======] /        \ |        =======]
"""

with open("tutorial.txt", "r") as f:
    text = "".join(f.readlines())

class Start:
    def __init__(self):
        print(title)

    def is_new(self):
        while True:
            new = input("This is a text-adventure game. Would you like a tutorial? Y/N")
            if new.upper() == "N":
                print("No? Ok!")
                break
            elif new.upper() == "Y":
                print(text)
                input()
                break
        print("Alright! Let's get started!\n...\n")
        Intro()


def Intro():
    print("....")
    print("Wa...U...")
    print("Wake Up...")
    print("\nYou wake up. You are in: ")
    print("\n A room. There is a table beside you and a door.")
