
from logger_adapter import Adapter

class FileAdapter(Adapter):

    def __init__(self, file_path) -> None:
        self.file_path = file_path

    def append(self, message):
        with open(self.file_path, "a") as file:
            file.write(str(message) + "\n")
