from abc import ABC, abstractmethod
from typing import List
from typing import TYPE_CHECKING
from models.comment import Comment

class Commentable(ABC): #abstract base classes (ABC)

    @abstractmethod
    def add_comment(self, comment : Comment):
        pass

    @abstractmethod
    def get_comments(self) -> List[Comment]:
        pass