from typing import TYPE_CHECKING
from models.question import Question
from models.answer import Answer
from models.tag import Tag
from typing import List
# from models.comment import Comment
import models.comment as Ccomment
from abstract.commentable import Commentable

class User:
    def __init__(self, name : str, email_id : str):
        self.name = name
        self.email_id = email_id
        self.questions: List[Question] = []
        self.answers: List[Answer] = []
        self.reputation = 0
        self.comments: List[Ccomment.Comment] = []

    
    def update_reputation(self, num : int) -> None:
        self.reputation += num
        self.reputation = max(self.reputation , 0)

    def ask_question(self, title : str, content : str, tags : List[Tag]) -> Question:
        question = Question(self, title, content, tags)
        self.questions.append(question)
        self.update_reputation(5)
        return question
    
    def answer_question(self, question : Question, content : str) -> Answer:
        answer = Answer(self, question, content)
        self.answers.append(answer)
        question.add_answer(answer)
        self.update_reputation(10)
        return answer


    def comment_on(self, commentable : Commentable, content : str):
        comment = Ccomment.Comment(self, content)
        self.comments.append(comment)
        commentable.add_comment(comment) #This can be for question or answer, depending on the object. That's why commentable is an abstract class. Which question and answer both will define them. 
        self.update_reputation(2)
        return comment
    
    def get_reputation(self) -> int:
        return self.reputation