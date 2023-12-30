import random

doorcodes = [0, 0, 4]

class Run:
    def __init__(self, room_num=1):
        doorcodes = [0, 0, 4]
        self.room_num = room_num
        self.doorcode = doorcodes[room_num]
        self.c = ""
        self.start()

    def write(self, passwd=str):
        with open('ran.py', 'w') as f:
            f.writelines([f"c = '{passwd}'", "\n", f"room = {self.room_num}"])

    def rand(self):
        c = ""
        for i in range(self.doorcode):
            c1 = str(random.randint(0, 9))
            c += c1
        self.c = c
        return c

    def start(self):
        if self.doorcode > 0:
            self.write(self.rand())
        else:
            self.write("0")

if __name__ == "__main__":
    r = Run(1)
