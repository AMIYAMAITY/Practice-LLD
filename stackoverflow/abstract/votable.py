from abc import ABC, abstractmethod
from models.comment import Comment
# from models.user import User

class Votable(ABC): #abstract base classes (ABC)
    
    @abstractmethod
    def vote(self, user: 'User', value : int):
        pass

    @abstractmethod
    def get_vote_count(self) -> int:
        pass