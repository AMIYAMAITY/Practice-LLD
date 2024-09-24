from typing import List, TYPE_CHECKING
# from models.user import User
# import models.user as Cuser

# from models.answer import Answer
import models.answer as Canswer

from models.tag import Tag
from models.vote import Vote
from models.comment import Comment
from datetime import datetime
from abstract.commentable import Commentable
from abstract.votable import Votable

class Question(Commentable, Votable):
    def __init__(self, user: 'User', title : str, content : str, tags : List[Tag]) -> None:
        self.id = id(self)
        self.author = user
        self.title = title
        self.content = content
        self.tags = [Tag(name) for name in tags ]
        self.creating_datetime = datetime.now()
        self.answers: List[Canswer.Answer] = []
        self.votes: List[Vote] = []
        self.comments: List[Comment] = []
    
    def vote(self, user: 'User', value : int) -> None:
        if value not in [-1, 1]:
            raise ValueError("Vote value must be 1 or -1")

        for vote in self.votes:
            if vote.user == user:
                raise ValueError("This user already given a vote for same question")

        self.votes.append(Vote(user, value))
        self.author.update_reputation(value * 5)

    def add_answer(self, answer : Canswer.Answer):
        if answer not in self.answers:
            self.answers.append(answer)

    def get_answers(self):
        return self.answers

    def get_vote_count(self) -> int:
        return sum(v.value for v in self.votes)
    
    def add_comment(self, comment : Comment):
        self.comments.append(comment)
    
    def get_comments(self) -> List[Comment]:
        return self.comments.copy()