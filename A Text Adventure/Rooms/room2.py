from ran import c as cod

c = []

for i in cod:
    c.append(i)

words = """
	
	Good Job! You thought logically and opened the door. That was simple. This room, however, will not be as easy.
    You will have to be smart and logical. There is a four-digit code to unlock the door. Go find it.

    Good Luck...
	
"""

room_num = 2

room = [
    'Room 2',
    "A strange room, you don't recognize it. You are sitting on a mattress. There is a table beside you, a bucket on the floor in the corner, and a door."
    ]

items = {
    "bucket": f"\nAs you pick up the bucket, you notice a little number {c[3]} on it."
}

unlockables_items = {
    "paper": "There is literally nothing special about the paper.",
    "calculator": f"\nAs you pick up the calculator, you notice something on the front. It reads {c[2]}",
    "note": f"\nAs you pick up the note, you notice a little number {c[0]} written on it."
}

interactions = {
    "table": "You walk over to the table. There is a note and calculator on top. You check under the table. There is a piece of paper.",

    "door": "You walk up to the door, only to find a padlock woth 4 digits. Sounds like you need to find the code...",
	
	"clock": f"You look at the clock on the wall. It's normal. Except, it isn't ticking! The clock's time is {c[1]}:00.",
	
	"bucket": f"There is a bucket on the ground. You look inside and see the number {c[3]} engraved into the bottom.",

    "mattress": "You are sitting on a stained, old, bed mattress. I'ts honestly not very comfortable"
    }

choices = [
    "Inspect or X: {0}",
    "Unlock: Door",
    "Take {0}"
    ]

doorcode = 4

unlockables = {
    "table": {
        "note": """You read the note on the table. It reads: {words}	In the corner of the note, is a small number {number}""".format(words=words, number=c[0]),

        "calculator": f"There's a calculator on the table. It reads the number {c[2]} on it.",

	    "paper": f"You crawl under tbe table and look at the piece of paper. It says, \n\tOrder:\nNote :: 1\nClock :: 2\nCalculator :: 3\nBucket :: 4"
    }
}