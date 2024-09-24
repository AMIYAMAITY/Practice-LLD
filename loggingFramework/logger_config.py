
class LoggerConfig:
    
    def __init__(self, level, adapter) -> None:
        self.level = level
        self.adapter = adapter
    
    def get_log_level(self):
        return self.level
    
    def set_log_level(self, level : int):
        self.level = level
    
    def get_adapter(self):
        return self.adapter
    
    def set_adapter(self, adapter):
        self.adapter = adapter