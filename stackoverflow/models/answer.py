from typing import List, TYPE_CHECKING
# from models.user import User
# import models.user as Cuser

# import models.question as Cquestion
# from models.question import Question

from models.vote import Vote
from models.comment import Comment
from datetime import datetime
from abstract.commentable import Commentable
from abstract.votable import Votable

class Answer(Commentable, Votable):
    def __init__(self, user : 'User', question : 'Question', content : str) -> None:
        self.id = id(self)
        self.author = user
        self.question = question
        self.content = content
        self.comments: List[Comment] = []
        self.votes: List[Vote] = []
        self.creation_datetime = datetime.now()
        self.is_accepted = False
    
    def vote(self, user: 'User', value : int) -> None:
        if value not in [-1, 1]:
            raise ValueError("Vote value must be 1 or -1")

        for vote in self.votes:
            if vote.user == user:
                raise ValueError("This user already given a vote for same answer")

        self.votes.append(Vote(user, value))
        self.author.update_reputation(value * 10)

    def get_vote_count(self) -> int:
        return sum(v.value for v in self.votes)

    def add_comment(self, comment : Comment):
        self.comments.append(comment)
    
    def accept(self):
        if not self.is_accepted:
            self.is_accepted = True
            self.author.update_reputation(15)

    def get_comments(self) -> List[Comment]:
        return self.comments.copy()

