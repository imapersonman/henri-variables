from Question import Question
from Expression import Int, Plus, Equals, Var, Minus

def check_sub_q(a):
    return a.interpret() == True

questions = [
    Question("If a = 1, what is another way of writing 'b'?", lambda a: a == Var("b")),
    Question("If x = 3, what is another way of writing 'x + y?'", lambda a: a == Plus(Int(3), Var("y"))),
    Question("Use substitute to make '11 + a = 17' True // copy-paste Equals(Plus(Int(11), Var(\"a\")), Int(17))", check_sub_q),
    Question("Use substitute and Minus to make '44 - b = 20' True // copy-paste Equals(Minus(Int(44), Var(\"b\")), Int(20))", check_sub_q),
    Question("Use substitute to make '30 + 50 = x' True // copy-paste Equals(Plus(Int(30), Int(50)), Var(\"x\"))", check_sub_q),
    Question("Use substitute to make 'y - 7 = 33' True // copy-paste Equals(Minus(Var(\"y\"), Int(7)), Int(33))", check_sub_q),
    Question("Use substitute to make 'n + 50 = 140' True // copy-paste Equals(Plus(Var(\"n\"), Int(50)), Int(140))", check_sub_q),
    Question("Use substitute to make '11 + m = 31' True // copy-paste Equals(Plus(Int(11), Var(\"m\")), Int(31))", check_sub_q),
    Question("Use substitute to make 'p - 7 = 23' True // copy-paste Equals(Minus(Var(\"p\"), Int(7)), Int(23))", check_sub_q),
    Question("Use substitute to make '70 - n = 20' True // copy-paste Equals(Minus(Int(70), Var(\"n\")), Int(20))", check_sub_q)
]

class QuestionMachine:
    def __init__(self, questions):
        self.questions = questions
        self.current_index = 0
    
    def ask(self):
        if self.current_index >= len(self.questions):
            return "You're done! Congratulations!"
        return self.questions[self.current_index]
    
    def answer(self, answer):
        if self.current_index >= len(self.questions):
            print("No more questions!")
        question = self.questions[self.current_index]
        response_prefix = "Question: {}\nAnswer: {}\n".format(self.questions[self.current_index], answer)
        if (question.check_answer(answer)):
            self.current_index += 1
            print("{}Correct!".format(response_prefix))
            print("\nNext Question: {}".format(self.ask()))
        else:
            print("{}Incorrect.  Try again.".format(response_prefix))