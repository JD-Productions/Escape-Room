try:
    import Rooms.room2
    room = Rooms.room2
except:
    try:
        import Rooms.room1
        room = Rooms.room1
    except:
        pass