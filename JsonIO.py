import json


class jsonReadWrite:
    def __init__(self, fileName):
        self.fileName = fileName
        self.data = None
        self.dataToWrite = None

    def read(self):
        with open(self.fileName, 'r') as f:
            self.data = json.load(f)
            return self.data
        

    def write(self, data):
        self.read()
        self.dataToWrite = data
        with open(self.fileName, 'w') as f:
            json.dump(self.dataToWrite, f, indent=4)

JsonIO = jsonReadWrite("points.json")