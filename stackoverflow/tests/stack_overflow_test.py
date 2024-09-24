from src.stack_overflow import StackOverflow
from models.tag import Tag


def printF(*data):
    if data is None:
        print("None")
    else:
        print(data)

class StackOverflowTest:
    
    @staticmethod
    def run():
        stackOverflow = StackOverflow()

        amiya = stackOverflow.create_user("Amiya", "amiyamaity23@gmail.com")
        abc = stackOverflow.create_user("ABC", "abc@gmail.com")
        pqr = stackOverflow.create_user("pqr", "pqr@gmail.com")
        xyz = stackOverflow.create_user("xyz", "xyz@gmail.com")

        #questions
        recursion_question = stackOverflow.ask_question(amiya, "What is recursion?", "Can someone explain about the recursion?", [Tag("programming"), Tag("tree"), Tag("DSA")])

        #answers
        recursion_answer1 = stackOverflow.answer_question(abc, recursion_question, "Recursion is defined as a process which calls itself directly or indirectly")
        recursion_answer2 = stackOverflow.answer_question(pqr, recursion_question, "Can you check this link? https://www.geeksforgeeks.org/what-is-recursion/")
        
        #comments
        comment1 = stackOverflow.add_comment(amiya, recursion_answer1, "Thank you ABC!!")
        comment2 = stackOverflow.add_comment(amiya, recursion_answer2, "Thank you PQR!!")


        #vote
        stackOverflow.vote_question(xyz, recursion_question, 1)
        
        stackOverflow.vote_question(xyz, recursion_answer1, 1)
        stackOverflow.vote_question(xyz, recursion_answer2, -1)

        stackOverflow.vote_question(pqr, recursion_answer1, 1)


        #accepted
        stackOverflow.accept_answer(recursion_answer1)



        #printF
        printF("Question:",  recursion_question.content, " vote count: ", recursion_question.get_vote_count())  
      
        printF("Answers-")
        for ans in stackOverflow.get_answers(recursion_question):
            printF("Answer: ", ans.content, " author:", ans.author.name,  " Vote count:", ans.get_vote_count())

            printF("Comments: ")
            for comment in ans.get_comments():
                printF(comment.content)


        #Reputations
        printF("get_reputation Name:",amiya.name, " reputation:", amiya.get_reputation())
        printF("get_reputation Name:",abc.name, " reputation:", abc.get_reputation())
        printF("get_reputation Name:",pqr.name, " reputation:", pqr.get_reputation())
        printF("get_reputation Name:",xyz.name, " reputation:", xyz.get_reputation())
StackOverflowTest.run()