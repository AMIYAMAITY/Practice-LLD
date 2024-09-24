
from logger_adapter import Adapter

class Console(Adapter):

    def append(self, message):
        print(message)