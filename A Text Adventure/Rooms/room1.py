words = """
	
	Hello, Dear, participant. As you can tell, you are in an unknown room.
"Who are you?" or "Why am I here?" may be a few questions you are asking. I'm Dr. Mac.
Why are you here? Don't worry, you'll find out soon enough...

Good Luck....
	
"""

room_num = 1

room = [
    'Room 1',
    "A room, you don't recognize it. There is a table beside you and a door."
    ]

items = {}

unlockables_items = {
    "note": f"\nYou pick up the note."
}

interactions = {
    "table": "You walk over to the table. There is a note on top",

    "door": "You go to the door. You turn the handle to find it... unlocked? You open the door. Huh, that was easy!"
    }

choices = [
    "Inspect or X: {0}",
    "Unlock: Door",
    "Take {0}"
    ]

doorcode = 0

unlockables = {
    "table": {
        "note": f"You read the note on the table. It reads: {words}"
    }
}