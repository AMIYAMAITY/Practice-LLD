from typing import Dict
from typing import List
# import models.user as Cuser
from models.user import User

from models.question import Question
from models.answer import Answer
from models.tag import Tag
from abstract.commentable import Commentable

class StackOverflow:

    def __init__(self) -> None:
        self.users: Dict[int, User] = {}
        self.questions: Dict[int, Question] = {}
        self.answers: Dict[int, Answer] = {}
        self.tags: Dict[str, Tag] = {}

    def create_user(self, name: str, emai_id: str) -> User:
        _id = len(self.users) + 1
        self.users[_id] = User(name, emai_id)
        return self.users[_id]
    
    def ask_question(self, user : User, title : str, content : str, tags : List[Tag]) -> Question:
        question = user.ask_question(title, content, tags)
        self.questions[question.id] = question
        for tag in tags:
            self.tags[tag.name] = tag
        return question
    
    def answer_question(self, user: User , question : Question, content : str) -> Answer:
        answer = user.answer_question(question, content)
        self.answers[answer.id] = answer
        return answer
    
    def get_answers(self, question : Question):
        return question.get_answers()

    def add_comment(self, user: User, commentable : Commentable, content : str) -> Commentable:
        return user.comment_on(commentable, content)

    def vote_question(self, user: User, question : Question, value : int) -> None:
        question.vote(user, value)

    def vote_answer(self, user: User, answer : Answer, value : int) -> None:
        answer.vote(user, value)
    
    def accept_answer(self, answer : Answer):
        answer.accept()
    
    def search_question(self, query : str) -> List[Question]:
        questions: List[Question] = []
        for q in self.questions.values():
            if query.lower() in  q.title or query.lower() in q.content or query.lower():
                questions.append(q)
        return questions
    
    def get_questions_by_user(self, user: User) -> List[Question]:
        return user.questions
    
    def get_answers_by_user(self, user: User) -> List[Answer]:
        return user.answers
    
    def get_user_by_id(self, _id : int) -> User:
        return self.users.get(_id)
    
    def get_question_by_id(self, _id : int) -> Question:
        return self.questions.get(_id)
    
    def get_answer_by_id(self, _id : int) -> Answer:
        return self.answers.get(_id)
    
    def get_tag_by_name(self, name : str) -> Tag:
        return self.tags.get(name)




