import json

class StreamEntry:
    def __init__(self):
        pass
    
    def __str__(self):
        return json.dumps(self.__dict__, indent=3)

