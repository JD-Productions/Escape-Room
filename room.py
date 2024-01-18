import json

def get_room(room_num):
    with open(f"rooms/room{room_num}.json", "r") as file:
        room_data = json.load(file)
    return room_data

if __name__=='__main__':
    get_room(1)