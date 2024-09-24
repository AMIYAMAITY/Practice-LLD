from typing import TYPE_CHECKING
import models.user as Cuser
# from models.user import User

from datetime import datetime

class Comment:
    def __init__(self, user: 'User', content : str):
        self.user = user
        self.content = content
        self.creation_datetime = datetime.now()