import time

class LogMessage:
    def __init__(self, level, message) -> None:
        self.level = level
        self.message = message
        self.timestamp = time.time()
    
    def __str__(self) -> str:
        return f"[{self.level.name}] : [{self.timestamp}] : [{self.message}]"