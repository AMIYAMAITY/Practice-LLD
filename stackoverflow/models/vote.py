# import models.user as Cuser
# from models.user import User

from datetime import datetime

class Vote:
    def __init__(self, user : 'User', value : int):
        self.user = user
        self.value = value
        self.vote_datetime = datetime.now()